from urllib import request as ur
import re
import os
import time

class Reader:
    def __init__(self):
        self.sources_dir = os.path.join(os.path.dirname(__file__),'../sources/',self.name)
        if not os.path.isdir(self.sources_dir):
            os.makedirs(self.sources_dir)
        for file in os.listdir(self.sources_dir):
            filepath = os.path.join(self.sources_dir, file)
            if os.path.isfile(filepath):
                os.unlink(filepath)
        print("Initialized reader " + self.name)

    def read(self,source):
        url = os.path.join(self.url_root, source["path"])

        try:
            document = ur.urlopen(url).read()
        except TimeoutError:
            print("Request timed out. Retrying...")
            return self.read(source)
            
        text = self.get_text(document,source)
        text = re.sub('\s+',' ',text)

        filepath = os.path.join(self.sources_dir,source["name"]+".txt")
        with open(filepath, "w", encoding='utf-8') as fh:
            fh.write(text)

        print("Success")

    def read_all(self):
        start_time = time.time()
        
        for source in self.sources:
            print('Reading %s...' % source['name'])
            self.read(source)

        print('Read %d articles.' % len(self.sources))
        elapsed = int(time.time() - start_time)
        print('Took %d seconds.' % elapsed)
