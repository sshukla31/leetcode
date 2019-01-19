from Queue import PriorityQueue



class Solution(object):
    def __init__(self):
        self.lowers = PriorityQueue()  # will be max_heap
        self.highers = PriorityQueue() # will be min_heap

    def peek(self, pq):
        return pq.queue[0]


    def get_median(self, array):
        self.add_numbers(array)
        self.rebalance()
        return self.find_median()

    def add_numbers(self, array):
        for num in array:
            if self.lowers.empty() or num < self.peek(self.lowers):
                # this makes min_heap as max_heap. simplest
                self.lowers.put(-num)
            else:
                self.highers.put(num)

    def rebalance(self):
        bigger = self.highers if self.lowers.qsize() < self.highers.qsize() else self.lowers
        smaller = self.highers if self.lowers.qsize() > self.highers.qsize() else self.lowers

        if bigger.qsize() - smaller.qsize() >= 2:
            is_abs = True if bigger == self.lowers else False
            total_size = bigger.qsize() + smaller.qsize()
            if total_size %2 == 0: # even
                while(bigger.qsize() > smaller.qsize()):
                    item = bigger.get()
                    smaller.put(abs(item)) if is_abs else smaller.put(-item)
            else:
                while(bigger.qsize() - smaller.qsize() != 1):
                    item = bigger.get()
                    smaller.put(abs(item)) if is_abs else smaller.put(-item)


    def find_median(self):
        if self.highers.qsize() == self.lowers.qsize():
            # get max of lower and min of higher
            return 0.5 * (abs(self.peek(self.highers)) + abs(self.peek(self.lowers)))
        elif self.highers.qsize() > self.lowers.qsize():
            return abs(self.peek(self.highers))
        else:
            return abs(self.peek(self.lowers))


if __name__ == '__main__':
    sol = Solution()
    array = [1, 4, 22, 2, 6, 201, 200]
    expected_result = 6
    actual_result = sol.get_median(sorted(array))
    assert expected_result == actual_result

    sol1 = Solution()
    array = [200, 18, 12, 204, 23, 16, 201, 22]
    expected_result = 22.5
    actual_result = sol1.get_median(sorted(array))
    assert expected_result == actual_result