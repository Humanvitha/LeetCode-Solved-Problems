class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.buckets = 10000
        self.hashMap = [None] * self.buckets
        
    def put(self, key: int, value: int) -> None:
        hash1 = key % self.buckets
        if self.hashMap[hash1] is None:
            self.hashMap[hash1] = Node(key, value)
        else:
            current = self.hashMap[hash1]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
        
    def get(self, key: int) -> int:
        hash1 = key % self.buckets
        current = self.hashMap[hash1]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1
        
    def remove(self, key: int) -> None:
        hash1 = key % self.buckets
        current = self.hashMap[hash1]
        if not current:
            return
        
        if current.key == key:
            self.hashMap[hash1] = current.next
        else:
            prev = current
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    return
                prev = current
                current = current.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)

# Problem 706: https://leetcode.com/problems/design-hashmap/description/