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

*/

class Solution {
 public:
  bool isBalanced(TreeNode* root, int* height = nullptr) {
    // define right and left tree heights to be referenced in recursive calls
    int leftHeight = 0;
    int rightHeight = 0;

    // check if we are at a leaf node
    // if so, return true (this will help us establish height later on)
    if (root == nullptr) {
      return true;
    }

    // recurse to the right and left branches
    // this will allow us to mark if the branches are balanced within themselves(?)
    int leftBool = isBalanced(root->left, &leftHeight);
    int rightBool = isBalanced(root->right, &rightHeight);

    // keep track of the total (largest) height on this branch
    // it's important to set this *after* the recursive call
    // because the recursive call incremented this call's leftHeight and rightHeight
    if (height) {
      *height = max(leftHeight, rightHeight) + 1;
    }

    // if the current heights don't differ by > 1, return true only if both branches concur
    if (abs(leftHeight - rightHeight) < 2) {
      return leftBool && rightBool;
    }

    return false;
  }
};