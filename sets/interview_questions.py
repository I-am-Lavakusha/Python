#Set Interview Programs
#Given two lists, write a program that returns True if they have any common member

# l1 = [1, 2, 3, 4, 5]
# l2 = [5, 6, 7, 8, 9]

# set1 = set(l1)
# set2 = set(l2)

# common = set1.intersection(set2) #5
# print(common)

#You have two sets of User IDs. Find which users are in Set A but not in B, and which are in both.

# set_a = {"user1", "user2", "user3", "user4"}
# set_b = {"user3", "user4", "user5", "user6"}

# only_a = set_a - set_b
# print(f"Only in A: {only_a}") # {'user1', 'user2'}

# both = set_a & set_b
# print(f"In both: {both}")     
# {'user3', 'user4'}

#Write an efficient program to remove all vowels from a given string.
# text = "Python Programming is Fun"

# vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# result = ""
# for char in text:
#     if char not in vowels:
#         result += char #Pythn 

# print(result) 
# Output: Pythn Prgrmmng s Fn



#How do you check if one group of data is entirely contained within another?
group_a = {1, 2, 3, 7}
group_b = {1, 2, 3, 4, 5,7}

print(group_a.issubset(group_b))   
print(group_b.issuperset(group_a)) 