class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap1 = dict()
        hashMap2 = dict()
        for i in range(len(s)):
            if s[i] not in hashMap1:
                hashMap1[s[i]] = t[i]
            else:
                if hashMap1[s[i]] != t[i]:
                    return False
            if t[i] not in hashMap2:
                hashMap2[t[i]] = s[i]
            else:
                if hashMap2[t[i]] != s[i]:
                    return False
        return True
# Problem 205: https://leetcode.com/problems/isomorphic-strings/description/