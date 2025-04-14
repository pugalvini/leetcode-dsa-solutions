# Problem Statement: https://leetcode.com/problems/product-of-array-except-self/
# The function calculates the product of all elements in the array except the current element for each position.
# Input:
#   - nums: A list of integers.
# Output:
#   - A list of integers where each element is the product of all elements in the array except itself.

# Time Complexity: O(n) - We traverse the array twice (once forward and once backward).
# Space Complexity: O(1) - The output array `ans` is not considered extra space as it is part of the result.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        ans[0]=1
        for i in range(1,len(nums)):
            ans[i]= ans[i-1]*nums[i-1]
        mul=1
        for i in reversed(range(len(nums))):
            ans[i]*=mul
            mul*=nums[i]
        return ans
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Normal case
    nums = [1, 2, 3, 4]
    print("Input:", nums)
    print("Output:", solution.productExceptSelf(nums))
    # Expected: [24, 12, 8, 6]

    # Example 2: Contains zero
    nums = [0, 1, 2, 3]
    print("Input:", nums)
    print("Output:", solution.productExceptSelf(nums))
    # Expected: [6, 0, 0, 0]

    # Example 3: Single element
    nums = [5]
    print("Input:", nums)
    print("Output:", solution.productExceptSelf(nums))
    # Expected: [1]

    # Example 4: All elements are the same
    nums = [2, 2, 2, 2]
    print("Input:", nums)
    print("Output:", solution.productExceptSelf(nums))
    # Expected: [8, 8, 8, 8]