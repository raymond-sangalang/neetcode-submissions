/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* getRandomNode(Node* head, Node* newNode, Node* node_to_compare) {
        // check if a random pointer already exists in the list

        if (node_to_compare == NULL) return NULL;

        Node* curr_node = head;
        Node* new_curr = newNode;
        while(curr_node != NULL) {
            if (curr_node == node_to_compare)
                return new_curr;
            curr_node = curr_node->next;
            new_curr = new_curr->next;
        }
        return NULL;
    }


    Node* copyRandomList(Node* head) {

        if (head == NULL) return head;

        Node* new_head = nullptr;
        Node* write_cur;

        // 1. Copy all nodes from next pointers
        Node* read_cur = head;
        while(read_cur != NULL) {
            if (new_head == NULL) {
                new_head = new Node(read_cur->val);
                write_cur = new_head;
            }
            else {
                write_cur->next = new Node(read_cur->val);
                write_cur = write_cur->next;
            }
            read_cur = read_cur->next;
        }

        // Check randoms in original list
        read_cur = head;
        write_cur = new_head;
        Node* temp_rand;
        while (read_cur != NULL) {
            temp_rand = getRandomNode(head, new_head, read_cur->random);
            write_cur->random = temp_rand;

            read_cur = read_cur->next;
            write_cur = write_cur->next;
        }
        return new_head;
    }
};
