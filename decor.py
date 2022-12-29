import time
def Test_register_case2(func):
    def inner(fname,lname,username,p1,p2):
        if username=="sai_chirakala":
            print("user name is already existed")
        else:
            Test_register_case1(fname,lname,username,p1,p2)
    return inner
        
@Test_register_case2
def Test_register_case1(fname,lname,username,p1,p2):
    print("-----New user information-----")
    print("first name is ",fname)
    print("last name is ",lname)
    print("username name is ",username)
    print("password name is ",p1)
    print("confirm password name is ",p2)
    print("-----------------")
if __name__=="__main__":
    Test_register_case1("sai","chirakala","sai_chirakala","krishna","krishna")
    print()
    Test_register_case1("krishna","goud","Krishna_chirakala","chirakala","chirakala")
print()
time.sleep(2)
print("end of an application......")