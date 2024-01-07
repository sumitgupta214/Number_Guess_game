import random



'''(:---Number Guessing Game---:)'''



#Easy level Game -->
def easyRange():
    num = random.randrange(1,10,1)
    print("To win guess a number between 1 to 10 \nTo quit Enter : 0 ")
    guess = int(input("Enter number : "))
    while guess != num and guess != 0:
        guess = int(input("Wrong Number Try Again : "))
    #end-While
    if guess == num :
        print("You Guessed the right Number!")
    elif guess == 0:
        print("You Quit! The number is : ",num)


#Medium Level Game -->

def midRange():
    num = random.randrange(1,50,1)
    print("To win guess a number between 1 to 50 \nTo quit Enter : 0 ")
    guess = int(input("Enter number : "))
    while guess != num and guess != 0:
        guess = int(input("Wrong Number Try Again : "))
    #end-while
    
    if guess == num :
        print("You Guessed the right Number!")
    elif guess == 0:
        print("You Quit! The number is : ",num)


#Hard level game -->
def hardRange():
    num = random.randrange(1,100,1)
    print("To win guess a number between 1 to 100 \nTo quit Enter : 0 ")
    guess = int(input("Enter number : "))
    while guess != num and guess != 0:
        guess = int(input("Wrong Number Try Again : "))
    #end-while

    if guess == num :
        print("You Guessed the right Number!")
    elif guess == 0:
        print("You Quit! The number is : ",num)


#Main program -->
def game():
    level = int(input("Enter the level you want to play : \nFor Easy Enter 1.\nFor Medium Enter 2.\nFor Hard Enter 3.\nTo Quit Enter 0.\n"))
    if level == 1:
        easyRange()
    elif level ==2:
        midRange()
    elif level == 3:
        hardRange()
    elif level==0:
        print("You Quit!")
    else:
        print("---->>Invalid Choice please choose a right LEVEL!<<----\n=======================================================")
        game()

#calling main game function -->
game()