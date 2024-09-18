class BitVector:
    def __init__(self, bits=0):
        self.bits = bits

    def __str__(self):
        return bin(self.bits)

    def get(self, i):
        return (self.bits >> i ) & 1

    def set(self, i, b):
        self.bits = (self.bits & ~(1<<i) | (b<<i))

    def union(self, other):
        return BitVector(self.bits | other.bits)

    def intersection(self,other):
        return BitVector(self.bits & other.bits)
