'''
210. Course Schedule II

MEDIUM

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.



'''


# this solution is very similar to Find loop in Directed Graph
# reference: tushar roy https://www.youtube.com/watch?v=rKQaZuoUR4M
# there is a subtle difference though, we don't have a HashMap to keep track of
# parent nodes to print the flow

from collections import defaultdict


''' THIS SOLUTION FOLLOWS TOPOLOGICAL SORT'''

class Solution(object):
    WHITE = 0
    GREY  = 1
    BLACK = 2

    GRAPH = defaultdict(list)
    STACK = []
    VISITED = {}


    def build_adj_list(self, prerequisites):
        for dst, src in prerequisites:
            Solution.GRAPH[src].append(dst)


    def build_visited_map(self, num_courses):
        # num_courses represents the vertex value here and will be
        # in the range of courses passed in prerequisites
        # eg: Input: 2, [[1,0]]  , the course name is 0 and 1
        #            so when we do range(2), then value will be 0, 1 which is used for initial marking

        for i in range(num_courses):
            Solution.VISITED[i] = Solution.WHITE


    def dfs(self, vertex, is_loop=False):
        if is_loop is True:
            return False

        Solution.VISITED[vertex] = Solution.GREY
        for neighbor in Solution.GRAPH[vertex]:
            neighbor_status = Solution.VISITED[neighbor]
            if neighbor_status == Solution.BLACK:
                continue
            elif neighbor_status == Solution.GREY:
                # loop present in the graph
                is_loop = True
                return False
            else:
                self.dfs(neighbor, is_loop)


        Solution.VISITED[vertex] = Solution.BLACK
        Solution.STACK.append(vertex)

        return True



    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Step 1: Build adjacency list from prerequisites for traversal
        self.build_adj_list(prerequisites)

        # Step 2: Build Hash Map for visited node info
        #         WHITE: un-visited,
        #         GREY: visited but not all of its children
        #         BLACK: visited with all childrens are ready to insert into stack
        self.build_visited_map(numCourses)

        #if Solution.GRAPH == {}:
        #    return []

        # Step 3: Perform DFS on WHITE(unvisited) vertex
        is_loop = False
        for vertex in range(numCourses):
            if Solution.VISITED[vertex] == Solution.WHITE:
                self.dfs(vertex, is_loop)

        print  Solution.STACK[::-1]
        # Step 4: Print in reverse order if no loop
        return [] if is_loop else Solution.STACK[::-1]


def stringToInt(input):
    return int(input)

def stringToInt2dArray(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            numCourses = stringToInt(line)
            line = lines.next()
            prerequisites = stringToInt2dArray(line)

            ret = Solution().findOrder(numCourses, prerequisites)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()