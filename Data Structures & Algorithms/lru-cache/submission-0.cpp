// Node for the doubly linked list
struct Node {
	int key;
	int value;
	Node *next;
	Node *prev;

	Node(int key, int value) {
		this->key = key;
		this->value = value;
		next = nullptr;
		prev = nullptr;
	}
};


class LRUCache {
public:

	int capacity;
	unordered_map<int, Node *> cacheMap;
	Node *head;
	Node *tail;
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }
    
    // Get the value for the specified key
    int get(int key) {

    	if (cacheMap.find(key) == cacheMap.end())
    		return -1;

    	Node *node = cacheMap[key];
    	// Update the most recently used within the list
    	remove(node);
    	add(node);
    	return node->value;
        
    }
    
    // Put Key-value pair into the cache
    void put(int key, int value) {

    	if (cacheMap.find(key) != cacheMap.end()) {
    		Node *oldNode = cacheMap[key];
    		remove(oldNode);
    		delete oldNode;
    	}

    	Node *newNode = new Node(key, value);
    	cacheMap[key] = newNode;
    	add(newNode);

    	// Check if we maxed out the size of the cache capacity
    	if (cacheMap.size() > capacity) {
    		Node *nodeToRemove = tail->prev;
    		remove(nodeToRemove);
    		cacheMap.erase(nodeToRemove->key);
    		delete nodeToRemove;
    	}
        
    }

    // Add a node right after the head - most recently used position
    void add(Node *node) {
    	Node *nextNode = head->next;
    	head->next = node;
    	node->prev = head;
    	node->next = nextNode;
    	nextNode->prev = node;
    }

    // Remove a node from the list
    void remove(Node *node) {
    	Node *prevNode = node->prev;
    	Node *nextNode = node->next;
    	prevNode->next = nextNode;
    	nextNode->prev = prevNode;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */