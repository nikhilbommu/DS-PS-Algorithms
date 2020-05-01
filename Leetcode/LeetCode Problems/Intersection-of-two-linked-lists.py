"""class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution():
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        in1,in2 = headA,headB
        while in1 != in2:
            if not in1:
                in1 = headB
            else:
                in1 = in1.next
            if not in2:
                in2 = headA
            else:
                in2 = in2.next
        return in1
