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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);

        if (!root)
            return result;
        
        while (!q.empty()) {
            vector<int> level_nodes;
            int num_nodes = q.size();
            for (int i = 0; i < num_nodes; i++) {
                TreeNode* nodePtr = q.front();
                q.pop();

                if (nodePtr->left)
                    q.push(nodePtr->left);
                if (nodePtr->right)
                    q.push(nodePtr->right);
                level_nodes.push_back(nodePtr->val);
            }
            result.push_back(level_nodes);
        }
        return result; 
    }
};
