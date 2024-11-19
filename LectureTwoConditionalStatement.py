age = int(input("Enter your age : "))
if(age >= 18):
    print("user can give the vote")
elif(age <= 18 and age >=15):
    print("user can make voter id")
else:
    print("user can not make voter id and give vote")


marks = int(input("Enter your marks : "))
if(marks>=90):
    print("the Grade is A")
elif(marks<90 and marks >=80):
    print("the Grade is B")
elif(marks<80 and marks >=70):
    print("the Grade is C")
else:
    print("the Grade is D")
