#Interview questions

#reverse a tuple
original = (10, 20, 30, 40, 50)
# print(tuple(reversed(original)))

# Slicing: [start:stop:step]
# reversed_tuple = original[::-1]
# print(original)
# print(reversed_tuple)






#Convert a List of Tuples into a Dictionary

# data = [("name", "John"), ("age", 25), ("city", "NY")]
# result_dict = dict(data)
# print(result_dict) 
#Output: {'name': 'John', 'age': 25, 'city': 'NY'}


#Find Duplicate Items in a Tuple


# my_tuple = (1, 2, 3, 2, 4, 5, 1, 1)
# duplicates = [] #[1,2]
# print(set(my_tuple))
# for item in my_tuple:
#                         #2>1
#      if my_tuple.count(item) > 1:
#          if item not in duplicates:
#              duplicates.append(item)

# print(tuple(duplicates)) 
# Output: (1, 2)




#Can you add an element to a tuple?" 

# No, tuples are immutable. However, you can concatenate two tuples using the + operator to create a new tuple."

t1 = (1, 2, 3)
t2 = (4,) 
t3 = t1 + t2
print(t3) # (1, 2, 3, 4)