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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        queue<TreeNode*> q;
        
        if (!root)
            return result;
        
        q.push(root);

        while (!q.empty()) {
            TreeNode* rightNode;
            int num_nodes = q.size();

            for (int i = 0; i < num_nodes; i++) {
                TreeNode* nodePtr = q.front();
                q.pop();

                if (nodePtr){
                    rightNode = nodePtr;
                    if (nodePtr->left)
                        q.push(nodePtr->left);
                    if (nodePtr->right)
                        q.push(nodePtr->right);
                }
            }
            if (rightNode) {
                result.push_back(rightNode->val);
            }
        }
        return result; 
    }
};
