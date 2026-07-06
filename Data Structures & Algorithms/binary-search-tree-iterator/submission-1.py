# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if self.hasNext():
            res = self.stack.pop()
            if res.right:
                node = res.right
                while node:
                    self.stack.append(node)
                    node = node.left
            return res.val
        return -1


    def hasNext(self) -> bool:
        return True if len(self.stack) != 0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()