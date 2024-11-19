print("Hello World", "world is gorgeous")
print(23)
print(23+25)

name = "Shrasti Gupta"
age = 24
price = 26.99
print("My name is : ", name)
print(age,price)


print(type(name))
print(type(age))
print(type(price))

old=False
a = None
print(old)
print(a)

number1=21
number2=5  
sum=number1+number2
print("sum of two numbers : ",sum)

#Arithmethic operator
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 % number2)   #finding the remainder
print(number1 ** number2)  #a^b


#Relational Operators
print(number1 == number2)
print(number1 != number2)
print(number1 > number2)
print(number1 < number2)
print(number1 >= number2)   
print(number1 <= number2)  

#Assignment operator
num = 30
num+=10  # num=num+10

print("number is :",num)

#Logical Operator
print(not False)
print(not (number1 > number2))

val1 = True
val2 = False
val3 = True

print(val1 and val3)
print(val1 and val2)
print(val1 or val2)


print((number1>number2) and (number1==number2))
print((number1>number2) or (number1==number2))


#Type Conversion

a = 2
b = 4.25
c = int("2")
#type conversion
print(a + b) #automatically convert the data type into float
#Type casting
print(b + c) # manually we are converting the string value into integer


# Input from user
studentName = input("enter your name :")
studentAge = int(input("enter your age : "))
studentMarks = float(input("enter your marks : "))

print(studentName)
print(studentMarks)
print(studentAge)


#print area of square
side = float(input("enter the side of the square : "))
area = side * side
print("area of the square : ", area)
