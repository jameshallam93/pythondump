import csv
usernames_passwords = {
        "James": "password",
        "Lewis": "changeme",
        "Tom" : "baloney",
        }

def basic_login():  
    x = input("Username:")
    if x in usernames_passwords:
        y = input("Password:")
        if y == usernames_passwords[x]:
            print("Welcome " + x)
    elif x == "New User":
        new_user()
    elif x == "save":
        w = csv.writer(open("output.csv", "w"))
        for key, val in usernames_passwords.items():
            w.writerow([key,val])
        basic_login()
        
def new_user():
    z = input("New username")
    if z in usernames_passwords:
        print("Username taken")
        basic_login()
    else:
            a = input("New password")
            usernames_passwords[z] = a            
basic_login()
y = 0
while y == 0:
    basic_login()
    
    
