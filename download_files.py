# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:10:00 2020

@author: Athma_000
"""
import os
import requests              
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path
    
#TODO eg. assets subfolder to be made automatically

url = "https://huyenchip.com"
path = os.path.abspath('C:/Users/Athma_000/Desktop/')
             
def get_page_html(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    
    html = session.get(url).content

    return html

def get_css_files_list(soup):
    css_files = []
    
    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            if not css.attrs.get("rel")[0] == 'canonical':
                print(urljoin(url,css.attrs.get("href")))
                css_url = urljoin(url,css.attrs.get("href"))
                css_files.append(css_url)

    return css_files
                     
def get_js_files_list(soup):
    script_files = []

    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            print(urljoin(url,script.attrs.get("href")))
            script_url = urljoin(url, script.attrs.get("src"))
            script_files.append(script_url)          
    
    return script_files


def write_html_to_local_file(soup, path):
    # Change pathing 
    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            if css.attrs.get("rel")[0] == 'canonical':
                name = soup.title.text
                css.attrs['href'] = name + '.html'
            else:
                name = css.attrs.get("href").split('/')[-1]
                css.attrs['href'] = name
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            name = script.attrs.get("src").split('/')[-1]
            script.attrs['src'] = name
    name = soup.title.text + '.html'
    f = open(os.path.join(path , name), "w")
    f.write(str(soup))
    f.close()

    
def write_assets_to_local_directory(files, path):
    for url in files:
        if not file_exists_locally(url, path):
            page_content = download_file(url)
            
            name = url.split('/')[-1]
#            print(str(page_content))
            f = open(os.path.join(path , name), "w")
            f.write(str(page_content))
            f.close()

def file_exists_locally(url, path):
    name = url.split('/')[-1]
    path_to_file = Path(path + name)
    return path_to_file.is_file()
        
def download_file(url):
    ''' Not using session, because script/css files will not appear differently for crawlers.
    '''
    page_content = requests.get(url).text
    
    return page_content
    
            
def write_files_to_disk(path,url):
    html = get_page_html(url)
    soup = BeautifulSoup(html, "html.parser")
    
    css_files = get_css_files_list(soup)
    js_files = get_js_files_list(soup)
    
    
    write_assets_to_local_directory(css_files, path)
    write_assets_to_local_directory(js_files, path)
    write_html_to_local_file(soup, path)
            



