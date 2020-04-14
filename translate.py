# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:44:50 2020

@author: szymo
"""

from googletrans import Translator
import requests

def googletrans():
    translator = Translator()
    result = translator.translate('How do you do?',dest='pl')
    print(result.text)
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
   
    response = requests.post(url, data=data)
    print(type(response.text))
    
piratetrans('Hello, sir')