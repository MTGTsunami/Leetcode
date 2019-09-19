"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = {root: None}
        nodes = set()
        nodes.add(root)
        findP, findQ = False, False
        depth = 0

        while not findP or not findQ:
            newnodes = set()
            depth += 1
            for node in nodes:
                if node == p:
                    findP = True
                    depthP = depth
                elif node == q:
                    findQ = True
                    depthQ = depth

                if node.left:
                    d[node.left] = node
                    newnodes.add(node.left)
                if node.right:
                    d[node.right] = node
                    newnodes.add(node.right)
            nodes = newnodes

        if depthP > depthQ:  # p is always higher than q
            p, q = q, p
            depthP, depthQ = depthQ, depthP

        while p != q:
            if depthP < depthQ:
                q = d[q]
                depthQ -= 1
            else:
                q = d[q]
                p = d[p]
        return p






