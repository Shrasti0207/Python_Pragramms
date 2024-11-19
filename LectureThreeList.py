# userDetails = ["Shrasti", 23, 23455, 34.89]
# print(userDetails)
# print(type(userDetails))


# userDetails[0] = "Gauranshi"
# print(userDetails)   #list are mutable

# userDetails.append("Gauri")     #insert at the end
# print(userDetails)

# marks=[84,54, 97.12]
# marks.sort()      #sort in ascending order
# print(marks)

# marks.sort(reverse = True)
# print(marks)        #sort in descendng order

# marks.reverse()
# print(marks)    #reverse original list

# marks.insert(2,67)
# print(marks)            #insert at particular index

# marks.remove(67)        #remove the partcular element
# print(marks)

# marks.pop(2)            #remove the element at particular index
# print(marks)


# #WAP to ask the user    to enter the names of their 3 favourite movies and store them in a list
# movie1 = input("Enter first movie name : ")
# movie2 = input("Enter second movie name : ")
# movie3 = input("Enter third movie name : ")

# listOfMovies = [movie1, movie2, movie3]
# print(listOfMovies)

list = [1,2,3,2,6]
copyList = list.copy()
copyList.reverse()
if(list == copyList):
    print("palindrome list")
else:
    print("not")