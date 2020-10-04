import magic
import os
from os import walk

def fix():
    mime = magic.Magic(mime=True)

    f = []
    for (dirpath, subdirs, filenames) in walk(os.getcwd()):
        for name in filenames:
            if mime.from_file(os.path.join(dirpath, name)) == 'text/html':
                if not name.endswith(".html"):
                    os.rename(os.path.join(dirpath, name), os.path.join(dirpath, name + ".html"))
    print("Fixed html URLs")
