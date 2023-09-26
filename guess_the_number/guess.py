# import random 

# def random_number_guess(x):
#     random_number = random.randint(1,x)
#     guess =1
    
#     while random_number_guess != random_number:
#         # if you put == here, then it means, you just let the computer to guess it 
#         # so, to let not to guess, you make the condition above
#         guess = int(input(f'Enter your guess from 1 to {x}: '))
        
#         if guess < random_number:
#             print("the guess is too low")
        
#         elif guess > random_number:
#             print("the guess is too high")

        
#         print(f"you did it, the {random_number} is the correct guess ")
        
        

# random_number_guess(10) 


import random 

def random_number_guess(x):
    random_number = random.randint(1,x)
    print(random_number)
    
    while random_number_guess != random_number:
        guess = input(f"Enter your guess from 1 to {x}: ")
        
        if guess == random_number:
            print("you did it ")
        else:
            print ("Sorry, next try")
        

random_number_guess(10) 

# try a variation in this, like add certain condition whether your guess is too high, or too low. something like this,and let me know
