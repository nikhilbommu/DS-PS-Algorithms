# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        if not odd:
            return head
        even = head.next
        if not even:
            return head
        evenHead = head.next
        while even.next:
            odd.next = even.next
            odd = odd.next
            if odd.next:
                even.next = odd.next
                even = even.next
            else:
                break
        odd.next = evenHead
        even.next = None
        return head

