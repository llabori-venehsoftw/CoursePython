#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:57:57 2020

@author: llabori
"""
""" Segundo ejemplo con archivos XML """

import xml.sax

from xml.etree.ElementTree import parse

xml_doc = parse('note.xml')
for ele in xml_doc.findall('pro'):
    print(ele.text)