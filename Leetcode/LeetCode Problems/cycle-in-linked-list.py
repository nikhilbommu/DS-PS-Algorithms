class Solution:
    def hasCycle(head):
        slow = head
        fast = head
        if not head:
            return False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
