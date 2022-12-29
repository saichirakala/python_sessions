import time
a=5
b=7
def add():
    global c
    c= 10 
    d= 15
    print("the addition is : ",a+b+c+d)
def sub():
    print("the subtraction is : ",a-b-c)
if (__name__=="__main__"):
    add()
    print()
    sub()