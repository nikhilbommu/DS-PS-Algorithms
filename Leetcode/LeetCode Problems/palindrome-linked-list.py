# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#checking whether is a linkedlist is palindrome or not using 2pointer approach
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        slow = head
        fast = head
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        firsthalf = head
        secondhalf = self.reverseList(slow.next)
        while (firsthalf and secondhalf):
            if firsthalf.val != secondhalf.val:
                return False
            firsthalf = firsthalf.next
            secondhalf = secondhalf.next
        return True

    def reverseList(self, head):
        temphead = None
        while (head):
            next = head.next
            head.next = temphead
            temphead = head
            head = next
        return temphead