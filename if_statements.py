import time 
print('-----if control statement------')
print()
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print()
if(a==7 and b==6):
    c=a*b
    print("the multiplication of a and b is: ",c) 
print()
#time.sleep("end of an if condition")
print()

print("-------if_else condition------")
value=input('enter the statement:')
if value=='session':
    print('Today we have a class at 9:00 am EST')
else:
    print("today we don't have a class")
print()
#time.sleep("end of if-else condition in different decleration")
print()


print("----if_elif_else condition------")
print()
key=input("enter the key value:")
door=input("enter the door number:")
print()
for key in range(10):
    print("the number of doors in this floor are",key)
print()
if key==door:       #if the key and door value is same.....
    print("the door is open....")
elif key<door:
    print("this key used to open the left_side doors....")
elif key>door:
    print("this key is used to open the right_side doors....")
else:
    print("this key does not match with any of the doors....")
    
