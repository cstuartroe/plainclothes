#from arithcode import *
from utils.shancode import Shancode
import .model

lm = NgramModel(6)

def generate_codes(context):
    probs = [prob.uint/2**20 for prob in lm.model(context)]
    sc = Shancode(probs)
    codes = sc.codes
    d = {}
    for i in range(len(included_chs)):
        d[codes[i]] = included_chs[i]
    return d

def plainclothes(bits):
    out = ''
    queue = ''
    context = 'ers. '
    try:
        codes = generate_codes(context)
    except IndexError:
        print(context)
        raise IndexError()
    for bit in bits:
        queue += bit
        ch = codes.get(queue,None)
        if ch:
            out += ch
            queue = ''
            context = context[1:] + ch
            codes = generate_codes(context)
    return out
