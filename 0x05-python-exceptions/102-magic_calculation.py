#!/usr/bin/python3

def perform_magic_calculation(x, y):
    final_result = 0
    for index in range(1, 3):
        try:
            if index > x:
                raise Exception('Exceeded limit')
            else:
                final_result += x ** y / index
        except:
            final_result = y + x
            break
    return final_result

# Test the perform_magic_calculation function
a = 2
b = 3
result = perform_magic_calculation(a, b)
print("The magic calculation result is:", result)

