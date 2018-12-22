class BurstBalloons(object):

    '''
     * Dynamic programming solution.
     '''
    def maxCoinsBottomUpDp(self, nums):
	len_nums = len(nums)
        if len_nums == 0:
            return 0

        T = [[0 for _ in xrange(len_nums)] for _ in xrange(len_nums)]

	for window_len in xrange(1, len_nums+1):
            for i in xrange(len_nums+1 - window_len):
                j = i + window_len - 1
		for k in range(i, j+1):
                    # leftValue/rightValue is initially 1. If there is element on
                    # left/right of k then left/right value will take that value.
                    # Note: leftValue is left value to the current index K
                    #       rightValue is right value to the current index K
                    # eg: [3] - left*3*right -> 1*3*1 ->3   # window len=1
                    # eg2: [3, 1]- where k=0, this means 3 is last to burst and 1 already bursted
                    #              then, left*3*right -> 1*3*5 = 15.
                    #              As 1 is already bursted, to the right of 1 is 5 in nums
                    leftValue = 1   # when k is the first element in the range
                    rightValue = 1  # when k is the last element
                    if not (i == 0):
                        # if the left value is not out index we take it or apply default 1
                        leftValue = nums[i-1]
                        # i-1 because all baloons between i & k are bursted
                    if not (j == len_nums -1):
                        # if the right value is not out index we take it or apply default 1
                        # j + 1 because all baloons between k & j are bursted
                        rightValue = nums[j+1]

                    # before is initially 0. If k is i then before will
                    # stay 0 otherwise it gets value T[i][k-1]
                    # after is similarly 0 initially. if k is j then after will
                    # stay 0 other will get value T[k+1][j]
                    # * NOTE: before and after are dependent on window_len(len of current window)
                    #         although, we have left & right value available in array nums
                    #         but if we look from window_len perspective there are no elements left and right
                    #
                    # eg: when we take window_len = 1 and suppose i=j=2, all we should think of is [1],
                    # where there is no left and right value. This is only applicable for before and after
                    # however, for leftValue and rightValue it looks at all indexes, hence, we pick the values
                    # taking the same example: [1] with i=j=2, leftValue=3, rightValue=5, before=0, after=0
                    # eg:2 - [3, 1] when 3 is last to burst, i=0, j = 1, k=0, leftValue=1, rightValue=5,
                    #                                        before=0, after=maxValueOf(1) when bursted which is 15
                    before = 0
                    after = 0
                    if (i != k):
                        before = T[i][k-1]
                    if (j != k):
                        after = T[k+1][j]
                    T[i][j] = max(
                        leftValue * nums[k] * rightValue + before + after,
                        T[i][j]
                    )


        return T[0][len_nums - 1]



bb = BurstBalloons()

input = [2, 4, 3, 5];
# actual_result = bb.maxCoinsBottomUpDp(input)
# expected_result = 115
# assert actual_result == expected_result

input = [3, 1, 5, 8];
actual_result = bb.maxCoinsBottomUpDp(input)
expected_result = 167
assert actual_result == expected_result