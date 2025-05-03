# Problem Statement: https://leetcode.com/problems/daily-temperatures/
# Time Complexity: O(n) - Each temperature is pushed and popped from the stack once.
# Space Complexity: O(n) - The stack can grow up to the size of the input in the worst case.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        This function calculates the number of days until a warmer temperature for each day.
        Input: A list of daily temperatures.
        Output: A list where each element represents the number of days until a warmer temperature.
        If no warmer temperature exists, the value is 0.
        """
        res = [0] * len(temperatures)  # Initialize result array with 0s
        stack = []  # Stack to store (temperature, index)

        for i, t in enumerate(temperatures):
            # Check if the current temperature is warmer than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  # Pop the top of the stack
                res[stackInd] = i - stackInd  # Calculate the difference in days
            stack.append((t, i))  # Push the current temperature and index onto the stack
        return res

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print("Input:", temperatures)
    print("Output:", solution.dailyTemperatures(temperatures))  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]

    # Example 2: Edge case with all decreasing temperatures
    temperatures = [80, 79, 78, 77]
    print("Input:", temperatures)
    print("Output:", solution.dailyTemperatures(temperatures))  # Expected: [0, 0, 0, 0]

    # Example 3: Edge case with all increasing temperatures
    temperatures = [60, 61, 62, 63]
    print("Input:", temperatures)
    print("Output:", solution.dailyTemperatures(temperatures))  # Expected: [1, 1, 1, 0]