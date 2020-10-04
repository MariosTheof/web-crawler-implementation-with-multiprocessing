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

seen = set()


def main(url, depth, workers):
    global start_url
    start_url = url
    urls = []
    threads = []
    q = queue.Queue()

    q.put((start_url, depth))
    start = time.time()

    for _ in range(workers):
        t = threading.Thread(target=search_links, args=(q, urls, seen))
        threads.append(t)
        t.daemon = True
        t.start()

    for thread in threads:
        print("JOIN ME  : " + str(thread))
        thread.join(5.0)

    print(f"Found {len(urls)} URLs using {workers} workers "
          f"{depth} levels deep in {time.time() - start}s")


def search_links(q, urls, seen):
#    while searching_process.is_set():
    while 1:
        try:
            url, level = q.get_nowait()
            q.task_done()
        except queue.Empty:
            continue

        if level == 0:
            break

        try:
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            for x in soup.find_all('a'):
                # get link title
                link = x.get("href")

                if link and link[0] in "#/": # if link title is '/' or starts '#/', then concatanate it to main url string
                    link = start_url + link
                if is_link_valid(link):
                    seen.add(link)
                    urls.append(link)
                    q.put((link, level - 1))
        except:
            continue

def is_link_valid(link):
    ''' Checks if link is valid. Specifically if it is within domain and if has been see before'''
    if start_url not in link:
        return False
    if link not in seen:
        return True
    return False




    