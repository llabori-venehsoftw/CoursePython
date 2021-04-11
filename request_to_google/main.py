#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:18:26 2020

@author: llabori
"""

import requests

print(requests.get("https://www.google.com").text)