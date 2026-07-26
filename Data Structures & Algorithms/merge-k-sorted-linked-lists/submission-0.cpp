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
struct Compare {
	// Min-heap: smaller node gets higher priority
    bool operator()(ListNode* node, ListNode* otherNode) {
        return node->val > otherNode->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {

    	// Min-heap storing the current smallest node from each list
    	priority_queue<ListNode*, vector<ListNode*>, Compare> p_queue;
    	
    	// Add the first node of each non-empty list
    	for (ListNode *list : lists) {
    		if(list) 
    			p_queue.push(list);
    	}
    	
    	// Cond: no nodes to merge
    	if (p_queue.empty()) 
    		return nullptr;

    	// Initialize the head of the merged list with the smallest node
    	ListNode *head = p_queue.top();
    	p_queue.pop();
    	
    	// Then, push the next node from the same list
    	if (head->next) 
    		p_queue.push(head->next);

    	head->next = nullptr;
    	ListNode *curr = head;

    	// Taking the smallest available node from priority queue
    	while (!p_queue.empty()) {
    		ListNode *node = p_queue.top();
    		p_queue.pop();

    		curr->next = node;
    		curr = node;
    		
    		// Add the next node from the node with current smallest value
    		if (node->next) 
    			p_queue.push(node->next);
    	}
    	return head;
    }
};