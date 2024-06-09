class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = dict()
        for i in s:
            if i in hashMap.keys():
                hashMap[i] = hashMap[i] + 1
            else:
                hashMap[i] = 1
        odd = length = 0
        for i in hashMap.keys():
            if hashMap[i] % 2 == 0:
                length = length + hashMap[i]
            else:
                if hashMap[i] != 1:
                    length = length + (hashMap[i] - 1)
                odd = 1
        return length + odd

# using hashset

class Solution:
    def longestPalindrome(self, s: str) -> int:
        alphaSet = set()
        longestPalLength = 0
        for i in s:
            if i not in alphaSet:
                alphaSet.add(i)
            else:
                alphaSet.remove(i)
                longestPalLength += 2
        if alphaSet:
            longestPalLength += 1
        return longestPalLength
# Problem 409: https://leetcode.com/problems/longest-palindrome/description/