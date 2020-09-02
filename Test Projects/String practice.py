# string practice

# different escape characters (allows you to use characters that aren't usually permitted,
#                       begin with a \)
# - \' (single quote)
# - \" (double quote)
# - \t (tab)
# - \n (new line)
# - \\ (backslash)

print("Hello,\nHow are you?\nThis was a test")

#r"" creates a raw string, ignoring escape characters - useful for ex. C\:users\nigel etc.

#Triple quotes (""" """) are multi line strings, in which spaces and tabs are considered part of the string

print("""This is another test,


to demonstrate the use of multiline quotes,


which has succeeded""")


"""This is a test comment
   which can span multiple
   lines, same use as #"""


#Strings can be indexed and sliced like lists, in the following fashion:

test_quote = "This is an indexing test"
print(test_quote)
print(test_quote[0])
print(test_quote[0:5])
print(test_quote[:10])
print(test_quote[10:])

inx = test_quote[11:19]
print(inx)


#the in and not in operators return boolean values, in the following fashion:

if "This" in test_quote:
    print("'This' is in the variable test_quote")

if "Lettuce" not in test_quote:
    print("'Lettuce' is not in the variable test_quote")

def is_it_in_tq():
    user_word = input("Do you want to know if any other words are in the variable test_quote? Enter a word, or no")
    if user_word.lower() == "no":
        print("No problem")
    else:
        if user_word in test_quote:
            print("That word is in test_quote")
            is_it_in_tq()
        else:
            print("That word is not in test_quote")
            is_it_in_tq()

is_it_in_tq()


#you can use the %s operator to put strings inside of other strings without having to use contantenation:

new_variable = "Second quote test"


print("The variable test_quote is %s and my new variable is %s" %(test_quote, new_variable))

#you can use f strings in a similar manner by employing braces {}

print(f"This is f strings{test_quote}, {new_variable}")


# you can use upper(), lower() and isupper() to change the format of test, or return a boolean value:

print(test_quote.upper())
print(test_quote.lower())

lower_quote = test_quote.upper()

if lower_quote.isupper():
    print("lower_quote is lower case")

#y you can also use:
    #string.isalpha()
    #string.isdecimal()
    #string.isalnum()
    #string.isspace()
    #string.istitle()
test_username = "1!"
def username_input():
    test_username = " "
    while test_username.isalpha == False:
        test_username = input("Please enter a username (no numbers or special characters)")
username_input()





