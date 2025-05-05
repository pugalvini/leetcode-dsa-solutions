# Problem Statement: https://leetcode.com/problems/reorder-list/
# The function reorders a singly linked list such that the nodes are rearranged in the following order:
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
# Input:
#   - head: The head of the singly linked list.
# Output:
#   - The linked list is modified in-place, so no return value is needed.

# Time Complexity: O(n) - The list is traversed multiple times (finding the middle, reversing, and merging).
# Space Complexity: O(1) - The reordering is done in-place without using extra space.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reversedSecondHead = self.reverseList(slow.next)
        slow.next = None
        self.mergeTwoLists(head, reversedSecondHead)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseHead = None
        def reverse(node):
            nonlocal reverseHead
            if node:
                prev = reverse(node.next)
                if prev:
                    prev.next = node
                else:
                    reverseHead = node
                node.next = None
            return node
        reverse(head)
        return reverseHead
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            if temp1:
                list2.next = temp1

            list1 = temp1
            list2 = temp2

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
    head = create_linked_list([1, 2, 3, 4])
    print("Input:", linked_list_to_list(head))
    solution.reorderList(head)
    print("Output:", linked_list_to_list(head))  # Expected: [1, 4, 2, 3]

    # Example 2: Odd number of nodes
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Input:", linked_list_to_list(head))
    solution.reorderList(head)
    print("Output:", linked_list_to_list(head))  # Expected: [1, 5, 2, 4, 3]

    # Example 3: Single node
    head = create_linked_list([1])
    print("Input:", linked_list_to_list(head))
    solution.reorderList(head)
    print("Output:", linked_list_to_list(head))  # Expected: [1]

    # Example 4: Empty list
    head = create_linked_list([])
    print("Input:", linked_list_to_list(head))
    solution.reorderList(head)
    print("Output:", linked_list_to_list(head))  # Expected: []