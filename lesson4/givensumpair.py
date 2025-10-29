'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
'''
    head1:  head of linkedList 1
    head2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:  len of linkedList 1
    x:   given sum
'''
class Solution:
    def countPairs(self, head1, head2, x):
        # code here

        values = set()
        p2 = head2
        while p2:
            values.add(p2.data)
            p2 = p2.next

        # Step 2: Check for each element in list1
        count = 0
        p1 = head1
        while p1:
            if (x - p1.data) in values:
                count += 1
            p1 = p1.next

        return count


