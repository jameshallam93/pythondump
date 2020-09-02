numbers = []

def input_list():
    new_number = input("Add a number (type done to finish)")
    if new_number == "done":
        meaning(numbers)
    else:
        numbers.append(new_number)
        input_list()
        
def meaning(list_x):
    for i in list_x:
        if i == "42":
            print(i)
            print("Ah, the meaning of life!")
            break
        else:
            print(i)
            
while True:
    numbers = []
    input_list()
    
    
