# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def listToInt(self, lst: Optional[ListNode]) -> int:
        r, d = 0, 1
        while lst:
            r += lst.val * d
            d *= 10
            lst = lst.next
        return r

    def intToList(self, num: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        for digit in str(num)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = self.listToInt(l1)
        d2 = self.listToInt(l2)
        s = d1 + d2

        return self.intToList(s)
