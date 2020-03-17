import bs4
import requests
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WIN_URL = 'https://www.hltv.org/team/7461/copenhagen-flames#tab-matchesBox'

# Brug web scraping til at finde top 5 hold i verden
def webscrape():
    r = requests.get('https://www.hltv.org/ranking/teams/2020/march/9')
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    elems = soup.find_all('span', {'class': 'name'})

    for el in elems[:5]:
        print(el.getText())

# Brug selenium til at finde "Copenhagen Flames" placering på verdensranglisten (Ranking)
def selenium(team):
    browser = webdriver.Chrome()
    browser.get('https://www.hltv.org/')
    browser.implicitly_wait(3)

    search_field = browser.find_element_by_name('query')
    search_field.send_keys(team)
    search_field.submit()

    sleep(3)

    link_to_team = browser.find_element_by_link_text(team)
    link_to_team.click()

    sleep(3)

    page_source = browser.page_source

    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    world_rankings = soup.find_all('div', {'class': 'profile-team-stat'})

    return world_rankings[0].getText()

#print(selenium('Copenhagen Flames'))

# Stadig på "Copenhagen Flames" siden. Find ved hjælp af regex hvor mange sejre de har under matches
def regex(url):
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    elems = soup.select('table > tbody')

    print(elems[1].getText())
    
    win_reg = re.compile(r'<div class="team-flex team-1">')

    wins = win_reg.findall(str(elems[1].getText()))

    #print(wins)

    

regex(WIN_URL)