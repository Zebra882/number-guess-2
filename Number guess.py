import random
playing= True
num=str(random.randint(20,30))
print("I will genarate a number from 20 to 30 and you have to guess it. Guess 1 digit at a time.")
print("The game ends when you get one Hero!")

while playing:
    
    guess= input("Give me your best guess. ")
    
    if num==guess:
        print("You win the game. ")
        
        print("The number was",num)
        break
    else:
        print("Your guess is not right. Try again. \n")
        
    