import ctypes

# Load the shared library
lib = ctypes.CDLL('./libPyList.so')

# Define the argument types for the function
lib.print_python_list_info.argtypes = [ctypes.py_object]

# Define the list and call the function
l = ['hello', 'World']
lib.print_python_list_info(l)

# Modify the list and call the function again
del l[1]
lib.print_python_list_info(l)

# Extend the list and call the function
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(l)

# Clear the list and call the function
l = []
lib.print_python_list_info(l)

# Append elements to the list and call the function
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)

# Remove an element from the list and call the function
l.pop()
lib.print_python_list_info(l)
