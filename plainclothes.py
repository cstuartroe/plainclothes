from arithcode import *
#from shancode import *

def generate_codes(context):
    probs = [prob.uint/2**20 for prob in model(context)]
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

with open('blue-winged-warbler.jpg','rb') as fh:
    bytecode = fh.read()[:1000]

ba = BitArray(bytecode)
bits = str(ba.bin)
p = plainclothes(bits)

with open('blue-winged-warbler.plc','w') as fh:
    fh.write(p)

##while True:
##    s = input('To encode: ')
##    ba = BitArray(s.encode('utf-8'))
##    bits = str(ba.bin)
##    p = plainclothes(bits)
##    print(p)
