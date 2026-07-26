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

    ListNode* reverseLinkedList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = nullptr;

        while (curr != nullptr) {
            next = curr->next;  // Save next node
            curr->next = prev;  // Reverse the curr's pointer
            prev = curr;
            curr = next;
        }

        return prev;  // prev points to the new head node
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        queue<ListNode*> q;
        ListNode* headNode = nullptr;

        ListNode* nodePtr = head;
        ListNode* prevNode = nullptr;

        while (nodePtr) {

            // Check whether there are k nodes remaining
            ListNode* check = nodePtr;
            int count = 0;
            while (check && count < k) {
                check = check->next;
                count++;
            }

            // Less than k nodes remain
            if (count < k) {
                q.push(nodePtr);
                break;
            }

            q.push(nodePtr);

            // Move to the last node of this group
            prevNode = nodePtr;
            for (int i = 1; i < k; i++)
                prevNode = prevNode->next;

            nodePtr = prevNode->next;
            prevNode->next = nullptr;
        }

        //
        ListNode* trackNode = nullptr;

        while (!q.empty()) {

            ListNode* node = q.front();
            q.pop();

            // Reverse only complete groups
            int count = 0;
            ListNode* temp = node;
            while (temp) {
                count++;
                temp = temp->next;
            }

            if (!headNode) {
                if (count == k)
                    headNode = reverseLinkedList(node);
                else
                    headNode = node;

                trackNode = headNode;
            }
            else {
                if (count == k)
                    trackNode->next = reverseLinkedList(node);
                else
                    trackNode->next = node;

                trackNode = trackNode->next;
            }

            // Move trackNode to the end
            while (trackNode->next)
                trackNode = trackNode->next;
        
        }
        return headNode;
    }
};