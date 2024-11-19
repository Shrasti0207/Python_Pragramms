paragraph = "My name is Shrasti Gupta.\nMy age is 23"
print(paragraph)

str1 = "shrasti"
str2 = "Gupta"
print(str1 + " " +str2)
print(len(str1 + " " +str2))

#indexing
print(str1[3])

#slicing
print(str1[1:4]) #hra
print(str1[:4])  #shra  (take from 0 index)
print(str1[1:]) #hrasti  (take from 1 to len(str1))

#Negative slicing
print(str1[-5:-1])  #rast

#string functions
print(str1.endswith("i"))  #return true or false
print(str1.capitalize())       #capitalize the first character
print(str1.replace("s", "g"))   #replacethe substring or character
print(str1.find("t"))  #return index
print(str1.find("q"))   #return -1 does not exist
print(str1.count("s"))      #count the substring or character


#WAP to input user's first name and print its length
userFirstName = input("Enter your name : ")
print("length of the user name : ", len(userFirstName))


#WAP to find the occurences of '$' in a string
sentence = "My name is Shrasti $ and my surname is $"
print("occurence of the $ : ", sentence.count("$"))

