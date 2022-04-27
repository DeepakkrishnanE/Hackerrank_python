Between Two Sets
------------------

Soluiton 1|| Brute force
------------------------


#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    # Write your code here
    multiple_a = []
    factors_b = []
    total_length = len(a+b)
    final_factors = []
    
    for i in range(1,101):
        for num_a in a:
            if i % num_a ==0:
                multiple_a.append(i)
        for num_b in b:
            if num_b % i ==0:
                factors_b.append(i)
        totalFactors = multiple_a + factors_b
        
    for num in totalFactors:
        if totalFactors.count(num) == total_length:
            final_factors.append(num)
    
    return(len(set(final_factors)))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

