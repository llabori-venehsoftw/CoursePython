#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:30:31 2020

@author: llabori
"""

import feedparser

BBC_FEED = "http://feeds.bbci.co.uk/news/world/rss.xml"
FEED = feedparser.parse(BBC_FEED)

for article in FEED['entries']:
    print(article['link'])

def tail(t):
    return t[1:]
    
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)
print(letters)