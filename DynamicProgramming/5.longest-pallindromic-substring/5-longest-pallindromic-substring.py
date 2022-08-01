class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 if i != j else 1 for j in range(len(s))] for i in range(len(s))]
        start, end = 0, 0
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                if s[i] == s[j]:
                    if j - i > 2:
                        if dp[i + 1][j - 1] == j - i - 1:
                            dp[i][j] = dp[i + 1][j - 1] + 2
                            if end - start + 1 < j - i + 1:
                                end, start = j, i
                    else:
                        dp[i][j] = j - i + 1
                        if end - start + 1 < j - i + 1:
                            end, start = j, i

        return s[start: end + 1]


def main():
    s = Solution()
    print(s.longestPalindrome("ramanandonanrz"))


if __name__ == '__main__':
    main()
