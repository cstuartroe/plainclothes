from model import *

def arithcode(context,seq,precision):
    out = BitArray()
    midbits = -1
    lowbound = 0
    upbound = 0
    for letter in seq:
        assert(letter in included_chs)
        
