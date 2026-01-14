# String Questions (Only Questions)

## First try to answer yourself and then refer the answers for validation

1. What is a string in programming?

2. How do you find the length of a string?

3. How do you reverse a string?

4. How do you check if a string is a palindrome?

5. How do you count the number of vowels in a string?

6. How do you convert a string to uppercase and lowercase?

7. How do you check if two strings are equal?

8. How do you find the frequency of each character in a string?

9. How do you remove spaces from a string?

10. How do you find the number of words in a string?


# String Programming Questions (Only Questions)

1. Write a program to reverse a given string.

2. Write a program to check whether a string is a palindrome.

3. Write a program to count vowels, consonants, digits, and spaces in a string.

4. Write a program to find the frequency of characters in a string.

5. Write a program to remove duplicate characters from a string.

6. Write a program to find the first non-repeating character in a string.

7. Write a program to count the number of words in a string.

8. Write a program to check if two strings are anagrams.

9. Write a program to replace all vowels with * in a string.

10. Write a program to find the longest word in a sentence.

## questions and answers

1. What is a string in programming?

A string is a sequence of characters enclosed in quotes.
Example: "hello", "Java123"

2. How do you find the length of a string?

The length is the total number of characters in the string.

Example (Python):
s = "hello"
print(len(s))  

## Output: 5

3. How do you reverse a string?

You reverse a string by changing the order of characters from last to first.

Example (Python):

s = "hello"
print(s[::-1])  # Output: olleh

4. How do you check if a string is a palindrome?

A string is a palindrome if it reads the same forward and backward.

Example (Python):

s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

5. How do you count the number of vowels in a string?

Check each character and count vowels (a, e, i, o, u).

Example (Python):

s = "hello"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)  # Output: 2

6. How do you convert a string to uppercase and lowercase?

Example (Python):

s = "Hello"
print(s.upper())  # HELLO
print(s.lower())  # hello

7. How do you check if two strings are equal?

Use the equality operator.

Example (Python):

s1 = "abc"
s2 = "abc"

if s1 == s2:
    print("Equal")
else:
    print("Not Equal")

8. How do you find the frequency of each character in a string?

Example (Python):

s = "hello"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


Output:

{'h':1, 'e':1, 'l':2, 'o':1}

9. How do you remove spaces from a string?

Example (Python):

s = "hello world"
print(s.replace(" ", ""))  

## helloworld

10. How do you find the number of words in a string?

Example (Python):

s = "I love programming"
words = s.split()
print(len(words))  

## Output: 3

