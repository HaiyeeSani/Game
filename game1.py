import random
import sys
print("Hey bro!This is the number guessing game that you will have 3 tries to win")

while True:
    try :
        min = int(input("Input your minimum number      : "))
        break
    except :
        print ("I want to you put number bro!!")

while True:
    try :
        max = int(input("Input your maximum number      : "))
        break
    except :
        print ("I want to you put number bro!!")
def playgame():
    global min
    global max
    def restart():
        restart = input("""Do you want to try again??  
yes    or   no           :  """).lower()
        if restart == "yes":
            return playgame()
        else:
            sys.exit("..............Thank you for enjoying...............")
    guesses = 3
   
            
    num = random.randint(min,max)
    answer = 0
    while num!= answer and guesses > 0:
        answer = int(input("Guess your number              : "))
        guesses -= 1
        if answer > num:
            print("It's high, number of guesses left  : " +str(guesses))
        elif answer < num:
            print("It's low, number of guesses left : " +str(guesses))
        elif answer == num:
            if guesses == 2:
                print("""This is unbelivable!,you spend only one time 
Congratulation, You won!""")
                restart()
            elif guesses == 0:
                print("""You won but you're bad guesser
So don't guess when you take a exam!!""")
                restart()
            else:
                print("Yaaa Habibi. You won!!")
                restart()
    if answer != num:
        print("Good Trying, sorry, the number was : " +str(num))
        restart()
playgame()
