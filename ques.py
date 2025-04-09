from math import gcd
from collections import Counter

# Example Test Case
arr = [5, 10, 20, 10, 15, 5]
k = 2
from itertools import combinations


def gcd_two_numbers(a, b):
    """Calculates the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def gcd_of_array(numbers):
    """Calculates the Greatest Common Divisor (GCD) of an array of numbers."""
    if not numbers:
        raise ValueError("Input array cannot be empty.")
    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd_two_numbers(result, numbers[i])
    return result
def brute_force(arr, k):
    n = len(arr)
    res = float("inf")
    fin_res = float("inf")
    for change_positions in combinations(range(n), k):  # Pick k elements to change
        this_res_gcd = float("inf")
        this_res_len = 0
        modified_subarray = arr[:]
        for idx in change_positions:
            modified_subarray[idx] = 1  # Change to 2 (since 2 is the smallest number > 1)
        
        for i in range(0, n+1):  # Try all subarray lengths from 1 to n
            for j in range(i,n+1):  # Generate all subarrays of length L
                subarray = modified_subarray[i:j]
                if subarray and gcd_of_array(subarray) > 1:
                    this_res_len = max(this_res_len,len(subarray))
        
        fin_res = min(fin_res,this_res_len)
    return fin_res



print(brute_force(arr, k))  # Expected Output: 2



