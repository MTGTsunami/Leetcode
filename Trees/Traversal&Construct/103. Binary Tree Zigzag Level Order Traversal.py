"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if root is None:
            return levels

        def helper(nodes, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(nodes.val)

            nextLevel = level + 1
            if nodes.left:
                helper(nodes.left, nextLevel)
            if nodes.right:
                helper(nodes.right, nextLevel)

        helper(root, 0)
        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i] = levels[i][::-1]
        return levels