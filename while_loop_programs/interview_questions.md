# Note: First try to answer these questions and then if you can't than refer the answers.

1.	What is a while loop in Python?
2.	What is the syntax of a while loop?
3.	Is the while loop entry-controlled or exit-controlled?
4.	Can a while loop execute zero times? Explain.
5.	What is the difference between a while loop and a for loop in Python?
6.	Does Python support a do-while loop?
7.	What is an infinite while loop?
8.	How can you stop a while loop in Python?
9.	What happens if the loop condition is always false?
10.	What is a loop variable?
11.	What are the three important parts of a while loop?
12.	What is a nested while loop?
13.	What are common mistakes made while using while loops?
14.	Can break and continue be used in a while loop?
15.	When should you prefer a while loop?


# Practical / Programming Questions

16. [Write a program to print numbers from 1 to N using a while loop](1_to_n_numbers.py)

17. [Print even numbers from 1 to 100 using a while loop](even.py)

18. [Print odd numbers from 1 to 50 using a while loop](odd.py)

19. [Find the sum of first N natural numbers](sum.py)

20. [Reverse a given number using a while loop](number_reverse.py)

21. [Count the number of digits in a number](count_digits.py)

22. [Check whether a number is a palindrome](number_palindrome.py)

23. [Find the factorial of a number using a while loop](factorial.py)

24. [Print the Fibonacci series using a while loop](fibonacci.py)

25. Find the GCD of two numbers using a while loop.

26. Write a program to keep taking input until the user enters 0.

27. Write a menu-driven program using a while loop.

28. Demonstrate the use of continue in a while loop.

29. Predict the output of a given while loop.

30. Give an example of an infinite while loop bug.

Practical / Programming Question


## Answers:

1. What is a while loop in Python?
A while loop repeats a block of code as long as a given condition is True.

2. What is the syntax of a while loop?
while condition:
    #statements


3. Is the while loop entry-controlled or exit-controlled?
It is an entry-controlled loop, because the condition is checked before execution.

4. Can a while loop execute zero times?
Yes. If the condition is False initially, the loop body will not execute.

5. Difference between while loop and for loop in Python?
while loop	                   for loop
Condition-based	               Sequence-based
Manual update	                 Automatic iteration
Used when iterations unknown	 Used when iterations known

6. Does Python support a do-while loop?
No. Python does not have a built-in do-while loop.

7. What is an infinite while loop?
A loop that runs forever because its condition is always True.
while True:
    pass

8. How can you stop a while loop?
By:
•	Making the condition False
•	Using break

9. What happens if the condition is always False?
The loop body will never execute.

10. What is a loop variable?
A variable that controls the number of loop iterations.

11. What are the three important parts of a while loop?
1.	Initialization
2.	Condition
3.	Update (increment/decrement)

12. What is a nested while loop?
A while loop inside another while loop.

13. Common mistakes in while loops?
•	Missing update statement
•	Infinite loop
•	Wrong condition
•	Indentation errors

14. Can break and continue be used?
Yes.
•	break exits the loop
•	continue skips the current iteration

15. When should you prefer a while loop?
When the number of iterations is not known in advance.
