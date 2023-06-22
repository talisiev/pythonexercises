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

def get_name(response):
    name  = response['Name'] 
    return name


data = main_request(url)
test_case_1 = (get_name(data))


if test_case_1 =="Home & garden":
    print ("Test Case 1 passed. Page name is " + (get_name(data)))
else:
    print ("Test Case 1 failed. Page name is not correct")