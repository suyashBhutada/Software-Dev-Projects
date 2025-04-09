# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temphead = ListNode(-1, head)
        len = 0
        val_at_k = -1
        val_at_kth_fromback = -1
        while head:
            len += 1
            if len == k:
                val_at_k = head.val
            head = head.next
        kth_index_from_back = len-k + 1
        head = temphead.next
        while kth_index_from_back:
            if((kth_index_from_back -1) == 0):
                val_at_kth_fromback = head.val
                break
            head = head.next
            kth_index_from_back -= 1
        counter = 1
        head = temphead.next
        while(head):
            if(counter == k):
                head.val = val_at_kth_fromback
            if(counter == (len-k + 1)):
                head.val = val_at_k
            counter += 1
            head =head.next
        return temphead.next



        
        