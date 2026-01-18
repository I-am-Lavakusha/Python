#this is the program that will check whether the program is palindrome or not
#it uses the concept of slicing
#it can be done by using the two pointer approach also

s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
