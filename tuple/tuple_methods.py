#methods in tuple
#count(): it will the number of times an element present
#index(): it will return the index or the position of the element

tuple1=(1,2,3,4,5,6,7,7,7,8,8)
print(tuple1.count(7)) #3
print(tuple1.index(8)) #9


#packing
student="lava", "kumar", 3, "cse", "75%"
print(type(student))

#unpacking
first_name, last_name, year, branch, percentage=student
print(first_name)
print(last_name)
print(year)
print(branch)
print(percentage)
