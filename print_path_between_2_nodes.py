'''
Print path between any two nodes in a Binary Tree
Given a Binary Tree of distinct nodes and a pair of nodes.
The task is to find and print the path between the two given nodes in the binary tree.

		0
              /   \
            1      2
	  /  \     / \
        3     4   5   6
       /     / \
      7     8   9

For Example, in the above binary tree the path between the nodes 7 and 4 is 7 -> 3 -> 1 -> 4.


Reference:
https://www.geeksforgeeks.org/print-path-between-any-two-nodes-in-a-binary-tree/


The idea is to find paths form root nodes to the two nodes and store them in two separate vectors or arrays say path1 and path2.

Now, there arises two different cases:

If the two nodes are in different subtrees of root nodes. That is one in the left subtree and the other in the right subtree. In this case it is clear that root node will lie in between the path from node1 to node2. So, print path1 in reverse order and then path 2.
If the nodes are in the same subtree. That is either in the left subtree or in the right subtree. In this case you need to observe that path from root to the two nodes will have an intersection point before which the path is common for the two nodes from the root node. Find that intersection point and print nodes from that point in a similar fashion of the above case.
'''



import sys
import math

# structure of a node of binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None





# Driver program
if __name__=='__main__':

    # binary tree formation
    root = getNode(0)
    root.left = getNode(1)
    root.left.left = getNode(3)
    root.left.left.left = getNode(7)
    root.left.right = getNode(4)
    root.left.right.left = getNode(8)
    root.left.right.right = getNode(9)
    root.right = getNode(2)
    root.right.left = getNode(5)
    root.right.right = getNode(6)
    node1=7
    node2=4
    printPathBetweenNodes(root,node1,node2)