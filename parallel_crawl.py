# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:01:44 2020

@author: Athma_000
"""

import queue
import requests
import threading
import time
from bs4 import BeautifulSoup

def search_links(q, urls, seen):
#    while searching_process.is_set():
    while 1:
        try:
#            print("I thread : " + str(threading.current_thread()) + " I request access to the queue ")                        
            url, level = q.get_nowait()
#            print("I thread : " + str(threading.current_thread()) + " received url: " + str(url)
#            +" and level : " + str(level))
            q.task_done()
        except queue.Empty:
#            print("Queue empty")
            continue

        if level == 0: 
            print("REACHED ZERO")
            break

        if stop_threads == True:
            break
        
        try:
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            
            for x in soup.find_all('a'): 
    
                link = x.get("href")
                
                if link and link[0] in "#/":
                    link = start_url + link
    
    
                if start_url not in link:
                    continue
                
                if link not in seen:
                    seen.add(link)
                    urls.append(link) 
                    q.put((link, level - 1))
#                    print("I thread : " + str(threading.current_thread()) + " I put " + str(link) +" in queue")
#                    print(" ")
#                try:
#                    print(" ")
#                    for q_link in q.queue:
#                        print(q_link)
                        
#                    print("#################################")
#                except Exception as e:
##                    print(e)
#                    print("Q is probably empty")
#                    continue
        except Exception as e:
#            print(e)
#            print(threading.active_count())
            continue
#

if __name__ == "__main__":
    stop_threads = False
    levels = 2
    workers = 10
#    start_url = "https://huyenchip.com/"
#    start_url = "http://eloquentix.com"
    start_url = "https://www.gatesnotes.com/"

    seen = set()
    urls = []

    threads = []
    q = queue.Queue()
    q.put((start_url, levels))
    start = time.time()
    
#    searching_process = threading.Event()
#    searching_process.set()
    
    for _ in range(workers):
        t = threading.Thread(target=search_links, args=(q, urls, seen))
        threads.append(t)
        t.daemon = True
        t.start()
    
#    time.sleep(20)
#    searching_process.clear()
    
    for thread in threads:
        print("JOIN ME  : " + str(thread))
        thread.join(5.0)


    print(f"Found {len(urls)} URLs using {workers} workers "
          f"{levels} levels deep in {time.time() - start}s")
    
    