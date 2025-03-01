class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        answer = ""
        while i < len(word1) and i < len(word2):
            answer += word1[i] + word2[i]
            i += 1
        if i < len(word1):
            answer += word1[i:]
        elif i < len(word2):
            answer += word2[i:]
        return answer