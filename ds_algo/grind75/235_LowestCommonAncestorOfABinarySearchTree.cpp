/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

/*
approach:
    recursive:
        because it's a binary search tree, the left node is lower and right node is greater
        we can use this property to determine when we have reached the lowest common ancestor

        the lowest common ancestor has the property that one node (p or q) will be greater
            and the other node (p if q, q if p) will be lower
        if we see that both nodes are lower, then we recurse on the left child (return)
        if we see that both nodes are greater, then we recurse on the right child (return)
        if neither of the above were true (i.e. one node is greater and one is lower) then we
            return the current node

*/

class Solution {
 public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    TreeNode* c = root;  // "current" root node
    int valC;            // value at current root node
    int valP;            // value at p
    int valQ;            // value at q

    while (true) {
      valC = c->val;
      valP = p->val;
      valQ = q->val;

      // if both p and q are lower, recurse to the left
      if (valP < valC && valQ < valC) {
        return lowestCommonAncestor(c->left, p, q);
      }
      // if both p and q are greater, recurse to the right
      if (valP > valC && valQ > valC) {
        return lowestCommonAncestor(c->right, p, q);
      }

      // if we didn't return early above, return the current root node
      // i.e. current root value is between the values of p and q
      return c;
    }
  }
};