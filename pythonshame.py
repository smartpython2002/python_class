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
        result = -1
    return result



first_number = input("What is the first number? ")
first_number =int(first_number) 

second_number = input("What is the second number?")
second_number = int(second_number)

operator = input("What operation do you wnat me to do (+, -, *, /)? ")

 
result = calculate(first_number, second_number, operator)

if result == -1:
    print("you need valid operator(+, -, *, /)?")
else:
    print (result)
