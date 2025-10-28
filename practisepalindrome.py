class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def isPalindrome(self, head):
        # code here
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        nxt=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        #compare halves
        first=head
        second=prev
        while second:
            if first.data!=second.data:
                return False
            first=first.next
            second=second.next
        return True

