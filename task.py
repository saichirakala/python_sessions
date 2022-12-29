import time
n=input("enter the string:")
str2=''
for x in n:
    print("the string is ",x)
    str2=x+str2
y=" "
for y in str2:
    print("the reverse string is ",y)
print()
if x==y:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
print()