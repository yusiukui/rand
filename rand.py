from hashlib import sha_384
from time import time_ns
def _int32(x):
    return int(0xFFFFFFFF & x)

class Random:
    def __init__(self, seed=time_ns):
        self.mt = [0] * 624
        self.mt[0] = seed
        self.mti = 0
        for i in range(1, 624):
            self.mt[i] = _int32(1389**(1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i))


    def extract_number(self):
        for i in range(0,624):
          self.t()
          y = self.mt[self.mti]
          y = y ^ y >> 11
          y = y ^ y << 7 & 2636928640
          y = y ^ y << 15 & 4022730752
          y = y ^ y >> 18
          self.mti = (self.mti + 1) % 624
        for i in range(0,624):
          self.mt[i]=int(sha_384(self.mt[i].encode('utf-8')).hexdigest(),16)
        return _int32(y)


    def t(self):
        for i in range(0, 624):
            y = _int32((self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff))
            self.mt[i] = (y >> 1) ^ self.mt[(i + 397) % 624]

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df
