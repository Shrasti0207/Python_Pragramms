for el in range(10):      #range(stop condition)
    print(el)

for el in range(1,10):       #range(start, stop)
    print(el)

for el in range(1,10,2):        #(start, stop, step size)
    print(el)

#print sum of even numbers from 2 to 10
sum = 0
for i in range(2,10,2):
    sum+=i
print(sum)

#print multiplication table of a number n

number = int(input("Enter any number : "))
for i in range(1,11):
    print(number * i)

#pass keyword -> null statement that does nothing
for i in range(5):
    pass
print("some work")


