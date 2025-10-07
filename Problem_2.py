'''
25 Reverse Nodes in K-group
https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?

Solution:
1. We go through the list and whenever we find a group of k nodes, we reverse them. We keep a dummy node before the head and update start to track the node before the group. Each group is reversed by reconnecting its pointers, and we repeat until the list ends.
https://youtu.be/R1MN07ZWZ9I?t=216
Time: O(N), Space: O(1)
'''
from typing import Optional
from linked_list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    ''' T: O(N), S: O(1) '''
    def reverse(begin, end):
        prev = None
        curr = first = begin.next
        fast = curr.next
        while fast != end:
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next
        curr.next = prev

        begin.next = curr
        first.next = end
        return first

    if not head or k == 0:
        return head

    dummy = ListNode(-1)
    dummy.next = head

    curr = head
    begin = dummy
    count = 0
    while curr:
        count += 1
        if count % k == 0:
            begin = reverse(begin, curr.next)
            curr = begin
        curr = curr.next
    return dummy.next

def run_reverseKGroup():
    tests = [([1,2,3,4,5], 2, [2,1,4,3,5]),
             ([1,2,3,4,5], 3, [3,2,1,4,5]),
    ]
    for test in tests:
        head, k, ans = test[0], test[1], test[2]
        sll = build_linked_list(head)
        print(f"\nSLL = {sll.to_array()}")
        print(f"k = {k}")
        rev_sll = reverseKGroup(sll, k)
        print(f"Reversed K-Nodes SLL = {rev_sll.to_array()}")
        success = (ans == rev_sll.to_array())
        print(f"Pass: {success}")
        if not success:
            print("Failed")
            return

run_reverseKGroup()