class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for (int num : nums){
            num = abs(num);
            if (nums[num] < 0)
                return num;
            nums[num] *= -1;
        }
        return -1;
    }
};
