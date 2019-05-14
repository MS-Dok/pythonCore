'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
'''
def count_positives_sum_negatives(arr):
    return([] if not arr else [len([y for y in arr if y>0]),sum([x for x in arr if x<0])])