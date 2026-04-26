class Node:
    def __init__(self, key : int , value : int):
        self.key = key
        self.value = value
        self.sledeci = None
    
    def getNode(self) -> List:
        return [self.key , self.value]
class MyHashMap:

    def __init__(self):
        self._head_ = None
    


    def put(self, key: int, value: int) -> None:
        if (self._head_ == None):
            self._head_ = []
            novi = Node(key,value)
            self._head_.append(novi)
        else:
            pret = None
            pom = self._head_[0]
            while pom != None:
                if pom.key == key:
                    pom.value = value
                    return
                pret = pom
                pom = pom.sledeci
            novi = Node(key , value)
            pret.sledeci = novi
            self._head_.append(novi)
        
        

    def get(self, key: int) -> int:
        if not self._head_:
            return -1
        pom = self._head_[0]
        while pom != None:
            if pom.key == key:
                return pom.value
            pom = pom.sledeci
        return -1


    def remove(self, key: int) -> None:
        if not self._head_:
            return
        pom = self._head_[0]
        pret = None
        while pom != None:
            if pom.key == key:
                if pret == None:
                    if pom.sledeci:
                        self._head_[0] = pom.sledeci
                    else:
                        self._head_ = None
                    return
                else:
                    pret.sledeci = pom.sledeci
                    return
            pret = pom
            pom = pom.sledeci