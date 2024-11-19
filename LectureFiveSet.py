collection={23,3,3,"hello_world","hello_world"}

print(collection)   #in-gnore duplicate items

print(len(collection))      # 3 -> ignore the duplicate items

emptySet = set()    #create empty
emptySet.add(24)
emptySet.add(2)
emptySet.add(2)
emptySet.add("shrasti")
emptySet.add((23,45))
# emptySet.add([23,45])       #unhashable type error -> set can not store mutable elements

emptySet.remove(2)
print(emptySet) # ignore duplicate

emptySet.clear()        # empty set

st={"hello","hello1", "world"}
print(st.pop())
print(st)   #remove random element

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))     #{1,2,3,4}

print(set1.intersection(set2))  #{2,3}

#you are a given a list of subjects for students. Assume one classroom is required for 1 subject.
#How many classrooms are neede by all students ?
subject={"python", "java", "c++", "python", "c++", "java", "c", "javascript"}
print(len(subject))

#Figure out a way to store 9 and 9.0 in set.
numberSet = {9,"9.0"}
print(numberSet)
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)