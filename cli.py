import sys
from utils import collector
from nlp import ngrammer

def printhelp():
    print("""
Plainclothes is a fun but not very useful Python package that
"decompresses" any file into a longer file of plain, ASCII English text.

usage: python cli.py <command> [<args>]

    cli.py download [ gutenberg | wikipedia ]
    - Downloads pages off the internet and stores them as plain ASCII text in sources/.
    - Specify one or more sources as arguments
    - If no arguments are passed, downloads from all sources

    cli.py collect
    - Collects all sources into sources/corpus.txt

    cli.py ngram [ n ]
    - Computes character ngrams of length up to n.

© 2018 Conor Stuart Roe

""")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        printhelp()
        quit()
    command = sys.argv[1]
    if command == "collect":
        collector.collect_all()
    elif command == "download":
        reader_names = sys.argv[2:]
        collector.download(reader_names)
    elif command == "ngrams":
        n = int(sys.argv[2])
        ngrammer.get_ngrams(n)
    elif command == "help":
        printhelp()
    else:
        print("Unknown command: " + command)
