class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        minimum = 101
        target_pos = []
        n = len(words)
        if words[startIndex] == target:
            return 0
        for i in range(n):
            if words[i] == target:
                target_pos.append(i)
        for pos in target_pos:
            if (pos - startIndex) % n < minimum:
                minimum = (pos-startIndex) % n 
            if (startIndex - pos) % n < minimum:
                minimum = (startIndex - pos) % n 
        return minimum
        