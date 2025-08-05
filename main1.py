print("This is a Programme of a simple Calculator model created by Coder-Abhay14")
while True:
    try:
        a = int(input("Enter the first number : "))
        e = input("Enter the arithematic operation (+, -, *, /, %, , ^, =) : ")
        b = int(input("Enter the second number : "))
        break
    except ValueError:
        print("Invalid Input \n Please enter an integer ")
def operations(a, e, b):
    if (e == "="):
        if (a == b):
            print (f"Both the numbers {a} and {b} are equal , {a}={b}") 
        else: 
            print(f"Both the numbers {a} and {b} are not equal , {a}≠{b}")
    elif (e == "+"):
        print (f"The sum of both numbers is : {a} + {b} = {a+b}")
    elif (e == "-"):
        print (f"The difference between the numbers is : {a} - {b} = {a-b}")
    elif (e == "*"):
        print (f"The product of numbers is : {a} * {b} = {a*b}")
    elif (e == "/"):
        if (b == 0):
            print("Error: Division by zero")
        else:
                print(f"The quotient of the numbers is : {a} / {b} = {a/b}")
    elif (e == "%"):
        print(f"The Remainder when {a} is divided by {b} is : {a%b}")
    elif (e == "^"):
        print(f"The number {a} raised to its exponential value {b} is : {a**b}")
    else: 
        print("Inavlid operation ")

operations(a,e,b)


print("Thanks for your support!")