# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = None
        curr = head
        left_bridge = dummy
        itr = dummy
        while True:
            for _ in range(k):                       
                itr = itr.next
                if not itr:
                    return dummy.next
            right_bridge = itr.next
            prev = right_bridge
            curr = left_bridge.next
            lnext = curr
            for _ in range(k):
                next_curr = curr.next
                curr.next = prev
                prev = curr
                curr = next_curr

            itr = lnext
            left_bridge.next = prev
            left_bridge = lnext


            
            
