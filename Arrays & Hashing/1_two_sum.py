# Problem Statement: https://leetcode.com/problems/two-sum/
# The function finds two numbers in the array that add up to a specific target.
# Input:
#   - nums: A list of integers.
#   - target: An integer representing the target sum.
# Output:
#   - A list of two indices of the numbers in the array that add up to the target.
#     The indices must be returned in any order.

# Time Complexity: O(n) - We iterate through the list once to populate the dictionary and once to find the solution.
# Space Complexity: O(n) - The dictionary stores up to n elements in the worst case.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx in range(len(nums)):
            num_map[nums[idx]] = idx
        print(num_map)
        for idx in range(len(nums)):
            s_value = target - nums[idx]
            if s_value in num_map and idx != num_map[s_value] :
                print(s_value, num_map)
                return [idx, num_map[s_value]]
            
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Normal case
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", nums, target)
    print("Output:", solution.twoSum(nums, target))  # Expected: [0, 1]

    # Example 2: Multiple pairs
    nums = [3, 2, 4]
    target = 6
    print("Input:", nums, target)
    print("Output:", solution.twoSum(nums, target))  # Expected: [1, 2]

    # Example 3: Negative numbers
    nums = [-3, 4, 3, 90]
    target = 0
    print("Input:", nums, target)
    print("Output:", solution.twoSum(nums, target))  # Expected: [0, 2]

    # Example 4: Single element (invalid case)
    nums = [1]
    target = 2
    print("Input:", nums, target)
    print("Output:", solution.twoSum(nums, target))  # Expected: None