'''
226. Invert Binary Tree
Easy

1392

24

Favorite

Share
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Steps:
    1) DFS using stack
    2) first push root node in stack
    3) while stack is not empty continue next steps else return root
    4) swap node.left and node.right
    5) Push node.left in stack if not empty
    6) Push node.right in stack if not empty
    7) Wait until stack is empty

'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """


        if root is None:
            return None

        if root.left is None and root.right is None:
            return root


        stack = [root]

        while(stack):
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)


        return root



# testing code
node1 = Node('1')
node3 = Node('3')
node6 = Node('6')
node9 = Node('9')
node2 = Node('2', node1, node3)
node7 = Node('7', node6, node9)
node4 = Node('4', node2, node7)



sol = Solution()
actual_result = sol.invertTree(node4)
root = actual_result
try:
    assert root.value == "4"
    assert root.left.value == "7"
    assert root.right.value == "2"
    assert root.left.left.value == "9"
    assert root.left.right.value == "6"
    assert root.right.left.value == "3"
    assert root.right.right.value == "1"
    print "PASS"
except:
    print "FAIL"

