# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 09:06:24 2020

@author: Athma_000
"""
import parallel_crawl
import format_wget_files

if __name__ == "__main__":

       # Example webpages
    #    start_url = "https://huyenchip.com/"
    #    start_url = "http://eloquentix.com"
    #    strrt_url = https://www.gatesnotes.com/

    print("This program crawls concurrently a website and downloads it")
    print("You can specify the url, the depth and the number of workers that will work for you :)")

    depth = int(input("Select depth (default 2) = ") or 2)
    print("Depth = " + str(depth))

    number_of_workers = int(input("Select number of workers (default 10) = ") or 10)
    print("Number of workers = " + str(number_of_workers))

    start_url = str(input("Give valid url -- eg. 'https://www.gatesnotes.com' (default is eloquentix.com) : " ) or "http://eloquentix.com")
    print("URL = " + start_url)

    print("#######################################################")
    print("Running...")

    parallel_crawl.main(start_url, depth, number_of_workers)

    format_wget_files.fix()
