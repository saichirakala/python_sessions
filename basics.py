import time
import datetime
print("the today's datetime is ",datetime.date.today())
#indentations
if 10 < 14:
#print("the high value")
#if we don't give the space after the condition it shows the indentation error
    print("the 10 is high")
# if we write the print statement in the same block it shows the same error
        #print("the value")
        #error:IndentationError: unexpected indent
#variables
print("enter the values of a,b:")
a=int(input())
b=int(input())
time.sleep(2)#this helps to give the output after 2sec.
print(a+b)
print(5+6)
#if we give the different values to the same variable the value should update automatically
#example
a=5
time.sleep(2)
print("the value of a before declaring in the code :",a)
a=7
time.sleep(2)#this helps to give the output after 2sec.
print(a)
Eid=1003 
print("Value is:",Eid)
print()
print("Address is:",id(Eid))
print()
time.sleep(2)
print("End of an Script")
