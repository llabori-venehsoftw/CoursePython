#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:59:17 2020

@author: llabori
"""

from namesplitter02.utils import name_helper

def test_two_names():
    assert name_helper.split_name("Jhon Smith") == ["Jhon", "Smith"]
    
def test_middle_names():
    assert name_helper.split_name("Jhon Patrick Smith") == ["Jhon Patrick", "Smith"]
    assert name_helper.split_name("Jhon Patrick Thomson Smith") == ["Jhon Patrick Thomson", "Smith"]
    
def test_surname_prefixes():
    assert name_helper.split_name("Jhon van der Berg") == ["Jhon", "van der Berg"]
    assert name_helper.split_name("Jhon Patrick van der Berg") == ["Jhon Patrick", "van der Berg"]
    
def test_split_name_onename():
    assert name_helper.split_name("Smith") == ["", "Smith"]
    
def test_split_name_onenames():
    assert name_helper.split_name("") == ["", ""]