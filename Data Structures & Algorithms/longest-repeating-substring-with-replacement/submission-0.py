class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #key insight
        # window size – count of the most frequent character ≤ k
        counts = defaultdict(int)
        most_frequent = 0 #frequency of the most frequent letter
        left = 0
        for right in range(len(s)):
            c = s[right]
            counts[c] += 1
            # update most frequent on each letter
            most_frequent = max(most_frequent, counts[c])
            while right - left + 1 - most_frequent > k:
                counts[s[left]] -= 1
                left += 1
        return right - left + 1

