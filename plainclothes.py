from model import *
from shancode import *
from bitstring import BitArray

def generate_codes(context):
    probs = model(context)
    sc = Shancode(probs)
    codes = sc.codes
    d = {}
    for i in range(len(included_chs)):
        d[codes[i]] = included_chs[i]
    return d

def plainclothes(bits):
    out = ''
    queue = ''
    context = 'e. '
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

while True:
    s = input('To encode: ')
    ba = BitArray(s.encode('utf-8'))
    bits = str(ba.bin)
    p = plainclothes(bits)
    print(p)
