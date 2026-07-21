# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get the middle of the linked list
        one_step = head
        two_step = head.next
        while two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next

        # Reverse the end half of the linked list
        end_node = one_step.next
        prev_node = one_step.next = None
        while end_node:
            temp_node = end_node.next 
            end_node.next = prev_node
            prev_node = end_node
            end_node = temp_node	

        # Merging the original start half and 
        #  the reversed end half 
        start_node, end_node = head, prev_node
        while end_node:
            temp_node1, temp_node2 = start_node.next, end_node.next
            start_node.next = end_node
            end_node.next = temp_node1
            start_node, end_node = temp_node1, temp_node2