# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:22:37 2020

@author: Athma_000
"""
#TODO cli
#TODO combine threading with download_files.py or wget
#TODO threading
#TODO can change html.parser to xml from lxml library. It's slightly faster maybe add later for docker
#TODO rate limiting 
#TODO robot.txt

import requests
from bs4 import BeautifulSoup
import queue
from queue import Empty 


main_url = "https://huyenchip.com"
#main_url = "http://eloquentix.com"
set_of_visited_pages = set()
# Create a queue that we will use to store our "workload".
q = queue.Queue()

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
#    set_of_visited_pages.add(url)
    
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
    

recursive_crawl(main_url, 6)
    
###########################################################################################################################
'''
for url, depth in iter(q.get, SENTINEL):
        if depth == 0:
            break
        time.sleep(1)
'''

def parallel_search(q, set_of_visited_pages):
    while 1:
        try:
            url , depth = q.get()
            if depth <= 0:
                break
        except queue.Empty:
            continue

        try:
            set_of_visited_pages.add(url)
            links = fetch_links(url)
            
            print("Level : ", depth, url)
            for link in links:
                try:
    #                print(link)
                    if is_link_valid(link) is True:
                        q.put((main_url + link.get('href'), depth - 1))
                except:
                    continue
        except (requests.exceptions.InvalidSchema, 
                requests.exceptions.ConnectionError):
            pass
    

import time
import threading

#urls=[]
threads = []

q.put((main_url, 3))                
start = time.time()

for _ in range(workers):
    t = threading.Thread(target=parallel_search, args=(q, set_of_visited_pages))
    threads.append(t)
    t.deamon = True
    t.start()
    
for thread in threads:
    print("In thread")
    print(thread)
    thread.join()
    print("after join")
    
print(f"3 levels deep in {time.time() - start}s")
    


if __name__ == "__main__":
    levels = 2
    workers = 2
    start_url = "https://huyenchip.com"
    seen = set()
    urls = []
    threads = []
    q = queue.Queue()
    q.put((start_url, levels))
    start = time.time()
    
    for _ in range(workers):
        t = threading.Thread(target=parallel_search, args=(q, seen))
        threads.append(t)
        t.daemon = True
        t.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Found {len(urls)} URLs using {workers} workers "
          f"{levels} levels deep in {time.time() - start}s")
























