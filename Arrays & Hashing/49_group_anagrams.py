# Problem Statement: https://leetcode.com/problems/group-anagrams/
# The function groups anagrams from a list of strings.
# An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
# using all the original letters exactly once.
# Input:
#   - strs: A list of strings.
# Output:
#   - A list of lists, where each sublist contains strings that are anagrams of each other.

# Time Complexity: O(n * k log k) - Where n is the number of strings and k is the average length of each string.
#   Sorting each string takes O(k log k), and we do this for all n strings.
# Space Complexity: O(n * k) - The dictionary stores all the strings, and each string can have up to k characters.
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for s in strs:
            key=tuple(sorted(s))
            dic[key].append(s)
        
        return list(dic.values())

if __name__ == "__main__":
    solution = Solution()

    # Example 1: Normal case
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input:", strs)
    print("Output:", solution.groupAnagrams(strs))
    # Expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    # Example 2: Single string
    strs = ["abc"]
    print("Input:", strs)
    print("Output:", solution.groupAnagrams(strs))
    # Expected: [["abc"]]

    # Example 3: Empty list
    strs = []
    print("Input:", strs)
    print("Output:", solution.groupAnagrams(strs))
    # Expected: []

    # Example 4: Strings with no anagrams
    strs = ["a", "b", "c"]
    print("Input:", strs)
    print("Output:", solution.groupAnagrams(strs))
    # Expected: [["a"], ["b"], ["c"]]