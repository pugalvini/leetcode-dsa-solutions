# Problem Statement: https://leetcode.com/problems/top-k-frequent-elements/
# The function finds the `k` most frequent elements in an array.
# Input:
#   - nums: A list of integers.
#   - k: An integer representing the number of most frequent elements to return.
# Output:
#   - A list of `k` integers that are the most frequent elements in the array.

# Time Complexity: O(n log k) - Counting the frequency of elements takes O(n), and retrieving the top `k` elements
#   using `most_common` takes O(n log k) in the worst case.
# Space Complexity: O(n) - The dictionary stores the frequency of all elements in the array.

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        dict1=Counter()
        for num in nums:
            dict1[num]+=1
        for key, value in dict1.most_common(k):
            ans.append(key)
        return ans
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Normal case
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Input:", nums, k)
    print("Output:", solution.topKFrequent(nums, k))
    # Expected: [1, 2]

    # Example 2: Single element repeated
    nums = [1]
    k = 1
    print("Input:", nums, k)
    print("Output:", solution.topKFrequent(nums, k))
    # Expected: [1]

    # Example 3: All elements with the same frequency
    nums = [1, 2, 3, 4]
    k = 2
    print("Input:", nums, k)
    print("Output:", solution.topKFrequent(nums, k))
    # Expected: [1, 2] (or any two elements, as all have the same frequency)

    # Example 4: Empty array
    nums = []
    k = 0
    print("Input:", nums, k)
    print("Output:", solution.topKFrequent(nums, k))
    # Expected: []