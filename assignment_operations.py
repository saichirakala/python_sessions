import time
print("the assignment operation :")
print()
a=eval(input("enter the a value for assignment operations:"))
b=eval(input("enter the b value for the assignment operation:"))
a=a+b
print("the value of a is :",a)
print()
a=a-b
print("the value of a when substracting is :",a)
print()
a=a/b
print("the value of a when dividing is:",a)
print()
time.sleep(3)
print("-----using the different method:------")
a**=b
print("the value of a is :",a)
print()
a//=b
print("the value of a is :",b)
print()
a=18
b=17
value=int(bin(a))
value1=int(bin(b))
print(value)
print(value1)
print(value+value1)
