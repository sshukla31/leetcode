'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''


from commons.binary_tree import Node



class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.add_nodes(root)  # pre-compute only left nodes of left sub-tree

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

            return node.data
        else:
            return None

    def add_nodes(self, root):
        while root:
            self.stack.append(root)
            root = root.left

class BSTIterator2(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.add_nodes(root)  # pre-compute every node

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
            return self.stack.pop().data
        else:
            return None

    def add_nodes(self, root):
        if root is not None:
            self.add_nodes(root.left)
            self.stack.append(root)
            self.add_nodes(root.right)

if __name__=='__main__':
    root  	     = Node(4);
    root.left        = Node(2);
    root.right       = Node(6);
    root.left.left   = Node(1);
    root.left.right  = Node(3);
    root.right.left  = Node(5);
    root.right.right = Node(7);

    # bti = BSTIterator(root)
    bti = BSTIterator2(root)

    while bti.hasNext():
        print bti.next()
