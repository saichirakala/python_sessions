def Add():
    number1=float(input("enter the value : "))
    number2=float(input("enter the next value : "))
    return number1+number2
def sub():
    number1=float(input("enter the value : "))
    number2=float(input("enter the next value : "))
    return number1-number2
def mul():
    number1=float(input("enter the value : "))
    number2=float(input("enter the next value : "))
    return number1*number2
def div():
    number1=float(input("enter the value : "))
    number2=float(input("enter the next value : "))
    return number1/number2
def fdiv():
    number1=float(input("enter the value : "))
    number2=float(input("enter the next value : "))
    return number1//number2
if(__name__=="__main__"):
    while True:
        print()
        print()
        operation = input("1.Addition\n2. subtraction\n3. Multiplication\n4. Division\n5. Floor Division\n6. Exit\nEnter the required operation : ")
        print()
        if operation == '1':
            print("the addition of two numbers :",Add())
        elif operation == '2':
            print("the substration of two numbers :",sub())
        elif operation == '3':
            print("the multiplication of two numbers :",mul())
        elif operation == '4':
            print("the division of two numbers :",div())
        elif operation == '5':
            print("the Floor Division of two numbers :",fdiv())
            
        elif operation == '6':
            break
        else:
            print("Enter the correct operation")
    
    