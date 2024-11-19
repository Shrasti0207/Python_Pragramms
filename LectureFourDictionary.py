information={
    "name": "shrasti",
    "age": 23,
    "isadult" : True,
    "marks": [23,56,87],
    23: "gauri"
}
print(information)
print(type(information))

print(information["name"])
print(information[23])

information["name"]="gauranshi"
information["surname"] = "gupta"
print(information)


student={
    "name": "rahul kumar",
    "subject_marks" : {
        "phy": 98,
        "math": 87,
    }
}
print(student)
print(student["subject_marks"]["phy"])

print(information.keys())   
print(student.keys())       #print Outer keys

print(list(student.keys()))     #typecasting

print(information.items())      #give the pair in the form of tuple

# print(information["name2"])     #give error and not executed the forward code.

print(information.get("name2"))     #no error  -> None

new_dict = {
    "city": "Noida"
}
information.update(new_dict)        #update the previous dictionary, If we put same key it overright the value
print(information)

#store following word meaning in a python dictionary
wordDict={
    "table": ("a piece of dictionary", "list of facts and figures"),        #or we can store in list
    "cat": "a samll animal"
}
print(wordDict)

# WAP to enter marks of 3 subjects from the user and store them in a dictionarty. Start with am empty dictionary & add one by one.
marks_dict = {}
marks_dict["chem"] = int(input("enter chem marks : "))
marks_dict["phy"] = int(input("enter chem phy : "))
marks_dict["math"] = int(input("enter chem math : "))
print(marks_dict)

