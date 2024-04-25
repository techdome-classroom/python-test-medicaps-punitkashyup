from typing import List

def smallest_missing_positive_integer(nums: List[int]) -> int:
    """
    Find the smallest missing positive integer in the given list using cyclic sort.
    
    Args:
    - nums: An unsorted list of integers
    
    Returns:
    - The smallest missing positive integer
    """
    n = len(nums)
    i = 0
    while i < n:
        if 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
