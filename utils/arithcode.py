from bitstring import BitArray
from nlp import model

charsetd = model.LanguageModel.charsetd

class ArithmeticEncoder:
    def __init__(self,_lm):
        self.lm = _lm

    def compress(self,charstring):
        out = BitArray()
        floor = 0
        ceiling = 1

        self.lm.refresh()

        for char in charstring:
            probs = self.lm.get_probs()
            i = charsetd[char]
            newfloor = sum(probs[:i])
            newceiling = newfloor + probs[i]
            
            d = ceiling-floor
            newfloor = floor + (d*newfloor)
            newceiling = floor + (d*newceiling)

            while newfloor >= .5 or newceiling < .5:
                if newceiling < .5:
                    out.append("0b0")
                    newfloor = newfloor*2
                    newceiling = newceiling*2
                if newfloor >= .5:
                    out.append("0b1")
                    newfloor = (newfloor*2) - 1
                    newceiling = (newceiling*2) - 1

            floor, ceiling = newfloor, newceiling
            self.lm.put_char(char)

        return out
