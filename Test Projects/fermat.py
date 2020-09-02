def equat(a,b,n):
    return (a ** n + b ** n)

def c_value(c,n):
    return (c ** n)

def fermat(a,b,c,n):
    value = equat(a,b,n)
    c_valu = c_value(c,n)
    if value == c_value(c,n):
        print("Fermat was wrong")
    else:
        print("Nope!")
def use_input():
    a = 0
    b = 0
    c = 0
    n = 0
    while a <= 2:
       a = int(input("number 1"))
    while b <= 2:
        b = int(input("number 2"))
    while n <= 2:
        n = int(input("to the power of"))
    ans = equat(a,b,n)
    print(ans)
    while c <= 2:
        c = int(input("number 3"))
    c_val = c_value(c,n)
    print(c_val)
    fermat(a,b,c,n)
while True:
    use_input()
