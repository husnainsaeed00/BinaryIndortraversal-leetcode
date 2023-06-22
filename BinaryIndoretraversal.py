class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.inorderHelper(root, result)
        return result
    
    def inorderHelper(self, node, result):
        if node is None:
            return

        self.inorderHelper(node.left, result)
        result.append(node.val)
        self.inorderHelper(node.right, result)
