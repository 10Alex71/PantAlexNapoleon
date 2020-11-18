class Solution:

    def romanToInt(self, s: str) -> int:
        warning = ', this number is more than 3999'
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, e in enumerate(s):
            if (i + 1) == len(s) or romans[e] >= romans[s[i + 1]]:
                result += romans[e]
            else:
                result -= romans[e]
        if result > 3999:
            res = str(str(result) + warning)
            return res
        else:
            return result


a = input()
solution = Solution()
print(solution.romanToInt(a))