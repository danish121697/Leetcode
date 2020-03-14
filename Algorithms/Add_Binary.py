class Solution(object):
    def addBinary(self, a, b):
        output = ""
        carry = 0
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for char_a, char_b in zip(a[::-1], b[::-1]):
            result = int(char_a) + int(char_b) + carry
            output += str(result % 2)
            carry = result // 2
            
        if carry:
            output += str(carry % 2)
        return output[::-1]
