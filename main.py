class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head):
        # Code here
        prev = None
        curr = head
        
        while curr:
            nextptr = curr.next   # 1️⃣ Save next node
            curr.next = prev      # 2️⃣ Reverse the pointer
            prev = curr           # 3️⃣ Move prev to current
            curr = nextptr        # 4️⃣ Move to next node
        
        return prev