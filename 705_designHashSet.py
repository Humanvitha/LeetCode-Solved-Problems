class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.bucketItems = 1000
        self.hashSet = [[]] * self.buckets

    def add(self, key: int) -> None:
        hash1 = key % self.buckets
        hash2 = key // self.bucketItems
        if not self.hashSet[hash1]:
            if hash1 == 0:
                self.hashSet[hash1] = [False]*(self.bucketItems + 1)
            else:
                self.hashSet[hash1] = [False]*self.bucketItems
        self.hashSet[hash1][hash2] = True
        

    def remove(self, key: int) -> None:
        hash1 = key % self.buckets
        hash2 = key // self.bucketItems
        # if contains(self,key):
        #     self.hashSet[hash1][hash2] = False
        if self.hashSet and self.hashSet[hash1]:
            self.hashSet[hash1][hash2] = False
        

    def contains(self, key: int) -> bool:
        hash1 = key % self.buckets
        hash2 = key // self.bucketItems
        if self.hashSet and not self.hashSet[hash1]:
            return False
        return self.hashSet[hash1][hash2]
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#Problem 705: https://leetcode.com/problems/design-hashset/description/