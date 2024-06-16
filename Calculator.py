# Python program for simple calculator 

# function to add two number
def add(number_1,number_2):
    return number_1 + number_2

# function to subtract two number
def sub(number_1,number_2):
    return number_1 - number_2

# function to divide two number
def div(number_1,number_2):
    return number_1 / number_2

# function to multiple two number
def mul(number_1,number_2):
    return number_1 * number_2

print("To select ADDITION operator press + \n" \
      "To select SUBTRACTION operator press - \n" \
      "To select DIVISION operator press / \n" \
      "To select MULTIPLICATION operator press *")

print()

number_1=int(input("Enter a number "))
select=input("Select operator ")
number_2=int(input("Enter a number "))

if select == '+':
    print(number_1,select,number_2,"=",add(number_1,number_2))
elif select == '-':
    print(number_1,select,number_2,"=",sub(number_1,number_2))
elif select == '/':
    print(number_1,select,number_2,"=",div(number_1,number_2))
elif select == '*':
    print(number_1,select,number_2,"=",mul(number_1,number_2))
else:
    print("INVALID OPERATOR")