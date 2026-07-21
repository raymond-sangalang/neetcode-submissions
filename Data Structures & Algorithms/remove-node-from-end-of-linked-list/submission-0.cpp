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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == NULL) return NULL;

        ListNode* tail = head;
        ListNode* n_front = head;
        int count = n;

        while (count-- > 0 && n_front != NULL) 
            n_front = n_front->next;
        
        // Then move both pointers at the same pace until the end of the 
        // linked list path
        while (n_front != NULL && n_front->next != NULL){
            tail = tail->next;
            n_front = n_front->next;
        }

        // at this point, tail pointer is the node before the node for removal.
        if (tail == head && tail->next == NULL) 
            head = head->next;
        else if (n_front == NULL) {
            // check the distance from tail
            ListNode* curr_node = tail;
          
            int steps = 0;
            while(curr_node->next != NULL){
                curr_node = curr_node->next;
                steps++;
            }
          
            if (n-steps == 1)
                head = head->next;
        }
        else if (tail->next != NULL){
            n_front = tail->next;
            tail->next = n_front->next;
        } 
        return head;
    }
};
