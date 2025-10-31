class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def union(self, head1, head2):
        # code here
        elements = set()

        # Traverse first linked list
        current = head1
        while current:
            elements.add(current.data)
            current = current.next

        # Traverse second linked list
        current1 = head2
        while current1:
            elements.add(current1.data)
            current1 = current1.next

        # Sort the unique elements
        sorted_values = sorted(elements)

        # Create a new linked list for the union
        dummy = Node(0)
        temp = dummy

        for val in sorted_values:
            temp.next = Node(val)
            temp = temp.next

        return dummy.next
