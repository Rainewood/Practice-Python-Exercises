'''
http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
8-24-17 by Rainewood
'''

import datetime

name = input("What's your name? ")
#print(name)
age = input("How old are you? ")
#print(age)

def ageCalc (name, age):
    toCentury = 100 - int(age)
    now = datetime.datetime.now()
    duration = int(now.year) + toCentury
    print("\n", name, "will turn 100 in the year", duration)

    n = int(input("How many times do you want this repeated? "))
    print("\n")
    for i in range(0, n):
        print(name, "will turn 100 in the year", duration, "\n")


ageCalc(name, age)

