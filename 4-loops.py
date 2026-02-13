'''
LOOPS
This covers how to write loops
'''

# There are two kinds of loops: a for loop and a while loop.

# A for loop is simple:
for i in range(10):
    print(i)

'''
Breakdown:

for   : the for loop keyword
i     : the iteration value. Above, it holds a number between 0 and 9.
range : a function that specifies a range of numbers to use.

The range function is very similar to list slicing. Its full use looks like this:

range(start, stop, step)

and it generates a list of numbers from start (inclusive) to stop (exclusive), incrementing by step. For instance:

range(10, 20, 2)

would generate 10, 12, 14, 16, 18.

for loops are also used on iterables.
'''

for letter in "hello":
    print(letter)

for number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(number)

# The other kind of loop is a while loop

a = 0
b = 10

while a < b:
    a+=1
    print(a)

'''
Breakdown:

while : the while loop keyword
a < b : condition

A while loop simply executes the body as long as the provided condition is true.
You can create an infinite loop by just providing True as the condition.
'''

'''
There are two relevant keywords to be used in loops:
break    : discards the rest of the current iteration and breaks out of the loop
continue : discards the rest of the current iteration and starts the next 
'''

# A use of "break"
counter = 0
while True:
    counter += 1
    print(counter)
    if counter == 10:
        break

# I can't actually think of a use of continue off of the top of my head