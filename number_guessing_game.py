import random
number = random.randint(0,10000)
i = 1
while i == 1:
    x = input("Enter the Number(for quit write end): ")
    if x == "end":
        i = 3
    else:
        comp = int(x)
    
        if comp == number:
            print("Congrats!! You won!!")
            i = 2
        elif comp > number:
            print("Your number is too high")
            i = 1
        elif comp< number:
            print("Your number is too lower")    
            i = 1