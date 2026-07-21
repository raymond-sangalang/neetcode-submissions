/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Head of the result 
        ListNode* sumOfNodes = nullptr;

        // Pointer to build the result
        ListNode* curr_node;

        // Stores carry from the previous digit addition
        int carry = 0;

        // Process both lists while they still have nodes
        while (l1 != NULL && l2 != NULL) {

            // Create the head node of the result list
            if (sumOfNodes == NULL) {
                carry = (l1->val + l2->val) / 10;
                sumOfNodes = new ListNode((l1->val + l2->val) % 10);
                curr_node = sumOfNodes;
            }
            // Append remaining digits to the result list
            else {
                curr_node->next = new ListNode((l1->val + l2->val + carry) % 10);
                carry = (l1->val + l2->val + carry) / 10;
                curr_node = curr_node->next;
            }

            // Move to the next nodes
            l1 = l1->next;
            l2 = l2->next;
        }

        // Process remaining nodes in l1
        while (l1 != NULL) {
            curr_node->next = new ListNode((l1->val + carry) % 10);
            carry = (l1->val + carry) / 10;
            curr_node = curr_node->next;
            l1 = l1->next;
        }

        // Process remaining nodes in l2
        while (l2 != NULL) {
            curr_node->next = new ListNode((l2->val + carry) % 10);
            carry = (l2->val + carry) / 10;
            curr_node = curr_node->next;
            l2 = l2->next;
        }

        // If there is still a carry, create one final node
        if (carry != 0)
            curr_node->next = new ListNode(carry);

        return sumOfNodes;
    }
};
