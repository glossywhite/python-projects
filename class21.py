# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:06:03 2020

@author: szymo
"""

import urllib.request
from bs4 import BeautifulSoup

argument = input('URL: ')
response = urllib.request.urlopen(url)
data = response.read()
file = BeautifulSoup(data, 'html.parser')

lists = file.find_all('ol')
for li in lists:
    i = 1
    list_elements = li.find_all('li')
    print('\n')
    for l in list_elements:
        print(str(i) + '. ' + l.get_text())
        i += 1