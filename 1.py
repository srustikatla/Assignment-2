First_name = input("Enter the first name: ")
Last_name = input("Enter the last name: ")
fullName = First_name + " " + Last_name

def Full_name(fn,ln):
    print("Full name is: " + fn +" "+ ln)

Full_name(First_name, Last_name)

def string_alternative(str):
    print(str[::2])

string_alternative(fullName)