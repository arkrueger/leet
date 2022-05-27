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
approach:
    notice that the inverted binary tree is a mirror image of the original
        -> swap right and left on all nodes
    recursive:
        accept node as input
            swap left and right
            recurse on right and left
            if input node is nullptr, return nullptr
            otherwise return input node

*/

class Solution {
 public:
  // recursive approach
  // Time: O(n) because the function is called once for each node
  // Space: O(1)
  TreeNode* invertTree(TreeNode* root) {
    // return early if input is nullptr
    if (!root) {
      return root;
    }

    // swap right and left
    TreeNode* swap = root->right;
    root->right = root->left;
    root->left = swap;

    // recurse on left and right
    invertTree(root->right);
    invertTree(root->left);

    // return root
    return root;
  }
};