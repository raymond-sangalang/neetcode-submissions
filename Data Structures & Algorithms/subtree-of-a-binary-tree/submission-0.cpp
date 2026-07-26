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
    // Helper to check if given trees are equal
    bool isSubtree_helper(TreeNode* node1, TreeNode* node2) {

        // Cond: Both nodes are null then they are equal
        if (node1 == nullptr && node2 == nullptr)
            return true;

        // Cond: One node is null then not equal
        if (node1 == nullptr || node2 == nullptr)
            return false;

        // Check if values are equal and recursively check the child nodes
        return (node1->val == node2->val &&
                isSubtree_helper(node1->left, node2->left) &&
                isSubtree_helper(node1->right, node2->right));
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {

        // Cond: Empty subtree is true
        if (subRoot == nullptr)
            return true;

        // Cond: Searched tree empty but subtree not is not a subtree
        if (root == nullptr)
            return false;

        // Cond: Found a match at the current node
        if (isSubtree_helper(root, subRoot))
            return true;

        // Otherwise, search in left and right
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};
