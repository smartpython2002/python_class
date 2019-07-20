
OUT_OF_BOUNDS = float('-inf')
# print(OUT_OF_BOUNDS)

def calculate(first_number, second_number, operator):
    result = 0
    if operator == "+":
        result = (first_number + second_number)
    elif operator == "-":
        result = (first_number - second_number)
    elif operator == "*":
        result = (first_number * second_number)
    elif operator == "/":   
        result = (first_number / second_number)
    else:
        result = OUT_OF_BOUNDS
    return result

# print (calculate(1,2, '+'))

# set a boolean to true to continue asking for input 
more_input = True

first_number = input("What is the first number? ")
first_number =int(first_number) 

second_number = input("What is the second number?")
second_number = int(second_number)

operator = input("What operation do you wnat me to do (+, -, *, /)? ")

 
result = calculate(first_number, second_number, operator)

if result == OUT_OF_BOUNDS:
    print("you need valid operator(+, -, *, /)?")
else:
    print (result)

if input("Another calculation (y/n)? ") == "y":
    more_input = True
else:
    more_input = False

#more_input = True if input("Another calculation (y/n)?")== 'y' else False

print ("Bye now")