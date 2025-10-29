'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
Nice — let’s do two clear, step-by-step examples so you can see exactly how the pointers move and why switching lists makes them meet.

Example 1 — Lists that intersect (Y-shape)

Shared tail: 4 → 5 (same nodes, same references)

List A: 1 → 2 → 3 → 4 → 5
List B:    9 → 4 → 5
           ↑
        (4 and 5 are the same nodes for both lists)


Initialize:

a = headA → node 1

b = headB → node 9

We iterate while a != b. At each step show (a, b).

Step 0 (start): (a=1, b=9)

Step 1: move both → (a=2, b=4)

a = a.next → 2

b = b.next → 4

Step 2: (a=3, b=5)

a = 3, b = 5

Step 3: (a=4, b=None)

a = a.next → 4

b = b.next → becomes None (end of B)

Step 4: b is None so we switch it to headA; a = a.next → 5

a = 5, b = headA = 1 → (a=5, b=1)

Step 5: (a=None, b=2)

a = a.next → None (end of A)

b = b.next → 2

Step 6: a is None so switch it to headB; b = 3 → (a=9, b=3)

a = headB = 9

b = b.next → 3

Step 7: (a=4, b=4)

a = a.next → 4

b = b.next → 4

Now a == b → intersection found at node 4

Why it met: after switchin
'''

class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        p1=head1
        p2=head2
        while p1!=p2:
            if p1 is None:
                p1=head2
            else:
                p1=p1.next
            if p2 is None:
                p2=head1
            else:
                p2=p2.next

        return p1
