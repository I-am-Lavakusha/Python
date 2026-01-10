#without list comprehension
# squares=[]
# for i in range(1, 11):
#   squares.append(i*i)
# print(squares)

#with list comprehension
# squares2=[i*i for i in range(1,11)]
# print(squares2)

# syntax : [expresion for item in iterable]

#without using list comprehension
# list1=[1,2,3,4]
# res=[]
# for i in range(len(list1)):
#   res.append(list1[i]*list1[i])
# print(res)

#with using list comprehension
# res1=[k*k for k in list1]
# print(res1)

#without using list comprehension
# res=[]
# for i in range(1, 11):
#   if i%2==0:
#     res.append(i)
# print(res)

#using list comprehension
# res1=[i for i in range(1,11) if i%2==0]
# print(res1)

#without using comprehenstion
# string="rosso"
# res=[]
# for i in string:
#   res.append(i)
# print(res)

#using comprehension
# name='rosso'
# res1=[i for i in name]
# print(res1)
