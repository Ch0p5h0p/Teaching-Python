'''
CLASSES
This covers how to create, modify, and instantiate classes
'''

# I don't know how to start this, so let's just jump right in with an example:

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def printColor(self):
        print(self.color)

    def returnBrand(self):
        return self.brand

    def __str__(self):
        return self.brand + ", " + self.color

Corolla = Car("Toyota", "Red")

Corolla.printColor()

corollaBrand = Corolla.returnBrand()

print(str(Corolla))

'''
Breakdown:

class Car : class definition

def __init__(self, brand, color) : the class constructor function
- self  : the variable that holds a reference to the object upon creation.
- brand : an argument
- color : another argument

def printColor(self) : a class method definition

def returnBrand(self) : another class method definition

def __str__(self) : a string cast handler
'''

'''
Classes have a lot of moving parts, so I'll try to simplify them:

Class: a blueprint for an object
Object: an instance of a class
Constructor: The constructor is a function that's called when a new instance of a class is created to make the object
Method: a function contained by a class

If we read the line "Corolla = Car("Toyota", "Red")", we can see that it passes two arguments while the constructor
requires three. The self parameter is automatically filled and, as previously stated, holds a reference to the object.

The self keyword is required in every method that's part of a class meant for instantiation.

If we look at the last method defined, we see that it's named "__str__". This is a special function. It's called
whenever something tries to cast the class as a string. If we look at the line "print(str(Corolla))", we can see
that we're doing exactly that (although using str() is redundant, as print() does that automatically). In order
to implement __str__() properly, you have to make it return a string (not print).

All of the casting functions previously mentioned are effectively ways to call __str__(), __int__(), __float__(), and 
others. This may flip your world upside down, but every "data type" is basically an object, and each implements the
relevant casting handlers. Aside from those, there are also ways to make a class iterable. I won't go into depth, but
it's worth the google.

There's also another method called a destructor that's used much less. This method is defined via __del__(). This
method is called under one of two circumstances:
1. Python wants to delete the object and reclaim the memory (when the object is either out of scope or no longer in use)
2. The user purposefully deletes it using the del keyword.

The del keyword is a pretty niche keyword, and many people suggest against using it unless you really know what you're
doing. The del keyword exists to forcibly remove an object from memory. If we wanted to delete Corolla, we'd simply
write:

del Corolla

And then it's gone from memory forever.

And that's about all for classes
'''