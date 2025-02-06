import  random
import sys


#this is the function we are calling
def game(nog, random_number, user_value):
    if random_number == user_value:
        print("Congratulations, you guessed right")
        sys.exit()
    elif random_number > user_value:
        print("Your guess is Low\n")
        
    else:
        print("Your guess is High\n")
        


print("Hello, Welcome to the game of random number generator \n")
print("I will say whether your guess is higher or lower\n")
print("You have a total of 3 guesses\n")
nog = 3
#Generating a random number
random_number = random.randint(1,20)

#While loop as it decrement takes place after each itheration so loop runs until guesses is greater than 0
while nog > 0:
    print("You have", nog, "guesses left\n") #decreased guesses are shown every time
    user_value = int(input("Enter your guess from 1 to 20: "))
    if 1 <= user_value <= 20: #user value has to be from 1 to 20
        print("Your number is ", user_value)
        game(nog, random_number, user_value) #passing variables to function
    else:
        print("Please enter a value between 1 and 20.")
    nog -= 1 #decrement takes place

#printing the actual number
print("The actual number is", random_number)

