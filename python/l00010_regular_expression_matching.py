# 10 https://leetcode.com/problems/regular-expression-matching/


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        if sn == 0 and pn == 0:
            return True
        st = [(0, 0)]
        visited = set()
        while len(st) > 0:
            si, pi = st.pop()
            if (si, pi) in visited:
                continue
            visited.add((si, pi))
            while (si <= sn) and (pi < pn):
                sc = "" if si == sn else s[si]
                if ((pi + 1) < pn) and (p[pi + 1] == "*"):
                    if (p[pi] == ".") or (p[pi] == sc):
                        st.append((si + 1, pi))
                    pi += 2
                elif (p[pi] == ".") or (p[pi] == sc):
                    si += 1
                    pi += 1
                else:  # failed match
                    break
                if (si == sn) and (pi == pn):
                    return True
        return False


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        if sn == 0 and pn == 0:
            return True
        return self.isMatchRecursive(s, sn, 0, p, pn, 0)

    def isMatchRecursive(
        self, s: str, sn: int, si: int, p: str, pn: int, pi: int
    ) -> bool:
        while si <= sn and pi < pn:
            sc = "" if si == sn else s[si]
            if ((pi + 1) < pn) and (p[pi + 1] == "*"):
                if (p[pi] == ".") or (p[pi] == sc):
                    if self.isMatchRecursive(s, sn, si + 1, p, pn, pi):
                        return True
                pi += 2
            elif (p[pi] == ".") or (p[pi] == sc):
                si += 1
                pi += 1
            else:
                return False
            if (si == sn) and (pi == pn):
                return True
        return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        st = [(0, 0)]
        visited = set()

        while st:
            si, pi = st.pop()

            if (si, pi) in visited:
                continue
            visited.add((si, pi))

            # Base Case: If we finished the pattern, we must have finished the string
            if pi == pn:
                if si == sn:
                    return True
                continue

            # Look ahead for a star
            has_star = pi + 1 < pn and p[pi + 1] == "*"

            if has_star:
                # PATH 1: Match zero times (Skip the x*)
                st.append((si, pi + 2))

                # PATH 2: Match one or more (Consume if characters match)
                if si < sn and (p[pi] == s[si] or p[pi] == "."):
                    st.append((si + 1, pi))
            else:
                # PATH 3: Standard match (No star)
                if si < sn and (p[pi] == s[si] or p[pi] == "."):
                    st.append((si + 1, pi + 1))

        return False
