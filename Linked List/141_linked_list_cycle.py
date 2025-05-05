# Problem Statement: https://leetcode.com/problems/linked-list-cycle/
# The function determines if a singly linked list has a cycle.
# Input:
#   - head: The head of the singly linked list.
# Output:
#   - A boolean value indicating whether the linked list contains a cycle.

# Time Complexity: O(n) - Each node is visited at most once.
# Space Complexity: O(1) - The algorithm uses constant space.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
if __name__ == "__main__":
    # Helper function to create a linked list with a cycle
    def create_cyclic_linked_list(values, pos):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        cycle_node = None
        for i, val in enumerate(values[1:], 1):
            current.next = ListNode(val)
            current = current.next
            if i == pos:
                cycle_node = current
        if cycle_node:
            current.next = cycle_node
        return head

    # Helper function to create a linked list without a cycle
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    solution = Solution()

    # Example 1: Linked list with a cycle
    head = create_cyclic_linked_list([3, 2, 0, -4], 1)
    print("Has Cycle:", solution.hasCycle(head))  # Expected: True

    # Example 2: Linked list without a cycle
    head = create_linked_list([1, 2])
    print("Has Cycle:", solution.hasCycle(head))  # Expected: False

    # Example 3: Empty linked list
    head = create_linked_list([])
    print("Has Cycle:", solution.hasCycle(head))  # Expected: False

    # Example 4: Single node without a cycle
    head = create_linked_list([1])
    print("Has Cycle:", solution.hasCycle(head))  # Expected: False

    # Example 5: Single node with a cycle
    head = create_cyclic_linked_list([1], 0)
    print("Has Cycle:", solution.hasCycle(head))  # Expected: True