import sys
from utils import collector
from nlp import ngrammer
from nlp import model
from nlp import model
from utils import arithcode

def printhelp():
    print("""
Plainclothes is a fun but not very useful Python package that
"decompresses" any file into a longer file of plain, ASCII English text.

usage: python plainclothes.py <command> [<args>]

    plainclothes.py download [ gutenberg | wikipedia ]
    - Downloads pages off the internet and stores them as plain ASCII text in sources/.
    - Specify one or more sources as arguments
    - If no arguments are passed, downloads from all sources

    plainclothes.py collect
    - Collects all sources into sources/corpus.txt

    plainclothes.py ngrams [ n ]
    - Computes character ngrams of length up to n.

    plainclothes.py prob [ ngram ]
    - Computes modeled probability of the ngram
    - More specifically, the probability of the last character given the
      previous characters
    - ngram must be printable non-whitespace ASCII characters

© 2018 Conor Stuart Roe

""")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        printhelp()
    else:
        command = sys.argv[1]
        
        if command == "collect":
            collector.collect_all()
            
        elif command == "download":
            reader_names = sys.argv[2:]
            collector.download(reader_names)
            
        elif command == "ngrams":
            n = int(sys.argv[2])
            ngrammer.compute_ngrams(n,recursive=True)
            
        elif command == "generate":
            gram_size = int(sys.argv[2])
            length = int(sys.argv[3])
            lm = model.NgramModel(gram_size)
            print(lm.generate(length))
            
        elif command == "prob":
            ngram = sys.argv[2]
            gram_size = len(ngram)
            lm = model.NgramModel(gram_size)
            lm.put_chars(ngram[:-1])
            p = lm.get_prob(ngram[-1])
            print(p)
            
        elif command == "project":
            context = sys.argv[2]
            gram_size = min(8,len(context)+1)
            lm = model.NgramModel(gram_size)
            lm.put_chars(context)
            ps_list = lm.get_probs()
            with_letters = zip(model.LanguageModel.charset,ps_list)
            ps_list = sorted(with_letters,key = lambda x: x[1], reverse=True)
            for letter, p in ps_list[:10]:
                print(letter, round(p,3))

        elif command == "compress":
            message = sys.argv[2]
            lm = model.NgramModel(8)
            ac = arithcode.ArithmeticEncoder(lm)
            ba = ac.compress(message)
            print(ba.bin)
                
        elif command == "help":
            printhelp()
            
        else:
            print("Unknown command: " + command)
