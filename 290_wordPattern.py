class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap1 = dict()
        hashMap2 = dict()
        temp = s.split()
        if len(pattern) != len(temp):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hashMap1.keys():
                if hashMap1[pattern[i]] != temp[i]:
                    return False
            else:
                hashMap1[pattern[i]] = temp[i]
            if temp[i] in hashMap2.keys():
                if hashMap2[temp[i]] != pattern[i]:
                    return False
            else:
                hashMap2[temp[i]] = pattern[i]
        return True
# Problem 290: https://leetcode.com/problems/word-pattern/description/