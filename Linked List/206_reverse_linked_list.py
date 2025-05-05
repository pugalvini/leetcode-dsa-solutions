
# Problem Statement: https://leetcode.com/problems/reverse-linked-list/
# The function reverses a singly linked list.
# Input:
#   - head: The head of the singly linked list.
# Output:
#   - The head of the reversed singly linked list.

# Time Complexity: O(n) - We traverse the linked list once to push nodes onto the stack and once to reverse the list.
# Space Complexity: O(n) - The stack stores all the nodes of the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        reversedHead = None
        node = head
        # Push all nodes onto the stack
        while node:
            stack.append(node)
            node = node.next
        prev = None
        # Pop nodes from the stack and reverse the list
        while stack:
            cur = stack.pop()
            cur.next = None
            if prev is None:
                reversedHead = cur
            else:
                prev.next = cur
            prev = cur
        return reversedHead
    
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert a linked list to a list
    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    solution = Solution()

    # Example 1: Normal case
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Input:", linked_list_to_list(head))
    reversed_head = solution.reverseList(head)
    print("Output:", linked_list_to_list(reversed_head))  # Expected: [5, 4, 3, 2, 1]

    # Example 2: Single node
    head = create_linked_list([1])
    print("Input:", linked_list_to_list(head))
    reversed_head = solution.reverseList(head)
    print("Output:", linked_list_to_list(reversed_head))  # Expected: [1]

    # Example 3: Empty list
    head = create_linked_list([])
    print("Input:", linked_list_to_list(head))
    reversed_head = solution.reverseList(head)
    print("Output:", linked_list_to_list(reversed_head))  # Expected: []