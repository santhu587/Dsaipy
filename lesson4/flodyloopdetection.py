'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

'''

curr=head
        
        list1=set()
        while curr:
            if curr not in list1:
                list1.add(curr)
            else:
                return True
            curr=curr.next
        return False
'''