'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
'''

class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0;
        cows = 0;
        # 0 indicates number is not seen in both secret and guess
        # negative number indicates number is seen in guess
        # positive number indicates number is seen in secret
        numbers = [0] * 10
        for index, val in enumerate(secret):
            s = int(secret[index])
            g = int(guess[index])
            if s == g:
                bulls = bulls + 1
            else:
                if numbers[s] < 0:
                    # as default is 0, however, if its less than 0, which indicates
                    # that guess has the number and count was marked as negative
                    cows = cows + 1
                if numbers[g] > 0:
                    # as default is 0, however, if its greater than 0, which indicates
                    # that secret has the number and count was marked as positive
                    cows = cows + 1
                numbers[s] = numbers[s] + 1
                numbers[g] = numbers[g] - 1

        return "{}A{}B".format(bulls, cows)



solution = Solution()
expected_result = "1A3B"
actual_result = solution.getHint("1807", "7810")
assert expected_result == actual_result

expected_result = "1A1B"
actual_result = solution.getHint("1123", "0111")
assert expected_result == actual_result