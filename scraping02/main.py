#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:47:22 2020

@author: llabori
"""

import requests
import string

from bs4 import BeautifulSoup
from collections import Counter

url = "https://www.bbc.com/news"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")

news_urls = []
for link in links:
    href = link.get("href")
    if href.startswith("/news") and href[-1].isdigit():
        news_url = "https://www.bbc.com" + href
        news_urls.append(news_url)
        
all_nouns = []
for url in news_urls[:10]:
    print("Fetching{}".format(url))
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    words = soup.text.split()
    nouns = [word for word in words if word.isalpha() and word[0] in string.ascii_uppercase]
    all_nouns += nouns
    
print(Counter(all_nouns).most_common(100))
        