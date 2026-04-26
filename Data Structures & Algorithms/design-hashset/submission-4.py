class MyHashSet:

    def __init__(self):
        self._set_ = []

    def add(self, key: int) -> None:
        for i in self._set_:
            if key == i:
                return
        
        self._set_.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self._set_)):
            if self._set_[i] == key:
                self._set_.pop(i)# self._set_[len(self._set_) - 1]
                # self._set_ = self._set_[0:i] + self._set_[i+1 : len(self._set_)]
                # self._set_[len(self._set_) - 1] = None
                # self._set_ = self._set_[0:len(self._set_) -1]
                return

    def contains(self, key: int) -> bool:
        for i in range(len(self._set_)):
            if self._set_[i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)