# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:22:37 2020

@author: Athma_000
"""

#TODO threading
#TODO can change html.parser to xml from lxml library. It's slightly faster maybe add later for docker
#TODO save page's css, js etc.
#TODO rate limiting 
#TODO robot.txt

import requests
from bs4 import BeautifulSoup



main_url = "https://huyenchip.com"
set_of_visited_pages = set()

def recursive_crawl(url, depth):
    if depth == 0:
        return None
    
    links = fetch_links(url)
    
    print("Level : ", depth, url)
    for link in links:
        try:
            if is_link_valid(link) is True:
                recursive_crawl(main_url + link.get('href'), depth - 1)
        except:
            continue
        

def fetch_links(url):
    page = requests.get(url)
    set_of_visited_pages.add(url)
    
    soup = BeautifulSoup(page.content, 'html.parser') # add on_duplicate_attribute='ignore' later in docker/ linux
    links = soup.find_all('a')
    return links

def is_link_valid(link):
    if ':' in link.get('href'):
        return False
    if '#' in link.get('href'):
        return False
    if main_url + link.get('href') in set_of_visited_pages:
        return False
    return True
    

recursive_crawl(main_url, 4)


'''
for link in links:
    print(link.get('href'))
                '''
                
   




