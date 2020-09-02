def is_triangle(a,b,c):
    if a+b > c and b + c > a and c + a > b:
        print("issa triangle")
    elif int(a)+int(b) == int(c) or int(b) + int(c) == int(a) or int(a) + int(c) == int(b):
        print("bassard triangle")
    else:
        print("no triangless")
def use_time():
    a = input("l1")
    b = input("l2")
    c = input("l3")
    is_triangle(a,b,c)

while True:
    use_time()
