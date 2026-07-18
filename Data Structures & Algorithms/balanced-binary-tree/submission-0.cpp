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
class Solution {
public:
 
    int getHeight(TreeNode* node_ptr) {
        if (node_ptr == NULL) return 0;
        
        int left_node = getHeight(node_ptr->left),
            right_node = getHeight(node_ptr->right);
        return max(left_node, right_node) + 1;
    }

    bool isBalanced(TreeNode* root) {
        if (root == NULL) return true;

        if (abs(getHeight(root->left) - getHeight(root->right)) > 1)
            return false;
        return isBalanced(root->left) && isBalanced(root->right);
    }
};