# Program Name:     fibonacci.py
# Author:           Rafaela Lomboy
# Date:             23.12.2019 (original), 4.1.2020 (edit)
# Purpose:          This program calculates the nth value of the Fibonacci sequence, then
#                   displays the time taken to calculate the value.
# Update:           (4.1.2020) added documentation (and this header!)

import time

cache = {} # saves values already calculated for faster runtime

def fibonacci(n):
    """Function computes nth number in the Fibonacci sequence recursively.
       This one improves upon a previous design by utilizing cache from the
       dictionary data type, improving computational speed for larger n values.
    """

    global cache
    
    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    cache[n] = result
    return result

#main

for i in range(0, 101, 5):
    start = time.time()
    result = fibonacci(i)
    end = time.time()
    duration = end - start
    print("fibonacci(" + str(i) + "):", result, ",", duration)
