class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a),len(b))):
            ca = int(a[i]) if len(a) > i else 0
            cb = int(b[i]) if len(b) > i else 0
            current = ca + cb + carry
            if current == 2:
                current = 0
                carry = 1
            elif current == 3:
                current = 1
                carry = 1
            else:
                carry = 0
            res.append(current)
        if carry:
            res.append(carry)
        return ''.join(map(str,res[::-1]))
        
                