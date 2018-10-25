import sys
from utils import collector

if __name__ == "__main__":
    command = sys.argv[1]
    if command == "collect":
        collector.collect_all()
    elif command == "download":
        reader_names = sys.argv[2:]
        collector.download(reader_names)
    else:
        print("Unknown command: " + command)
