#!/bin/python3

import math
import os
import random
import re
import sys



def gradingStudents(grades):
    # Write your code here
    res=[]
    for i in grades:
        if (i>=38):
            rem=i%5
            if(rem>=3):
                i+=(5-rem)
        res.append(i)
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

