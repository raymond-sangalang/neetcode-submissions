# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        arm_node = head
        new_head = head
        while arm_node.next:
            
            # reference node to rotate to head
            rotate_node = arm_node.next

            if arm_node.next.next:
                # link arm to rotating node's next
                arm_node.next = rotate_node.next
                
                # move rotating node to head
                rotate_node.next = new_head
                new_head = rotate_node
            
            else:
                # move rotating node to head
                rotate_node.next = new_head
                new_head = rotate_node

                # end while loop
                arm_node.next = None
        return new_head