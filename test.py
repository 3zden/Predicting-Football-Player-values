from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


url = "https://www.transfermarkt.fr/afc-sunderland/startseite/verein/289/saison_id/2025"

path  = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = Options()
options.binary_location = path 
# Initialize the driver (use ChromeDriver)
driver = webdriver.Chrome(service=Service(), options=options)
driver.get(url)
container = driver.find_element(By.XPATH , "//*[@id='yw1']/table/tbody")
alllinks= container.find_elements(By.XPATH , '//*[@id="yw1"]/table/tbody/tr/td/table/tbody/tr/td/a')
links = pd.DataFrame(columns = ['Player','link'])
for link in alllinks :
    link = link.get_attribute("href")
    name = " ".join(link[28:].split("/")[1].split("-"))
    print(link, '\n',name)
    if name not in links['Player'].values :
        links.loc[len(links)] = [name,link]
    continue
    
print(links)
