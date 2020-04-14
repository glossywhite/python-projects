# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:44:50 2020

@author: szymo
"""

from googletrans import Translator

def main():
    translator = Translator()
    result = translator.translate('How do you do?',dest='pl')
    print(result.text)
    
main()