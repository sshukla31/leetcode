"""
--------------
Level: Medium
--------------


In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?


Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length


"""


"""
Observations:
This problem is actually lengthOfLongestSubstringTwoDistinct

1) Keep 2 pointers i and start both pointing to 0 index
2) move i to read next value
3) keep adding the value at i'th index in hash map and increase the count
4) Check if the total count of keys in hash_map is greater than unique count
5) if yes, calculate the max_count until now and then start removing the extra value
   in the oder of insertion. To calculate max_count = max(max_count, index - start)
6) Here start pointer is used to remove keys in the order it was inserted to match
   the hash map count to unique count
7) Keep moving the window where start pointer indicates start of the window and
   index i indicates current value
8) Once the loop is over , return max(max_count, tree_len - start)

"""

def fruit_into_baskets(tree, unique=2):
    i = 0
    start = 0
    tree_len = len(tree)
    fruit_count = dict()
    max_count = 0

    if any([
        tree is None,
        tree_len == 0
    ]):
        return max_count

    for index, value in enumerate(tree):
        if value in fruit_count:
            fruit_count[value] = fruit_count[value] + 1
        else:
            fruit_count[value] = 1

        if len(fruit_count) > unique:
            max_count = max(max_count, index - start)
            while(len(fruit_count) > unique):
                start_value = tree[start]
                if fruit_count.get(start_value, 1) == 1:
                    fruit_count.pop(start_value)
                else:
                    fruit_count[start_value] = fruit_count[start_value] - 1

                start +=1

    max_count = max(max_count, tree_len - start)


    return max_count


if __name__=='__main__':
    actual_output = fruit_into_baskets([0, 1, 2, 2])
    expected_output = 3
    assert actual_output == expected_output

    actual_output = fruit_into_baskets([3,3,3,1,2,1,1,2,3,3,4])
    expected_output = 5
    assert actual_output == expected_output



