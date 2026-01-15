#set methods
#union()/|: it will return the elements from both sets 
#intersection()/&: it will return the common elements 
#difference()/-: it will return the elements that are present in that set.
set1={1,2,3}
set2={3,4,5}
print(set1|set2)
print(set1&set2)
print(set2-set1)

#add(): add the elements to the set
#remove(): remove that element but if element is not there it will throw an error
#discard(): remove the element if element doesn't present it will not return any errors
#update():to add another list or set 

a={2,3,4}
b={5,6,7}
a.add(10)
print(a)
a.remove(4)
print(a)
a.update(b)
print(a)
