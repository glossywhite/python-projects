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
#q1
question_1 = input("Do you prefer to learn about a) how small parts form into a bigger whole or b) how the bigger parts interact with each other?")
if question_1 == 'a':
    result3_count += 1
    print("You've chosen a")
elif question_1 == 'b':
    result2_count += 1
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")
#q2
question_2 = input("Do you prefer to learn about a) sounds/sound systems or b) the connection between language and cognition?")
if question_2 == 'a':
    result5_count += 1
    print("You've chosen a")
elif question_2 == 'b':
    result9_count += 1
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")
#q3
question_3 = input("Would you like to a) find out hidden meaning encoded in language or b) study how we are able to acquire language?")
if question_3 == 'a':
    result4_count += 1
    print("You've chosen a")
elif question_3 == 'b':
    result8_count += 1
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")   
#q4
question_4 = input("Would you like to a) learn about the development of linguistic universals or b) find out where does the variation in language come from?")
if question_4 == 'a':
    result10_count += 1
    print("You've chosen a")
elif question_4 == 'b':
    result6_count += 1
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")  
#q5
question_5 = input("Would you like to know how language changes with time or learn what are the psychological factors enabling us to understand language?")
if question_5 == 'a':
    result1_count += 1
    print("You've chosen a")
elif question_5 == 'b':
    result7_count += 1
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")  
#q6
question_6 = input("Are you interested in psychology and human brain ? a) yes b) no")
if question_6 == 'a':
    result7_count += 1
    print("You've chosen a")
elif question_6 == 'b':
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")  
#q7
question_7 = input("Have you ever wondered how do we learn second/third/etc language and how they influence each other ? a) yes b) no")
if question_7 == 'a':
    result8_count += 1
    print("You've chosen a")
elif question_7 == 'b':
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b") 
#q8
question_8 = input("Did you enjoy studying theory of evolution in biology classes? a) yes b) no")
if question_8 == 'a':
    result10_count += 1
    print("You've chosen a")
elif question_8 == 'b':
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")  
#q9
question_9 = input("Are you intrested more in a) how sth has changed or b) why has it changed?")
if question_9 == 'a':
    result1_count += 1
    print("You've chosen a")
elif question_9 == 'b':
    result6_count += 1
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b") 
#q10
question_10 = input("Do you like to look for logic in task that you’re performing ? a) yes b) no")
if question_10 == 'a':
    result2_count += 1
    print("You've chosen a")
elif question_10 == 'b':
    result2_count += 1
    print("You've chosen b")
else: 
    print("Incorrect answer: type a or b")  
