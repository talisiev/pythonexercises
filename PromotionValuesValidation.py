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

def parse_api(response):
    promolist = []
    for item in response['Promotions']:
        promo = {
            'Name': item['Name'], 
            'Description': item['Description']
        }
        promolist.append(promo)
    return promolist
    
mainlist = []
data = main_request(url)
mainlist.extend(parse_api(data))

    
if {'Name': 'Feature', 'Description': 'Better position in category'} in mainlist:
    print ("Test Passed. The value Name: 'Feature' with matching Description: 'Better position in category' is in the Promotion array.")
else:
    print ("Test Failed. Target Name matching Description not found")
