import bs4
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

print(selenium('Copenhagen Flames'))
