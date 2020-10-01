# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:22:37 2020

@author: Athma_000
"""
#TODO do not got to duplicates ## use a set, which by definition is a collection of unique elements.
#TODO threading
#TODO save page's css, js etc.


import requests
from bs4 import BeautifulSoup

url = "http://eloquentix.com/"

set_of_visited_pages = set()


def recursive_crawl(url, depth):
    if depth == 0:
        return None
    if url in set_of_visited_pages:
        return None

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser') # add on_duplicate_attribute='ignore' later in docker/ linux
    links = soup.find_all('a')

    set_of_visited_pages.add(url)
    print("Level : ", depth, url)
    for link in links:
        try:
            if ':' in link.get('href'):
                continue
            if '#' in link.get('href'):
                continue
            #will need to change wikipedia to an abstract url
            recursive_crawl("http://eloquentix.com" + link.get('href'), depth - 1)
        except:
            continue

recursive_crawl(url, 2)



'''
for link in links:
    print(link.get('href'))
                '''
