# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:54:22 2023

@author: Acer
"""

import requests

url = 'https://api.tmsandbox.co.nz/v1/Categories/6329/Details.json?catalogue=false'
response = url

def main_request(url):
    result = requests.get(url)
    return result.json()

def get_relist(response):
    canrelist =response['CanRelist']
    return canrelist

data = main_request(url)
test_case_2 = (get_relist(data))


if test_case_2 is True:
    print ("Test Case 2 passed. CanRelist value is True" )
else: 
    print ("Test Case 2 failed. CanRelist value is not True")
