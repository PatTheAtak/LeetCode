class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Dummy node for the merged list
        current = dummy     # Pointer to the current node of the merged list
        ptr1 = list1        # Pointer to the current node of list1
        ptr2 = list2        # Pointer to the current node of list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next

        # Append the remaining nodes of list1 or list2
        if ptr1:
            current.next = ptr1
        else:
            current.next = ptr2

        return dummy.next  # Return the actual head of the merged list
