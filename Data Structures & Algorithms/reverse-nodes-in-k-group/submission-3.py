# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left_group = dummy
        def reverse(head, last):
            prev = None
            curr = head 
            while curr != last:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return head, prev

        while True:
            kth = left_group
            for _ in range(k):
                kth = kth.next
                if not kth: return dummy.next
            
            next_group = kth.next
            l,r = reverse(left_group.next, next_group)
            left_group.next = r
            l.next = next_group
            left_group = l
        