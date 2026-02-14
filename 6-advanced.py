'''
ADVANCED
This is the fun stuff >:D
'''

'''
Alright, I'm going to drop all pretenses of seriousness here. The stuff I'm about to teach is:
1. Cool
2. Potentially explosive if done wrong
3. Fun

So let's jump in :D
'''

'''
Let's start with something easy: format strings (or f-strings)

An f-string is simply a string that can automatically insert and concatenate values instead of having to worry about
writing + to concatenate.
'''

# Here's an example of an f-string

age = 30
name = "Bob"
string = f"My name is {name} and I'm {age} years old"
print(string)

# You can also directly make the string in a print statement or function
print(f"My name is {name} and I'm {age} years old")

# Simple as that.

# Next are inline if statements. They're also very simple.

A = 3
B = "Even" if A%2 == 0 else "Odd"
# This sets B to "Even" if A is even or "Odd" if it's not.

'''
Next is something fun: list comprehensions.

List comprehensions are basically concise ways of generating lists. They incorporate a for loop and an inline if 
statement into the generation process.

Here's an example:
'''

squared_evens = [i**2 for i in range(20) if i%2 == 0]
'''
Breakdown:

i           : the iteration variable
i**2        : the value we're putting into the finished list (in this instance, it's i squared
range(20)   : a range of numbers 0 (inclusive) to 20 (exclusive).
if i%2 == 0 : only add to the list if i is even.


Note: in math, it would be helpful for you to learn parenthetical inclusivity notation. Square brackets are inclusive, 
parenthesis are exclusive. For example, in range(20), we would say [0, 20), because we include 0 and exclude 20.
'''


# Another fun thing is dictionary comprehensions. Here are two examples:

cubed_evens = {i : i**3 for i in range(10) if i%2 == 0} # fully generative

fruit = ["apple", "banana", "orange"]
cost = [2.00, 1.50 , 2.75]
fruit_costs = {k: v for k, v in zip(fruit, cost)} # list combiner

'''
Alright, we've had fun with our lists, but it's time to move on.

If you're anything like me, you HATE how lax Python is with types. Luckily, Python has a way to at least annotate the
types, if not fail because of bad typing.

Let's do one now.
'''

def add(a:int, b:int) -> int:
    return a+b

# We can annotate argument/parameter types with argument:type and return types with def function() -> type
# As shown below, we can annotate variables the same way.
a:int = 0

'''
Next, let's tackle an important part of program safety: error handling.

There are VERY many Python error types, and they're all in a hierarchy. You should google them on your own time though,
because I'm not explaining them here :P

To do handling, you use a try/catch statement.
'''

try:
    print(1)
except Exception as e: # "Exception" is basically any sort of error.
    raise e # You can also print the exception if you don't want the program to crash.

'''
Another fun part of making functions is the arguments. Sure, we can define functions the NORMAL way, but why do that?

By the way, you'll probably hear me use arguments and parameters interchangeably.

We have three concepts here:
defaulted arguments : arguments that have a default value when they're not provided
*args               : a set of variable length arguments
**kwargs            : a set of arguments that have associated keys, like a dictionary.

Examples of all are provided below
'''

def print_a_string(string="hello"):
    print(string)

print_a_string("abcdefg")
print_a_string()

# If you provide a string, the string argument becomes what you passed it. If you don't pass anything in, it
# becoems "hello"

def print_lots(*args):
    for arg in args:
        print(arg)

print_lots("Hello", "world", "I'm", "printing", "stuff")
# It takes in as many arguments as you want to pass in, then prints them.

def print_person(**kwargs):
    print(f"I am {kwargs['name']}, and I'm {kwargs['age']} years old")

print_person(name="bob", age=30)

'''
Next is bitwise operations. Here's a refresher for the bitwise operators, which are similar to the symbolic logic
operators, as well as some more:
    &  : and
    ~  : not
    |  : or
    ^  : xor
    >> : shift right
    << : shift left
    
Only >> and << have assignment versions (>>= and <<=)

>> and << operate specifically on binary. Here are examples of each being used:

00110000 >> 3 = 00000110
00000110 << 4 = 01100000

Right shift is considered destructive, because you're shrinking the number. Left shift isn't because you can recover the
original number very easily.

Also: right shift is a very easy way to divide a number by two, and left shift is great for multiplying by two.
'''

'''
Next are lambda functions. Lambdas are basically very quick ways of writing functions.

Lambdas are very useful in things like map statements as they mean you don't have to define a whole function. They can
be assigned to names, though, if you really want to.

Lambda syntax is fairly simple:

lambda <arguments> : <operation>

The operation also functions as a return. Think of lambdas the same way you think about mathematical functions: no
programming function behavior (unless you use inline if statements).
'''

# Assigning a lambda to a variable and calling it
square = lambda x:x**2
square(4) # returns 16

# Using a lambda on a map
numbers = [i for i in range(10)]
cubed = list(map(lambda x:x**3, numbers)) # results in [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

'''
Next is one of the most dangerous things you can use: recursion.

Recursion is when a function calls itself. Simple as that. Here's an example:
'''

# Recursive countdown
def countdown(start):
    print(start)
    countdown(start-1) if start > 0 else None

