# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return list1
        elif list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1

        mergeList = None
        curr_node = None

        head1 = list1
        head2 = list2

        while head1 is not None or head2 is not None:

            if mergeList is None:
                if head1.val < head2.val:
                    mergeList = head1
                    head1 = head1.next
                else:
                    mergeList = head2
                    head2 = head2.next

                curr_node = mergeList

            if head1 is None:
                curr_node.next = head2
                head2 = head2.next
               

            elif head2 is None:
                curr_node.next = head1
                head1 = head1.next
              

            else:
                # Both list still have elements
                # so compare
                if head1.val < head2.val:
                    curr_node.next = head1
                    head1 = head1.next
                else:
                    curr_node.next = head2
                    head2 = head2.next

            curr_node = curr_node.next

        return mergeList