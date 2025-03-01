class Solution:

    
    def encode(self, strs):
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '/' + s)
        return ''.join(encoded)

    def decode(self, s):
        decoded = []
        i = 0
        while i != len(s):
            j = i
            while s[j] != '/':
                j += 1
            len_str = s[i:j]
            decoded.append(s[j+1:j+1+int(len_str)])
            i = j + 1 + int(len_str)
        return decoded
