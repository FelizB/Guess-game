import random
import numpy as np

number_list=[]
for numbers in range(1,101):
    number_list.append(numbers)
# print(number_list)

trials=0
def easy():
    global trials
    trials=10
    return trials

def standard():
    global trials
    trials=7
    return trials

def hard():
    global trials
    trials=5
    return trials
difficulty={
    "1":easy,
    "2":standard,
    "3":hard
}


# for levels in difficulty:
    # print(levels)
leveled=input("Select difficulty with 1 being easy,2- standard and 3- hard : ")

difficulty[leveled]()

Guess=random.choice(number_list)
print (Guess)


def find_nearest(number):
    arrayed=[5,15,25,35,45,55,65,75,85,95]
    array = np.asarray(arrayed)
    idx = (np.abs(array - number)).argmin()
    return array[idx]
    
created=find_nearest(Guess)
numbered=[]
for numbers in range(created-5,created+6):
    numbered.append(numbers)
# print(numbered)
not_over=False
def calculate_value(value):
    global trials
    if value==Guess and trials!=0:
        return (f"You got it correct. Guess is {Guess}")
    else:
        if value in numbered and value!=Guess and trials!=0:
            trials-=1
            return (f"You are close, Number is within {numbered[0]}-{numbered[-1]}.You have {trials} trials remaining.Try again")
            
        elif value>50 and value!=Guess and Guess<50 and trials!=0:
            trials-=1
            return (f"Number is less than 50. You have got {trials} trials remainng.Try again")
            
        elif value<50 and value!=Guess and Guess>50 and trials!=0:
            trials-=1
            return (f"Number is more than 50. You have got {trials} trials remainng.Try again")
        elif trials==0:
            return (f"You lost. Trials are {trials}")
        elif value not in numbered and value<=100:
            trials-=1
            return (f"You are pretty close. Remaining {trials} trials.Try again")
        elif value>100:
            trials-=1
            return (f"Select a value in range provided")
        
    
    


def start_here():
    global not_over
    number=int(input(f"I have a number between 1 and 100. You have {trials} trials yo get it correct.Enter a number to start:\n "))
    calc= calculate_value(number)
    print(calc)
    while not not_over:
        number2=int(input("Enter a value to continue:"))
        calc2=calculate_value(number2)
        if number2!=Guess:
            not_over=False
            print(calc2)
        else:
            not_over=True
            print(calc2)
   

start_here()

    
    
    