class BloomFilter:
    def __init__(self):
        self.bits = 0

    def add(self, element):
        hs = abs(hash(element)) % (2**32)
        low_hash = hs % (2**16)
        high_hash = (hs >> 16) % (2**16)
        self.bits |= 1 << low_hash
        self.bits |= 1 << high_hash

    def might_contain(self, element):
        hs = abs(hash(element)) % (2**32)
        low_hash = hs % (2**16)
        high_hash = (hs >> 16) % (2**16)
        return (self.bits & (1 << low_hash)) and (self.bits & (1 << high_hash))

    def _true_bits(self):
        return bin(self.bits).count("1")
