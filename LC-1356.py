class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        l = []
        for i in arr:
            c = bin(i).split('1')
            l.append([len(c)-1,i])
        l.sort()
        fl= []
        for i in l:
            fl.append(i[1])
        return fl

