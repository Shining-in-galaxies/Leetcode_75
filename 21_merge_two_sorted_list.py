# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a new linked list to hold nodes
        head = ListNode()
        # Start from the head of the new linked list
        current = head
        while list1 and list2: # This means: while list1 and list2 are both not null

            # Check which is the smaller node
            if list1.val < list2.val:
                # If the smaller one is from list1, current will point next at list1.
                current.next = list1
                # Then we should move the list1's pointer to the next
                list1 = list1.next
            else:
                current.next = list2
                # Then we should move the list2's pointer to the next
                list2 = list2.next
            
            # Advance current, to prepare for the next loop item
            current = current.next

        # Point to the list that is not null
        current.next = list1 or list2
        return head.next