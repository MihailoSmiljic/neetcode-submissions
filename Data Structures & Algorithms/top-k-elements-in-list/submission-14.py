class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3]
        mapa = {}
        k_najvecih = []
        for elem in nums:
            if elem not in mapa:
                mapa[elem] = 1
                if elem not in k_najvecih and len(k_najvecih) < k:
                    k_najvecih.append(elem)
            else:
                mapa[elem] += 1
                if elem not in k_najvecih:
                    for i in range(len(k_najvecih)):
                        if (k_najvecih[i] != elem and mapa[k_najvecih[i]] < mapa[elem]):
                            k_najvecih.pop(i)
                            k_najvecih.append(elem)
                            break
        return k_najvecih