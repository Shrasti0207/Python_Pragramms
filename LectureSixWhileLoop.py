num = 1
while(num<=5):
    print("hello")
    num=num+1

#print numbers from 1 to 100
i = 1
while(i<=100):
    print(i)
    i+=1

#print numbers from 100 to -1
number = 100
while(number >= 1):
    print(number)
    number=number-1


#print the multiplication table of a number n 
tableNumber = int(input("Enter the number : "))
input = 1
while(input<=10):
    print(tableNumber, "x", input, "=", input * tableNumber)
    input+=1

list = [1,4,9,16,25,36,49,64,81,100]
index=0
while(index <= (len(list) - 1)):
    print(list[index])
    index+=1

tup = (1,4,9,16,25,36,49,64,81,100)
x = 36
ind = 0
while(ind<len(tup)):
    if(x == tup[ind]):
        print("find the number at index : ", ind)
        break
    ind+=1

j = 0
while(j<=10):
    if(j%2==0):
        j+=1
        continue #skip
    print(j)
    j+=1