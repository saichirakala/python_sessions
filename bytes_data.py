import time 
list_one=[111,112,123,156,4]
obj1=bytes(list_one)
print(obj1)
print()
print(*obj1)
print()
for a in list_one:
    print(a)
print()
print(type(obj1))
print()
time.sleep(2)
print("End of an application ..")