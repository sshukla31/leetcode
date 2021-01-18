'''
772. Basic Calculator III
Hard

550

218

Add to List

Share
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, open '(' and closing parentheses ')' and empty spaces ' '. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 6-4 / 2 "
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
Example 4:

Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
Output: -12
Example 5:

Input: s = "0"
Output: 0


Constraints:

1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', ')' and ' '.
s is a valid expression.


'''

### NOTE: This takes care of Basic Calculator 1, 2 and 3

class Solution:
    def calculate(self, s):
        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                # Python 3
                # stack.append(int(stack.pop()/num))

                # Python 2 use below
                #stack.append(int(float(stack.pop()) / num))

                # Note1: This section is required for such case: "14-3/2". Here, -3/2 can cause issue
                if  stack[-1]//num < 0 and stack[-1]%num!= 0:
                    stack[-1] = stack[-1]//num+1
                else:
                    stack[-1] = stack[-1]//num


        stack = []
        op = '+'
        num  = 0
        opset = set('+-/*')

        for c in s+'+':   # Note2: extra operator
            if c.isdigit():
                num = num*10 + int(c)
            elif c in opset or c == ')':
                update(op,num)
                num = 0
                op = c
                if c == ')':
                    tmp_num = 0
                    while stack[-1] not in opset:
                        tmp_num += stack.pop()
                    update(stack.pop(),tmp_num)
            elif c == '(':
                stack.append(op)
                num = 0
                op  = '+'


        return sum(stack)




if __name__ == '__main__':
    sol = Solution()

    # Test Case: 1
    s = "6+(2*3)-4/2"
    expected_value = 10
    actual_result = sol.calculate(s)
    assert expected_value == actual_result

    # Test Case: 2
    s = "(2+6* 3+5- (3*14/7+2)*5)+3"
    expected_value = -12
    actual_result = sol.calculate(s)
    assert expected_value == actual_result

    # Test Case: 3
    s = "0"
    expected_value = 0
    actual_result = sol.calculate(s)
    assert expected_value == actual_result


    # Test Case: 3
    s = " 6-4 / 2 "
    expected_value = 4
    actual_result = sol.calculate(s)
    assert expected_value == actual_result


