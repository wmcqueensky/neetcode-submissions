class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [] * 10**4
        for i in range(10**4):
            self.set.append(ListNode(0))       

    def add(self, key: int) -> None:
        current = self.set[key % len(self.set)]
        while current.next:
            if current.next.key == key:
                return
            current = current.next
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.set[key % len(self.set)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        current = self.set[key % len(self.set)]
        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)