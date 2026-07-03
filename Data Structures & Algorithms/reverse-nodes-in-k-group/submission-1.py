# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        Lbridge = dummy
        def reverse(head, last):
            left = head
            prev = last
            curr = head
            while curr != last:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return left, prev
        
        while True:
            kth = Lbridge
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            next_group = kth.next
            l,r = reverse(Lbridge.next,next_group)
            Lbridge.next = r
            Lbridge = l
        
