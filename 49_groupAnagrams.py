class Solution:
    def prime(self, s: str):
        primes = [2, 3, 5, 7, 11, 13,
                 17, 19, 23, 29, 31,
                 37, 41, 43, 47, 53, 
                 59, 61, 67, 71, 73, 
                 79, 83, 89, 97, 101]
        result = 1
        for j in s:
            order = ord(j) - ord('a')
            result = result * primes[order]
        return result
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for i in strs:
            primeProduct = self.prime(i)
            if primeProduct in hashMap.keys():
                hashMap[primeProduct] += [i]
            else:
                hashMap[primeProduct] = [i]
        return hashMap.values()       
# Problem 49: https://leetcode.com/problems/group-anagrams/description/