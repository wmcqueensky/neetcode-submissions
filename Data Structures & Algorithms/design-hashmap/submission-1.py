class ListNode:
    def __init__(self, key = -1, value = -1, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.buckets = [ListNode() for _ in range(1000)] #why not 10000?

    def hash(self, key):
        return key % len(self.buckets) #why not 1000 instead?

    def put(self, key: int, value: int) -> None:
        current = self.buckets[self.hash(key)]
        while current.next:
            if current.next.key == key:
                current.next.value = value
                return #why not break keyword?
            current = current.next
        current.next = ListNode(key, value) #  why not: = current.next.next

    def get(self, key: int) -> int:
        current = self.buckets[self.hash(key)]
        while current.next:
            if current.next.key == key:
                return current.next.value
            current.next = current.next.next
        return -1

    def remove(self, key: int) -> None:
        current = self.buckets[self.hash(key)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)