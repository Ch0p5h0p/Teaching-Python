'''
USING LIBRARIES
This covers how to import and use libraries
'''

# In order to import a library, you use "import"

import numpy

# This allows you to use functions from the numpy library (NumPy is a good library for math. SciPy is also good)
# If you're in an IDE and see a red line, that's probably because you don't have NumPy installed.
'''
Windows: pip install numpy
Linux and maybe Mac: pipx install numpy
'''

# You can also import only specific functions, variables, and classes from libraries. For example:
from numpy import pi, power, ndarray

# pi: a constant containing pi
# power: a function that exponentiates numbers, power(3,2) = 3**2
# ndarray: an N-dimensional array class

# all of these are accessible without the library. You can just type pi or power(3, 2)
# You can access these all if you just import numpy through numpy.pi, numpy.power(), numpy.ndarray, etc.

# finally, you can assign an alias to an imported library like so:
import scipy as sp

# this means that instead of having to type scipy for every time you want to access something, you can just type sp.