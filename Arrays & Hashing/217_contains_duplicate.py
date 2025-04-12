# Problem Statement: https://leetcode.com/problems/contains-duplicate/
# The function determines if a given integer array contains any duplicates.
# Input:
#   - nums: A list of integers.
# Output:
#   - A boolean value indicating whether any value appears at least twice in the array.

# Time Complexity: O(n) - We iterate through the list once, and dictionary operations (insert and lookup) are O(1).
# Space Complexity: O(n) - The dictionary stores up to n elements in the worst case.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        for num in nums:
            if num in num_map:
                return True
            else:
                num_map[num] = 1
        return False
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Contains duplicates
    nums = [1, 2, 3, 1]
    print("Input:", nums)
    print("Output:", solution.containsDuplicate(nums))  # Expected: True

    # Example 2: No duplicates
    nums = [1, 2, 3, 4]
    print("Input:", nums)
    print("Output:", solution.containsDuplicate(nums))  # Expected: False

    # Example 3: Single element
    nums = [1]
    print("Input:", nums)
    print("Output:", solution.containsDuplicate(nums))  # Expected: False

    # Example 4: Empty list
    nums = []
    print("Input:", nums)
    print("Output:", solution.containsDuplicate(nums))  # Expected: False