#check if linkedlisr is palindrome
#algo
#step find the middle of linkedlist'
#using fast and slow pointer
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find middle (slow will stop at middle)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare both halves
        first, second = head, prev
        while second:  # only need to check till second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
