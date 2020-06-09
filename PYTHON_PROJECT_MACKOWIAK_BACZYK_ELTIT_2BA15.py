# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:03:33 2020

@author: szymo
"""
from googlesearch import search 



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
while True:
    question_1 = input("Do you prefer to learn about a) how small parts form into a bigger whole or b) how the bigger parts interact with each other?")
    if question_1 == 'a':
        result3_count += 1
        print("You've chosen a")
        break
    elif question_1 == 'b':
        result2_count += 1
        print("You've chosen b")
        break
    print("Incorrect answer: type a or b")
#q2
while True:
    question_2 = input("Do you prefer to learn about a) sounds/sound systems or b) the connection between language and cognition?")
    if question_2 == 'a':
        result5_count += 1
        print("You've chosen a")
        break
    elif question_2 == 'b':
        result9_count += 1
        print("You've chosen b")
        break
    print("Incorrect answer: type a or b")
#q3
while True:
    question_3 = input("Would you like to a) find out hidden meaning encoded in language or b) study how we are able to acquire language?")
    if question_3 == 'a':
        result4_count += 1
        print("You've chosen a")
        break
    elif question_3 == 'b':
        result8_count += 1
        print("You've chosen b")
        break
    print("Incorrect answer: type a or b")   
#q4
while True:
    question_4 = input("Would you like to a) learn about the development of linguistic universals or b) find out where does the variation in language come from?")
    if question_4 == 'a':
        result10_count += 1
        print("You've chosen a")
        break
    elif question_4 == 'b':
        result6_count += 1
        print("You've chosen b")
        break
    print("Incorrect answer: type a or b")  
#q5
while True:
    question_5 = input("Would you like to know how language changes with time or learn what are the psychological factors enabling us to understand language?")
    if question_5 == 'a':
        result1_count += 1
        print("You've chosen a")
        break
    elif question_5 == 'b':
        result7_count += 1
        print("You've chosen b") 
        break
    print("Incorrect answer: type a or b")  
#q6
while True:
    question_6 = input("Are you interested in psychology and human brain ? a) yes b) no")
    if question_6 == 'a':
        result7_count += 1
        print("You've chosen a")
        break
    elif question_6 == 'b':
        print("You've chosen b") 
        break
    print("Incorrect answer: type a or b")  
#q7
while True:
    question_7 = input("Have you ever wondered how do we learn second/third/etc language and how they influence each other ? a) yes b) no")
    if question_7 == 'a':
        result8_count += 1
        print("You've chosen a")
        break
    elif question_7 == 'b':
        print("You've chosen b") 
        break
    print("Incorrect answer: type a or b") 
#q8
while True:
    question_8 = input("Did you enjoy studying theory of evolution in biology classes? a) yes b) no")
    if question_8 == 'a':
        result10_count += 1
        print("You've chosen a")
        break
    elif question_8 == 'b':
        print("You've chosen b")
        break
    print("Incorrect answer: type a or b")  
#q9
while True:
    question_9 = input("Are you intrested more in a) how sth has changed or b) why has it changed?")
    if question_9 == 'a':
        result1_count += 1
        print("You've chosen a")
        break
    elif question_9 == 'b':
        result6_count += 1
        print("You've chosen b") 
        break
    print("Incorrect answer: type a or b") 
#q10
while True:
    question_10 = input("Do you like to look for logic in task that you’re performing ? a) yes b) no")
    if question_10 == 'a':
        result2_count += 1
        print("You've chosen a")
        break
    elif question_10 == 'b':
        result2_count += 1
        print("You've chosen b")
        break
    print("Incorrect answer: type a or b")  
#q11
    
#q12
    
#q13
    
#q14
    
#q15
    
#q16

#q17
    
#q18
    
#q19
    
#q20
    
































































#calculate which result has the highest number of 'points' after the quiz is over
maxscore = max(result1_count, result2_count, result3_count, result4_count, result5_count,
               result6_count, result7_count, result8_count, result9_count, result10_count)
#show the result of the quiz and provide user with a link from google
print("Your result is: ")
if maxscore == result1_count:
    print("historical linguistics -> The study of language change over time")
    google_result = "historical linguistics"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result2_count:
    print("syntax -> The study of the rules that govern the structure of sentences, and which determine their relative grammaticality")
    google_result = "syntax"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result3_count:
    print(")morphology -> The study of morphemes, the smallest units of grammatical meaning, such as inflection and affixes")
    google_result = "morphology"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result4_count:
    print("semantics and pragmatics -> The study of meaning as encoded in language and the study of how context contributes to meaning")
    google_result = "semantics and pragmatics"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result5_count:
    print("phonetics and phonology -> The study of the sounds of human speech and the sound systems of specific languages")
    google_result = "phonetics and phonology"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result6_count:
    print("sociolinguistics -> The study of variation in language and its relationship with social factors")
    google_result = "sociolinguistics"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result7_count:
    print("psycholinguistics and neurolinguistics -> The study of the psychological and neurobiological factors that enable humans to acquire, use, and understand language")
    google_result = "psycholinguistics and neurolinguistics"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result8_count:
    print("language acquisition -> The study of how children and adults acquire language knowledge and ability")
    google_result = "language acquisition"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result9_count:
    print("cognitive linguistics -> The study of language and cognition (thinking)")
    google_result = "cognitive linguistics"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 
elif maxscore == result10_count:
    print(")evolutionary linguistics -> The study of the psychosocial and cultural factors involved in the origin of language and the development of linguistic universals")
    google_result = "evolutionary linguistics"
    for i in search(google_result, tld="co.in", num=10, stop=1, pause=1): 
        print(i) 




















