# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:03:33 2020

@author: szymo
"""




#variables storing 'points' from answered questions
result1_count = 0
result2_count = 0
result3_count = 0
result4_count = 0
result5_count = 0
result6_count = 0
result7_count = 0
result8_count = 0
result9_count = 0
result10_count = 0

#questions with possible answers + adding 'points' to variables
question_1 = input("Do you prefer to learn about a) how small parts form into a bigger whole or b) how the bigger parts interact with each other?")
if question_1 == 'a':
    result3_count += 1
    print("You chose a")
elif question_1 == 'b':
    result2_count += 1
else: 
    print("Incorrect answer: type a or b")

