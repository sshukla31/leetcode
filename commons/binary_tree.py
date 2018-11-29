'''
Binary Tree implementation
'''

class Node(object):
    """ Define node creation methods """
    def __init__(self, data):
        """ Intialize new node """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    """ Define methods to insert node and print nodes in pre, post and in order """

    def __init__(self):
        """ Initialize root """
        self.root = None
        self.curr_node = None
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.sibling = None

    def insert(self, value):
        """ Insert node in the tree """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while(node!=None):
                if(value <= node.data):
                    if node.left is None:
                        node.left = new_node
                        node = node.left
                    node = node.left
                elif(value > node.data):
                    if node.right is None:
                        node.right = new_node
                        node = node.right
                    node = node.right


    def record_meta_data(self, value):
        found = False
        node = self.root
        while(node != None and found == False):
            if(value == node.data):
                found = True
                if self.root == node:
                    self.parent = None
                    self.left_child = None if node.left is None else node.left.data
                    self.right_child = None if node.right is None else node.right.data
                else:
                    if node.data == getattr(self.parent.right, 'data', None):
                        self.sibling = getattr(self.parent.left, 'data', None)
                    else:
                        self.sibling = getattr(self.parent.right, 'data', None)

                    self.left_child = None if node.left is None else node.left.data
                    self.right_child = None if node.right is None else node.right.data
            elif(value < node.data):
                self.parent = node
                node = node.left
            else:
                self.parent = node
                node = node.right

        print "Value found: {}".format(str(value))
        if found:
            return {
                'found': found,
                'node_value': node,
                'parent_node': self.parent,
                'sibling': self.sibling,
                'left_child': self.left_child,
                'right_child': self.right_child,
            }
        else:
            "Value not found: {}".format(str(value))
            return {
                'found': found
            }

    def search(self, value):
        found = False
        node = self.root
        while(node != None and found == False):
            if(value == node.data):
                found = True
            elif(value < node.data):
                node = node.left
            else:
                node = node.right

        print "Value found: {}".format(str(value)) if found else "Value not found: {}".format(str(value))

    def delete(self, value):
        node = self.root
        found = False
        while(node != None and found == False):
            result = self.record_meta_data(value)
            found = result['found']
            parent = result.get('parent_node')
            node = result.get('node_value')
            if result.get('found'):
                if(result.get('left_child') != None and result.get('right_child') != None):
                    # Select righmost node of the left node
                    temp_node = node.left
                    while(temp_node.right.right != None):
                        temp_node = temp_node.right
                    node.data = temp_node.right.data
                    temp_node.right = None
                elif(result.get('left_child') != None and result.get('right_child') == None):
                    parent.left = node.left
                    print "Deleting {}".format(value)
                    node = None
                elif(result.get('left_child') == None and result.get('right_child') != None):
                    parent.right = node.right
                    print "Deleting {}".format(value)
                    node = None
                elif(result.get('left_child') == None and result.get('right_child') == None):
                    print "Deleting {}".format(value)
                    if node == parent.right:
                        paren.right = None
                    else:
                        parent.left = None
            else:
                print "value not found"

    def delete_recursive(self, root, number):
        """ Delete node using recursion algo """
        if root is None:
            return root
        elif (number < root.data):
            # If the node is deleted from the left subtree then we get back the address of
            # the new node. This new node is becomes left child of the root node
            root.left = self.delete_recursive(root.left, number)
        elif (number > root.data):
            root.right = self.delete_recursive(root.right, number)
        else:
            # Case 1: root has no children
            if (root.left is None and root.right is None):
                root = None
                return root
            # Case 2: root has one children
            elif (root.left is not None and root.right is None):
                temp = root
                root = root.left
                temp = None
            elif (root.right is not None and root.left is None):
                temp = root
                root = root.right
                temp = None
            # Case 3: root has 2 children
            else:
                max_element = self.find_max(root.left)
                root.data = max_element.data
                root.left = self.delete_recursive(root.left, max_element.data)

        return root


    def print_inorder(self, node=None):
        """ Print tree in-order """
        if node is not None:
            self.print_inorder(node.left)
            print node.data
            self.print_inorder(node.right)

    def print_preorder(self, node=None):
        """ Print tree pre-order """
        if node is not None:
            print node.data
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_postorder(self, node=None):
        """ Print tree post-order """
        if node is not None:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print node.data

    def purge(self, node):
        if node is not None:
            self.purge(node.left)
            self.purge(node.right)
            node.left = node.right = None

    def height(self, root):
        if root == None:
            return -1
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

    def find_min(self, root):
        if root is None:
            return root

        if root.left is None:
            return root

        return self.find_min(root.left)

    def find_max(self, root):
        if root is None:
            return root

        if root.right is None:
            return root

        return self.find_max(root.right)

if __name__ == '__main__':

    # Below commented line works
    '''
    Insert, print and purge test
    '''
    binary_tree = BinaryTree()
    for value in [5, 2, 1, 9, 10, 0, 6]:
        binary_tree.insert(value)


    for element in [5, 9]:
        meta_data = binary_tree.record_meta_data(element)
        if meta_data.get('found') is not None:
            for key, value in meta_data.iteritems():
                print "{}: {}".format(key, value)
        print "----------------------------------------"

    binary_tree.search(5)
    binary_tree.search(10)
    print "In-order----"
    binary_tree.print_inorder(binary_tree.root)
    print "Pre-order----"
    binary_tree.print_preorder(binary_tree.root)
    print "Post-order----"
    binary_tree.print_postorder(binary_tree.root)
    print "Height of the tree"
    print binary_tree.height(binary_tree.root)
    print "min element of the tree"
    min_element = binary_tree.find_min(binary_tree.root)
    print min_element.data
    print "max element of the tree"
    max_element = binary_tree.find_max(binary_tree.root)
    print max_element.data
    print "Purge-Tree----"
    binary_tree.purge(binary_tree.root)
    binary_tree.print_inorder(binary_tree.root)  # should print only root as we are passing root as param

    '''
    Delete test
    '''
    print "------------------- Delete operations -------------------------------------------"
    binary_tree_new = BinaryTree()
    print "Test Single Node deletion: 3 Cases"
    for value in [10, 5, 14, 3, 6, 4, 12, 16, 11, 18, 2]:
        binary_tree_new.insert(value)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 1: No child"
    binary_tree_new.delete(2)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 2-a: One left child"
    binary_tree_new.delete(12)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 2-b: One right child"
    binary_tree_new.delete(16)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 3: Two child"
    binary_tree_new.delete(5)
    binary_tree_new.print_inorder(binary_tree_new.root)

    print "Final Tree flow after all deletion"
    binary_tree_new.print_postorder(binary_tree_new.root)


    '''
    Delete test using recursion method
    '''
    print "------------------- Delete operations: using recursion -------------------------------------------"
    binary_tree_new = BinaryTree()
    print "Test Single Node deletion: 3 Cases"
    for value in [10, 5, 14, 3, 6, 4, 12, 16, 11, 18, 2]:
        binary_tree_new.insert(value)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 1: No child"
    binary_tree_new.delete_recursive(binary_tree_new.root, 2)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 2-a: One left child"
    binary_tree_new.delete_recursive(binary_tree_new.root, 12)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 2-b: One right child"
    binary_tree_new.delete_recursive(binary_tree_new.root, 16)
    binary_tree_new.print_inorder(binary_tree_new.root)
    print "Case 3: Two child"
    binary_tree_new.delete_recursive(binary_tree_new.root, 5)
    binary_tree_new.print_inorder(binary_tree_new.root)

    print "Final Tree flow after all deletion"
    binary_tree_new.print_postorder(binary_tree_new.root)