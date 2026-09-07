/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

 /*
        1
    2       -1
  3   4

 */

class Solution {
public:

	void goodNodeHelper(TreeNode* nodePtr, int max_path, int& result) {

		if (!nodePtr)  return;
		
		if (nodePtr->val >= max_path) {
			max_path = nodePtr->val;
			result++;
		}
		goodNodeHelper(nodePtr->left, max_path, result);
		goodNodeHelper(nodePtr->right, max_path, result);
	}


    int goodNodes(TreeNode* root) {
    	int result = 0;
    	goodNodeHelper(root, root->val, result);

        return result;
    }
};
