class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        lst = [list(i) for i in strs]
        for i in range(len(lst[0])):
            col = []
            for j in lst:
                col.append(j[i])
            if sorted(col) != col:
                counter += 1
        return counter