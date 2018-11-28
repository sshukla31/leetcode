'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''



class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.add_nodes(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            node = self.stack.pop()
            self.add_nodes(node.right)

            return node.val
        else:
            return None

    def add_nodes(self, root):
        while root:
            self.stack.append(root)
            root = root.left

