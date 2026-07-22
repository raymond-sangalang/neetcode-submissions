class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // Initialize both pointers at the first element
        int slow = nums[0];
        int fast = nums[0];

        // Detect the cycle using Floyd's Tortoise and Hare algorithm
        while (true) {
            // Move slow pointer one step and
            // move fast pointer two steps
            slow = nums[slow];
            fast = nums[nums[fast]];

            // Break when a cycle is detected, where both pointers meet
            if (fast == slow) break;
        }


        // Find the entrance to the cycle or the duplicate number
        int ptr1 = nums[0];
        int ptr2 = slow;

        // Move both pointers one step at a time until they meet at the duplicate
        while (ptr1 != ptr2) {
            ptr1 = nums[ptr1];
            ptr2 = nums[ptr2];
        }

        return ptr1;
    }
};
