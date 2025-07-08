import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def get_player_data(player_url):
    """
    Scrapes player data from Transfermarkt player profile page.
    
    Args:
        player_url (str): URL of the player's Transfermarkt profile page
        
    Returns:
        dict: Dictionary containing player information with keys:
              - Player: Player name
              - Club: Current club
              - Age: Player age
              - Position: Playing position
              - Nation: Nationality
              - Value: Market value
              - Contract: Contract expiration date
              - Years_Left: Years remaining on contract
              - League: Current league
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(player_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize result dictionary
        player_data = {
            'Player': '',
            'Club': '',
            'Age': '',
            'Position': '',
            'Nation': '',
            'Value': '',
            'Contract': '',
            'Years_Left': '',
            'League': ''
        }
        
        # Extract player name
        player_name = soup.find('h1', class_='data-header__headline-wrapper')
        if player_name:
            player_data['Player'] = player_name.get_text(strip=True)
        
        # Extract main player info from the data header
        data_header = soup.find('div', class_='data-header__details')
        if data_header:
            # Age
            age_element = data_header.find('span', class_='data-header__content')
            if age_element and 'years' in age_element.get_text():
                age_text = age_element.get_text(strip=True)
                age_match = re.search(r'(\d+)', age_text)
                if age_match:
                    player_data['Age'] = age_match.group(1)
        
        # Extract info from the info table
        info_table = soup.find('table', class_='info-table')
        if info_table:
            rows = info_table.find_all('tr')
            for row in rows:
                header = row.find('th')
                data = row.find('td')
                if header and data:
                    header_text = header.get_text(strip=True)
                    
                    if 'Position:' in header_text:
                        player_data['Position'] = data.get_text(strip=True)
                    elif 'Current club:' in header_text:
                        club_link = data.find('a')
                        if club_link:
                            player_data['Club'] = club_link.get_text(strip=True)
                    elif 'Contract expires:' in header_text:
                        player_data['Contract'] = data.get_text(strip=True)
                        # Calculate years left
                        if player_data['Contract'] and player_data['Contract'] != '-':
                            try:
                                contract_date = datetime.strptime(player_data['Contract'], '%b %d, %Y')
                                current_date = datetime.now()
                                years_left = (contract_date - current_date).days / 365.25
                                player_data['Years_Left'] = f"{years_left:.1f}" if years_left > 0 else "0"
                            except:
                                player_data['Years_Left'] = 'N/A'
        
        # Extract nationality
        nationality_img = soup.find('img', {'title': True, 'class': 'flaggenrahmen'})
        if nationality_img:
            player_data['Nation'] = nationality_img.get('title', '')
        
        # Extract market value
        market_value = soup.find('div', class_='market-value-development')
        if market_value:
            value_element = market_value.find('div', class_='market-value-number')
            if value_element:
                player_data['Value'] = value_element.get_text(strip=True)
        
        # Alternative market value extraction
        if not player_data['Value']:
            value_spans = soup.find_all('span', class_='waehrung')
            for span in value_spans:
                if span.get_text(strip=True) == '€':
                    parent = span.parent
                    if parent:
                        value_text = parent.get_text(strip=True)
                        if 'm' in value_text.lower() or 'k' in value_text.lower():
                            player_data['Value'] = value_text
                            break
        
        # Extract league information
        club_info = soup.find('span', class_='hauptverein')
        if club_info:
            league_link = club_info.find_next('a')
            if league_link and 'wettbewerb' in league_link.get('href', ''):
                player_data['League'] = league_link.get_text(strip=True)
        
        # Alternative league extraction
        if not player_data['League']:
            league_links = soup.find_all('a', href=True)
            for link in league_links:
                if 'wettbewerb' in link.get('href', '') and 'liga' in link.get('href', '').lower():
                    player_data['League'] = link.get_text(strip=True)
                    break
        
        return player_data
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"Error parsing the webpage: {e}")
        return None

def get_player_data_as_list(player_url):
    data = get_player_data(player_url)
    if data:
        return [
            data['Player'],
            data['Club'],
            data['Age'],
            data['Position'],
            data['Nation'],
            data['Value'],
            data['Contract'],
            data['Years_Left'],
            data['League']
        ]
    return None

# Example usage
if __name__ == "__main__":
    # Test with the provided URL
    url = "https://www.transfermarkt.com/michael-olise/profil/spieler/566723"
    
    # Get data as dictionary
    player_info = get_player_data(url)
    if player_info:
        print("Player Data (Dictionary):")
        for key, value in player_info.items():
            print(f"{key}: {value}")
        
        print("\n" + "="*50 + "\n")
        
        # Get data as list
        player_list = get_player_data_as_list(url)
        print("Player Data (List):")
        print(player_list)
    else:
        print("Failed to retrieve player data")