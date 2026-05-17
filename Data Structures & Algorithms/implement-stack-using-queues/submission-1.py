class Node:
    def __init__(self, x: int):
        self.element = x
        self.back = None

class MyStack:
    def __init__(self):
        self._top = None        # ← atribut sa donjom crtom
        self.length = 0
    
    def push(self, x: int) -> None:
        cvor = Node(x)
        cvor.back = self._top
        self._top = cvor
        self.length += 1

    def pop(self) -> int:
        if self.empty():
            return None
        pom = self._top.element
        self._top = self._top.back
        self.length -= 1
        return pom

    def top(self) -> int:        # ← metoda BEZ donje crte
        return self._top.element if self._top else None

    def empty(self) -> bool:
        return self.length == 0