class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = s.split(" ")
        inverted_s_array = s_array[::-1]
        for char in s_array[::-1]:
            if char == "":
                s_array.remove("")
        return " ".join(char for char in s_array[::-1])
