# Example of an infinite while loop bug
i = 1
while i <= 5:
    print(i)

# i never changes → infinite loop
# Fixed Version

i = 1
while i <= 5:
    print(i)
    i += 1
