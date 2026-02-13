'''
CONTROL STRUCTURES
This covers how to use structures to control execution
'''

'''
Before we begin, there are some operators you need to learn that make control structures work. All of them evaluate to
a boolean value.

Comparison operators:
    A == B : is A the same as B? (note: different than using the assignment equals, "=")
    A != B : is A not equal to B?
    A > B  : is A greater than B?
    A >= B : is A greater than or equal to B?
    A < B  : is A less than B?
    A <= B : is A less than or equal to B?
    
Logical operators:
    A and B : are both A and B true?
    not A   : negates A. If A is true, then A becomes false.
    A or B  : is either A or B true?
    A xor B : is either A or B true (but not both)?

Symbolic logical operators:
    & : and
    ! : not
    | : or
    ^ : xor

Other operators:
    A is B : basically and alias for "=="
    A in B : does B contain A? (used for iterables)
'''

# Let's set up an if/else statement:
A = True
B = False

if (A == B):
    print("A is the same as B")
else:
    print("A isn't the same as B")

# In the above example, "A isn't the same as B" is printed to the console.

# How about an if/elif/else statement?
# An if/elif/else statement has as many elifs as you want, and only one will get selected, prioritizing the first.
# Let's set one up now:
A = True
B = True
C = False

if (A==B):
    print("1")
elif (B==C):
    print("2")
elif (B==C):
    print("3")
else:
    print("4")

'''
Let's trace the path.

If A equals B, we print "1" and stop.
If A doesn't equal B...
    If B equals C, we print "2" and stop
    Otherwise, we print "4" and stop
    
We'll never print "3", because the chain prioritizes the first hit condition
'''

'''
There's one more control structure to know: match/case.

The match/case structure is essentially an upgraded if/elif/else structure.
Match takes in a value, and then there are a series of cases that check if they match the value.
'''

num = 5
match num%2:
    case (0):
        print("Even")

    case (1):
        print("Odd")

# You can also use logical operators:
letter = "a"
match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")

# "case _" functions like an "else"