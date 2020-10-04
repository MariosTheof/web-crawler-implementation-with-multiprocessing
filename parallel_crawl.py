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
from subprocess import call

set_of_seen_links = set()

def main(url, depth, workers):
    """ Initializes some need variables, starts time calculation
    and starts threads.
    """
    global start_url
    start_url = url
    urls = []
    threads = []
    q = queue.Queue()

    q.put((start_url, depth))
    start = time.time()

    for _ in range(workers):
        t = threading.Thread(target=search_and_download, args=(q, urls, set_of_seen_links))
        threads.append(t)
        t.daemon = True
        t.start()

    for thread in threads:
        thread.join(25.0)

    print(f"Found and downloaded {len(urls)} URLs using {workers} workers "
          f"{depth} levels deep in {time.time() - start}s")


def search_links_in_webpage(url, urls, q, level):
    """ Searches for links in a webpage, using BeautifulSoup
    and checks if link is valid.
    """
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for x in soup.find_all('a'):
        link = x.get("href")

        if link and link[0] in "#/": # if link title is '/' or starts '#/', then concatanate it to main url string
            link = start_url + link
        if is_link_valid(link):
            set_of_seen_links.add(link)
            urls.append(link)
            q.put((link, level - 1))

def search_and_download(q, urls, set_of_seen_links):
    """ Searches links for each webpage in the Queue,
    and downloads the particular webpage that is being searched.
    """
    while True:
        try:
            url, level = q.get_nowait()
            q.task_done()
        except queue.Empty:
            continue
        if level == 0:
            break

        search_links_in_webpage(url, urls, q, level)

        download_page_to_folder(url)



def download_page_to_folder(link):
    """Downloads an html page along with the assets and images, using wget."""
    call(["wget", "--timestamping","-p", "--convert-links", link, "-q"])

def is_link_valid(link):
    ''' Checks if link is valid.'''
    if link is None:
        return False
    if start_url not in link:
        return False
    if link not in set_of_seen_links:
        return True
    return False
