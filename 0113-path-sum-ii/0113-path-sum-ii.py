# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(root, targetSum, path):
            if not root:
                return

            path.append(root.val)
            targetSum -= root.val

            if not root.left and not root.right:
                if targetSum == 0:
                    result.append(path[:])

            dfs(root.left, targetSum, path)
            dfs(root.right, targetSum, path)

            path.pop()

        dfs(root, targetSum, [])

        return result