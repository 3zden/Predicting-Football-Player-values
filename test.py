import requests
from bs4 import BeautifulSoup
import pandas as pd
import re





def scrape_team_players(team_url, PlayersTM):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(team_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find squad table
    squad_table = soup.find('table', class_='items')
    player_rows = squad_table.find_all('tr', class_=['odd', 'even'])
    
    for row in player_rows:
        # Get player name
        name_cell = row.find('td', class_='hauptlink')
        player_name = name_cell.find('a').text.strip()
        
        # Get market value
        value_cell = row.find('td', class_='rechts hauptlink')
        market_value = value_cell.text.strip()
        
        # Convert value to number
        if 'm' in market_value.lower():
            value_num = float(re.findall(r'[\d.]+', market_value)[0]) * 1000000
        elif 'k' in market_value.lower():
            value_num = float(re.findall(r'[\d.]+', market_value)[0]) * 1000
        else:
            value_num = 0.0
        
        # Add to DataFrame
        new_row = pd.DataFrame({
            'Player_Name': [player_name],
            'Market_Value': [market_value],
            'Market_Value_EUR': [value_num]
        })
        
        PlayersTM = pd.concat([PlayersTM, new_row], ignore_index=True)
    
    return PlayersTM



scrape_team_players()