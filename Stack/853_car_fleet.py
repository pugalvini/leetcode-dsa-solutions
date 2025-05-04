# Problem Statement: https://leetcode.com/problems/car-fleet/
# The function calculates the number of car fleets that will arrive at the destination.
# A car fleet is a group of cars that travel together at the same speed.
# Input:
#   - target: The destination point.
#   - position: A list of starting positions of the cars.
#   - speed: A list of speeds of the cars.
# Output:
#   - The number of car fleets that will arrive at the destination.
# Time Complexity: O(n log n) - Sorting the cars by position takes O(n log n), and iterating through the cars is O(n).
# Space Complexity: O(n) - The stack and the cars list both take O(n) space.

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(cars)[::-1]:
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print("Input:", target, position, speed)
    print("Output:", solution.carFleet(target, position, speed))  # Expected: 3

    # Example 2: All cars at the same position
    target = 10
    position = [5, 5, 5]
    speed = [1, 2, 3]
    print("Input:", target, position, speed)
    print("Output:", solution.carFleet(target, position, speed))  # Expected: 1

    # Example 3: No cars
    target = 10
    position = []
    speed = []
    print("Input:", target, position, speed)
    print("Output:", solution.carFleet(target, position, speed))  # Expected: 0