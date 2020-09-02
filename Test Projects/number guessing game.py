import random
actual = random.randint(1,10)
def guess():
    for attempts in range(1,11):
        try:        
            g = int(input("guess a number between 1 and 10:"))
            if g == actual:
                break
            elif g > actual:
                print("Too high, guess again")
                continue
            elif g < actual:
                print("Too low, guess again")
                continue

        except ValueError:
            print("0 is not a number")
    if g == actual:
        print("correct!")
        print("it took you " + str(attempts) + " attempts to guess the right number!")
    else:
        print("Wrong again! Out of guesses!")
        
guess()
        
            
        
