import random

number_to_guess= random.randint(1,100)
while True:
    try:
        guess = int(input("Enter a number_to_guess: "))
        if (guess< number_to_guess):
            print("too low")
        elif(guess > number_to_guess):
            print("too hight")
        else:
            print("Well done")
            break
    except ValueError:
        print("plaese enter a valid number")