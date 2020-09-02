def collatz():
    x = input("enter number:")
    int(x)
    while x != 1:
        try:    
            if int(x) % 2 == 0:
                x = int(x) // 2
                print(str(x))
                continue
            else:
                x = 3 * int(x) + 1
                print(str(x))
                continue
        except ValueError:
            print("Please enter a number, not a string")
            continue
while 1:
    collatz()
