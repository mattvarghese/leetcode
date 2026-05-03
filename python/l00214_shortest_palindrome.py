# 214 https://leetcode.com/problems/shortest-palindrome/


class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        largestI = 0
        largestIisEven = False
        for i in range(((n + 1) // 2) - 1, -1, -1):
            isEvenPalindrome = True
            isOddPalindrome = True
            for j in range(i + 1):
                if isOddPalindrome and (s[j] != s[(2 * i) - j]):
                    isOddPalindrome = False
                if (
                    isEvenPalindrome
                    and (n <= ((2 * i) - j + 1))
                    or (s[j] != s[(2 * i) - j + 1])
                ):
                    isEvenPalindrome = False
                if (not isEvenPalindrome) and (not isOddPalindrome):
                    break
            if isEvenPalindrome or isOddPalindrome:
                largestI = i
                largestIisEven = isEvenPalindrome  # Even trumps Odd
                break

        palindromePrefixLen = (2 * largestI) + 1
        if largestIisEven:
            palindromePrefixLen += 1

        prefix = []
        for j in range(n - 1, palindromePrefixLen - 1, -1):
            prefix.append(s[j])

        return "".join(prefix) + s


class Solution3:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Combine string with its reverse and a separator
        # The separator '#' ensures the prefix-suffix match doesn't cross the middle
        combined = s + "#" + s[::-1]

        # Build the KMP LPS (Longest Prefix Suffix) table
        n = len(combined)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j

        # The last value in lps is the length of the longest palindromic prefix
        pal_len = lps[-1]

        # Add the remaining suffix (reversed) to the front
        suffix_to_add = s[pal_len:][::-1]
        return suffix_to_add + s


class Solution4:
    def shortestPalindrome(self, s: str) -> str:
        combined = s + "#" + s[::-1]

        n = len(combined)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j = j + 1
            lps[i] = j
        return s[j:][::-1] + s


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j = j + 1
            lps[i] = j
        j = 0
        for i in range(n - 1, -1, -1):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j = j + 1

        return s[j:][::-1] + s
