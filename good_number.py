"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""

def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    for item in nums:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    
    ans = reduce(lambda x, value: x + value*(value - 1) // 2, d.values(), 0)
    return ans

numIdenticalPairs([1, 1, 2, 4, 2, 2, 1])