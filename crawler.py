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
                
             
                
                
                
                ##### 1
import requests              
from urllib.parse import urljoin
# initialize a session
session = requests.Session()
# set the User-agent as a regular browser
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

main_url = "https://huyenchip.com"
                
# get the HTML content
html = session.get(main_url).content

# parse HTML using beautiful soup
soup = bs(html, "html.parser")


path = 'C:/Users/Athma_000/Desktop/'

f = open(path+"testy.html", "w")
f.write(str(soup))
f.close()
                
                
             
                
   






                ##### 2
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# URL of the web page you want to extract
url = "https://huyenchip.com/"

# initialize a session
session = requests.Session()
# set the User-agent as a regular browser
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

# get the HTML content
html = session.get(url).content

# parse HTML using beautiful soup
soup = BeautifulSoup(html, "html.parser")

# get the JavaScript files
script_files = []

for script in soup.find_all("script"):
    if script.attrs.get("src"):
        # if the tag has the attribute 'src'
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)

# get the CSS files
css_files = []

for css in soup.find_all("link"):
    if css.attrs.get("href"):
        # if the link tag has the 'href' attribute
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)


print("Total script files in the page:", len(script_files))
print("Total CSS files in the page:", len(css_files))

# write file links into files
with open("javascript_files.txt", "w") as f:
    for js_file in script_files:
        print(js_file, file=f)

with open("css_files.txt", "w") as f:
    for css_file in css_files:
        print(css_file, file=f)
                










