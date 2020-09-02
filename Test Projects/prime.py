def get_prime(a,b):
    for number in range(a,b):
        number/2


def is_prime(x):
    num = 1
    for i in range(0, (x//2)):
        try:
            if x % i == 0:
                print("Not a prime")
                return False
            else:
                print(x + ": It's a Prime!")
                return True
        except:
            ZeroDivisionError


while True:
    
    is_prime(int(input("Choose a number")))
