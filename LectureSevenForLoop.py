nums = [1,2,3,4,5]

for val in nums:
    print(val)

#sum of the numbers in list
sum=0
for val in nums:
    sum = sum + val
print(sum)

#print the tuples elements
tup = ("cucumber", "carrot")
for val in tup:
    print(val)

#for loop with else
#print the each chracter in string
name = "Gauranshi"
for char in name:
    print(char)
else:
    print("END")            #else does not work in case of break

#WAP to write a program for search a element
tup = (1,4,9,16,25,36,49,64,81,100)
index = 0
number = 9 
for el in tup:
    if(number == el):
        print("number found at " ,index)
        index+=1
        break
    else:
        print("Not found")
        index+=1

# Wap to find the factorial of first n number
num = int(input("Enter any number:"))
fact = 1
for i in range(1,num):
    fact = fact * i
    print(fact)