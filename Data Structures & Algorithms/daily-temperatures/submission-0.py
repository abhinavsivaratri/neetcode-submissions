class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        stack.append(0)
        r = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                r[index] = i - index
            stack.append(i)
        return r