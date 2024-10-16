def advance_calculator():
    x=int(input("Enter your first number: "))
    y=int(input("Enter your second number: "))
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

    while True:
        print("Hit 1=Addition")
        print("Hit 2=Subtraction")
        print("Hit 3=Multiplication")
        print("Hit 4=Division")
        print("Hit 5 and exit the operation")
        calc=int(input())

        if calc==1:
            print(add(6,9))
        elif calc==2:
            print(subtract(11,5))
        elif calc==3:
            print(multiply(5,50))
        elif calc==4:
            print(divide(45/9))
        elif calc==5:
            print("Exiting the operation")
            break