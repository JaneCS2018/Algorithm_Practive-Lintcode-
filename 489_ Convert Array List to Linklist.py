"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: nums: an integer array
    @return: the first node of linked list
    """
    def toLinkedList(self, nums):
        # write your code here
        p, head = None, None
        for num in nums:
            if head is None:
               head = ListNode(num)
               p=head
            else:
               p.next = ListNode(num)
               p = p.next
        return head
