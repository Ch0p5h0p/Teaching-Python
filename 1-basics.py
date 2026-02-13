'''
PYTHON BASICS
This will cover all the basics of Python programming
'''

# -- Defining Variables -- #

# Variables are defined regardless of type.
a = 2 #integer (int)
# or x=2. The spaces are for readability
b = "Hello" #string (str)
c = 5.2 #float
d = True #boolean (bool)

# You can reference a variable by simply typing its name
'''
The following operations between variables exist:
+ (add), - (subtract), * (multiply), / (divide), ** (power or exponentiation), and // (floor-divide)
Some operations that may need definitions are ** and //.

** is simply powers. For example, 3**2 is the same as three squared, or 9.
// is for division, rounded down to the nearest integer (never rounded up)

There are a few weird rules that sorta make sense for all operations:
1. If an operation is between any number type and includes a float type, the result will always be a float.
   This includes floor division. 5 // 2.0 returns 2.0, not 2 or 2.5.
2. Variable types have to be compatible, which we'll see below.

Compatibility:
String:
        +  : Works for concatenation (combining two strings), only works with other strings.
        *  : Repeats a string. For example, "Hello"*3 becomes "HelloHelloHello"
        -  : Not supported
        /  : Not supported
        ** : Not supported
        // : Not supported 
Integer, float:
        (Weird note: booleans are automatically converted to integers (True -> 1, False -> 0), so they're usable here.
        +  : Addition, both compatible with each other
        -  : Subtraction, both compatible with each other
        *  : Multiplication, both compatible with each other
        /  : Division, both compatible with each other
        ** : Exponentiation, both compatible with each other
        // : Floor division, both compatible with each other
List, dictionary, tuple:
        None compatible
        
Every operator has an assignment version as well, just put '=' after it.

The assignment version both does the operation and updates the variable, while the regular form doesn't.
For example: a += 1
Typically, it's shorthand for a = a + 1

For integers and floats, every operation does
'''


# In order to change the type of a variable (known as casting), you have the following functions:
str() # converts anything with letters to a string
int() # converts a string, float, or boolean to an integer
      # booleans convert to 0 or 1
      # floats are rounded down regardless
      # strings are attempted to be converted. Ex: "42" -> 42
float() # converts an integer to a float
bool() # converts a string or integer to a boolean
       # 0 becomes False, 1 becomes True
list() # covered later, converts an iterable object to a list
dict() # covered later, converts some iterable objects to dictionaries


# To define a function, you do the following:
def myFunction(parameter):
    pass

'''
Let's break it down:
"def": the keyword to define a function
"myFunction": the function name
"parameter": the value that will be passed into the function. The word "parameter" is a variable that holds
             the value you pass in as a variable
"pass": a placeholder for data, typically used when you don't know what you're going to put in something yet.
'''


# To call a function, you use the following:
myFunction(12) # Assumes that the parameter should be an integer. "parameter" holds the value 12 in the function.

# Functions typically have return statements, unless they're only for modifying data in-place.
def returningFunction(number):
    return number+1

numberPlusOne = returningFunction(5) # in this isnstance, returningFunction(5) reduces to 6, so numberPlusOne = 6


# There was another set of types I listed above, each defined by different kinds of brackets.
# We'll get into them here.

# A list is a grouping of values, and they don't have to be the same (though I don't know why you wouldn't make them so)
myList = ["a string", 1, 5.0, True]

# A tuple is an immutable list
myTuple = ("hello", 2)

# A dictionary is a mapping of keys to values
myDictionary = {"numberOne":1, "some_boolean":True, "A string": "hello", 0: "integer", 3.2: "float"}

# In order to get specific values from lists and tuples, you access them by their index.
# The first item is at index 0, not 1

myList[0] # returns "a string"
myList[2] # returns 5.0

myTuple[0] # returns "hello"
myTuple[1] # returns 2

# There's also something called list slicing, which is when you get a smaller portion of the list from the main list.
# You use this syntax: myList[start:end:step]. For example:
numbers=[0,1,2,3,4,5,6,7,8]
firstThreeEven = numbers[2:8:2] # returns [2, 4, 6]

# Lists and tuples are also indexable backwards. -1 corresponds to the last element of a list, -2 the second to last.
myList[-1] # returns True
myList[-2] # returns 5.0

# To get something from a dictionary, you use the key.
myDictionary["numberOne"] # returns 1
myDictionary["some_boolean"] # returns True
myDictionary[0] # returns "integer"
myDictionary[3.2] # returns "float"


# Lists have a few different functions related to them
len(myList) # returns the length of myList. Always one greater than the final index of the list
myList.insert(2, "hello") # inserts "hello" into myList at the index 2 (the third slot), pushing all following items up an index
myList.remove("hello") # removes the first occurrence of the word "hello" from myList
myList.pop() # removes and returns the item at the end of a list (can pop from other indices if supplied with an index)
myList.index(True, 0, len(myList)-1) # finds the index of True in the list between the bounds of the first and last index
myList.append("appended string") # appends "appended string" to the end of a list

# There's also this funky bit of code:
def addOne(number):
    return number+1

list(map(addOne, numbers))

'''
Let's break that down:
1. The map function applies the function addOne to every item in numbers, returning a map object (not a list)
2. list() casts the map object back to a list
'''

# Tuples share only len and index, as they're immutable.

# Dictionaries share len with lists as well as having the following functions to themselves:
myDictionary.keys() # returns all the keys in a dictionary as a dict_keys object which can be cast to a list.
myDictionary.values() # returns all the values in a dictionary as a dict_values object which can be cast to a list.

keys = ["greeting", "departure"]
values = ["hello", "goodbye"]
newDict = zip(keys, values) # creates a new dictionary and assigns newDict to it.

'''
Before we continue, a note on function parameters:

Python is a weird language. A very weird language. There's a rule it has called "pass-by-object-reference", which
basically means that when you call a function and pass in a variable as a parameter, the parameter that you pass in is 
actually a reference to the original variable (or object). This has some odd implications on data types, so I'll do my
best to explain.

Attempting to modify an immutable data type that was passed in as a variable results in a new instance of that variable
being created. For example, if you have the following function:

def increment(integer):
    integer+=1
    return integer
    
and you pass in a variable named "myInt" assigned to 1, the original instance of myInt won't be modified, but the
function will return the modified version of myInt.

By contrast, mutable data types will be directly changed.

Here's a reference for mutability:
Immutable:
    - string
    - int
    - bool
    - float
    - tuple
Mutable:
    - list
    - dictionary
'''

'''
I know you've been seeing these funky bits that start with three single-quotes and hashtags all along and wondering 
what they are, so I'll define them here for you.

They're called comments, and they're spaces where you can write whatever you want and it won't be executed.

Single-line comments start with #.

Multi-line comments start with either three single-quotes or three double-quotes. This is also the way to write a
multi-line string
'''

# Finally, I'll leave you with the following functions:
print("hello") # outputs "hello" to the console
response = input("How are you? ") # requests the user enter input into the console and stores it in "response".