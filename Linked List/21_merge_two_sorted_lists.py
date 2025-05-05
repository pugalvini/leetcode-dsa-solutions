# Problem Statement: https://leetcode.com/problems/merge-two-sorted-lists/
# The function merges two sorted singly linked lists into one sorted linked list.
# Input:
#   - list1: The head of the first sorted singly linked list.
#   - list2: The head of the second sorted singly linked list.
# Output:
#   - The head of the merged sorted singly linked list.

# Time Complexity: O(n + m) - Where n and m are the lengths of the two input lists.
# Space Complexity: O(1) - The merging is done in-place without using extra space.

        
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergeHead = None
        prev = None
        while list1 and list2:
            if list1.val < list2.val:
                node = ListNode(list1.val, None)
                list1 = list1.next
            else:
                node = ListNode(list2.val, None)
                list2 = list2.next
            if not prev:
                mergeHead = node
            else:
                prev.next = node
            prev = node
        if list1:
            if prev:
                prev.next = list1
            else:
                mergeHead = list1 
        if list2:
            if prev:
                prev.next = list2
            else:
                mergeHead = list2

        return mergeHead

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
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    print("Input:", linked_list_to_list(list1), linked_list_to_list(list2))
    merged_head = solution.mergeTwoLists(list1, list2)
    print("Output:", linked_list_to_list(merged_head))  # Expected: [1, 1, 2, 3, 4, 4]

    # Example 2: One list is empty
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    print("Input:", linked_list_to_list(list1), linked_list_to_list(list2))
    merged_head = solution.mergeTwoLists(list1, list2)
    print("Output:", linked_list_to_list(merged_head))  # Expected: [0]

    # Example 3: Both lists are empty
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    print("Input:", linked_list_to_list(list1), linked_list_to_list(list2))
    merged_head = solution.mergeTwoLists(list1, list2)
    print("Output:", linked_list_to_list(merged_head))  # Expected: []