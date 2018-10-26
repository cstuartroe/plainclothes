#from arithcode import *
from utils.shancode import Shancode
import .model

def generate_codes(lm, context):
    probs = [prob.uint/2**20 for prob in lm.model(context)]
    sc = Shancode(probs)
    codes = sc.codes
    d = {}
    for i in range(len(included_chs)):
        d[codes[i]] = included_chs[i]
    return d

def decompressBits(gram_size, bits):
    out = ''
    queue = ''
    context = '`'*gram_size
    codes = generate_codes(context)
    for bit in bits:
        queue += bit
        ch = codes.get(queue,None)
        if ch:
            out += ch
            queue = ''
            context = context[1:] + ch
            codes = generate_codes(context)
    return out
