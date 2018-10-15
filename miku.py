# All about Miku
# Created by Astral
# Date: 10/10/18
# Description: Fetches the text and or content from (url) using the following api's, Requests and BeautifulSoup. Displays the information in a user friendly manner.

import requests
import time
from bs4  import BeautifulSoup

def aboutmiku():
    clear()
    # Where to collect from
    url = requests.get("https://ec.crypton.co.jp/pages/prod/vocaloid/cv01_us")
    soup = BeautifulSoup(url.content, 'lxml')
    
    # Part 1
    article = soup.find('div', class_='ctn1')
    headline = article.h1
    text = article.p, article.span

    # Part 2
    article2 = soup.find('div', class_='ctn2')
    facts = article2.h2, article2.p, article2.span


    print(headline)
    print(text)
    print(facts)

# Clears the screen for a better user interface
def clear():
    print("\n"*100)

# User operations
def main():
    print("Welcome to All about Miku!")
    time.sleep(10)
    aboutmiku()

main()
