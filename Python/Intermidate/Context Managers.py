# To open a file and read content of it or write content such binary data files or csv files
"""
with open('notes.txt', 'w') as f:
    f.write('Hello World')

file=open('notes.txt','w')
try:
    file.write('Hello World')
finally:
    file.close()
#context manager for threading
from threading import Lock
lock=Lock()

lock.acquire()
#... lines od codes
lock.release()# need to write otherwise would cause deadlock
# other approach
with lock:
    #... here no need to mention
"""
#context manager for own classes
class ManagedFile:
        def __init__(self, filename):
            self.filename = filename
        def __enter__(self):
            print('enter')
            self.file = open(self.filename, 'w')
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
            if exc_type is not None:
                print('exception type')
            #print(exc_type, exc_val, exc_tb)
            print('exit')
            return True
    with ManagedFile('notes.txt') as f:
        print("do some stuff....")
        file.write('Hello World')
        file.somemethod()
    print('continuing')
