class Solution(object):
    def romanToInt(self, s):
        dicc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(0, len(s)-1 if len(s) > 1 else len(s)):
            if i == (len(s)-2) and dicc[s[i]] >= dicc[s[i+1]]:
                sum += dicc[s[i+1]]
            if i >= 1 and dicc[s[i]] > dicc[s[i-1]]:
                continue
            if len(s) > 1 and dicc[s[i]] < dicc[s[i+1]]:
                sum += dicc[s[i+1]] - dicc[s[i]]
            else:
                sum += dicc[s[i]]
        return sum