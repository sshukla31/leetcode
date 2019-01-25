'''
297. Serialize and Deserialize Binary Tree
Hard

1161

58

Favorite

Share
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.index = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized_result = []
        self.preorder(root, serialized_result)

        return serialized_result


    def preorder(self, root, serialized_result):
        if root is None:
            serialized_result.append(None)
            return

        serialized_result.append(root.val)
        self.preorder(root.left, serialized_result)
        self.preorder(root.right, serialized_result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if self.index == len(data) or data[self.index] == None:
            return None

        new_node = TreeNode(data[self.index])
        self.index += 1
        new_node.left = self.deserialize(data)
        self.index += 1
        new_node.right = self.deserialize(data)


        return new_node




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))