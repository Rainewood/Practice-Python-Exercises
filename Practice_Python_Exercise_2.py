'''
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
8-24-17 by Rainewood
'''

numToCheck = float(input("Please input a number to determine odd or even: "))


def oddsEvens(numToCheck):
    if numToCheck == 0:
        print("This number is even.")
    elif (numToCheck % 2) == 0:
        if (numToCheck % 4) == 0:
            print("This number is even and a multiple of 4!")
        else:
            print("This number is even.")
    else:
       print("This number is odd.")

oddsEvens(numToCheck)

