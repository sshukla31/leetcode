'''
23. Merge k Sorted Lists
Hard

1941

124

Favorite

Share
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

Steps:
1) Create a PriorityQueue(minHeap-default)
2) Traverse through list and insert in PQ
3) Pop out PQ elements and rebuild the list
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 0:
            return


        pq = PriorityQueue()

        for node in lists:
           while(node is not None):
                    print node.val
                    pq.put((node.val, node))
                    node = node.next



        if pq.empty():
            return

        _, root = pq.get()
        temp = root

        while(not pq.empty()):
            _, node = pq.get()
            temp.next = node
            temp = temp.next

        temp.next = None


        return root







