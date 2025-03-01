class Solution:

    def encode(self, strs):
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '/' + s
        return encoded

    def decode(self, s):
        decoded = []
        i = 0
        len_counter = 0
        len_str = None
        while i != len(s):
            if i == 0 or len_counter == int(len_str):
                decoded.append('')
                len_str = ''
                while s[i] != '/':
                    len_str += s[i]
                    i += 1
                i += 1  # Skip '/'
                len_counter = 0
                continue
            decoded[-1] += s[i]
            i += 1
            len_counter += 1
        return decoded
