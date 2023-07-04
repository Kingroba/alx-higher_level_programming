How to Utilize 0-add_integer.py
This module introduces a function called "add_integer(a, b=98)" that performs integer addition.

Usage
The function "add_integer(...)" returns the sum of its two arguments. When the arguments are numbers, the result is equivalent to using the "+" operator.

::
>>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(2, 3)
5
::

>>> add_integer(2, -3)
-1
The function also supports floating-point values.

::

>>> add_integer(2.0, 3.0)
5
Note that floats are converted to integers before the addition is executed.

::

>>> add_integer(2.9, 0.2)
2
::

>>> add_integer(-2.9, -0.2)
-2
It is possible to combine floating-point and non-floating point values.

::

>>> add_integer(2.3, -3)
-1
The second argument is optional; its default value is 98.

::

>>> add_integer(2)
100
Non-Numbers
The function "add_integer()" expects both arguments to be either integers or floats. If any of the arguments is neither an integer nor a float, a TypeError will be raised:

::

>>> add_integer("hello", 3)
Traceback (most recent call last):
TypeError: a must be an integer
::

>>> add_integer(2, "hello")
Traceback (most recent call last):
TypeError: b must be an integer
::

>>> add_integer(None)
Traceback (most recent call last):
TypeError: a must be an integer
::

>>> add_integer(2.3, None)
Traceback (most recent call last):
TypeError: b must be an integer
If both arguments are non-integers and non-floats, a TypeError message will only be displayed for the first argument.

::

>>> add_integer("hello", "there")
Traceback (most recent call last):
TypeError: a must be an integer
The function will fail if infinity is provided.

::

>>> add_integer(float('inf'))
Traceback (most recent call last):
OverflowError: cannot convert float infinity to integer
 
::

>>> add_integer(2, float('inf'))
Traceback (most recent call last):
OverflowError: cannot convert float infinity to integer
The same applies to NaN (Not a Number) values.

::

>>> add_integer(float('nan'))
Traceback (most recent call last):
ValueError: cannot convert float NaN to integer
::

>>> add_integer(2, float('nan'))
Traceback (most recent call last):
ValueError: cannot convert float NaN to integer
