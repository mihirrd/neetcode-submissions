from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canConvert(word1, word2):
            # assumes both words will always have same len
            same = 0
            for w1,w2 in zip(word1,word2):
                if w1 == w2:
                    same += 1
            return same == len(word1)-1
        
        if endWord not in set(wordList):
            return 0
        q = deque([(beginWord,0)])
        found = False
        visited = set()
        while q:
            w,count = q.popleft()
            if w in visited:
                continue
            visited.add(w)
            if w == endWord:
                count += 1
                found = True
                break
            for word in wordList:
                if canConvert(w,word):
                    q.append((word,count+1))                    
        

        return count if found else 0

