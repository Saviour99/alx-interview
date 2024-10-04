#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    if(n <= 0):
        return []
    else:
        pascal_val = [[1] * (row + 1) for row in range(n)]  # Create initial structure of 1's
        for row in range(2, n):
            for col in range(1, row):
                pascal_val[row][col] = pascal_val[row - 1][col - 1] + pascal_val[row - 1][col]
        return pascal_val
