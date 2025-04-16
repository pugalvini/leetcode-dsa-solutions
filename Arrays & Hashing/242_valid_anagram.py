# Problem Statement: https://leetcode.com/problems/valid-anagram/
# The function determines if two strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# using all the original letters exactly once.
# Input:
#   - s: The first string.
#   - t: The second string.
# Output:
#   - A boolean value indicating whether the two strings are anagrams.

# Time Complexity: O(n) - We iterate through both strings once, where n is the length of the longer string.
# Space Complexity: O(1) - The dictionaries store at most 26 keys (for lowercase English letters).

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s={}
        dic_t={}
        for char in s:
            dic_s[char] = dic_s.get(char,0)+1
        for char in t:
            dic_t[char] = dic_t.get(char,0)+1
        return dic_t == dic_s
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Valid anagram
    s = "anagram"
    t = "nagaram"
    print("Input:", s, t)
    print("Output:", solution.isAnagram(s, t))  # Expected: True

    # Example 2: Not an anagram
    s = "rat"
    t = "car"
    print("Input:", s, t)
    print("Output:", solution.isAnagram(s, t))  # Expected: False

    # Example 3: Empty strings
    s = ""
    t = ""
    print("Input:", s, t)
    print("Output:", solution.isAnagram(s, t))  # Expected: True

    # Example 4: Different lengths
    s = "a"
    t = "ab"
    print("Input:", s, t)
    print("Output:", solution.isAnagram(s, t))  # Expected: False