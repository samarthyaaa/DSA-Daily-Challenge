# context managers handle the setup and teardown of resources efficiently
# standard file handling using context manager
with open("notes.txt","w") as file:
    file.write("some todo...")
# custom context manager class
#implementing a custom context manager class using __enter__ and __exit__ methods
class ManagedFile:
    def __init__(self,filename):
        self.filename=filename

    def __enter__(self):
        print("enter")
        self.file=open(self.filename,"w")
        return self.file

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.file:
            self.file.close()
        print("exit")
        # returning True
        return True
with ManagedFile("notes.txt") as file:
    print("doing some work...")
    file.write("some todo...")
# context manager using contextlib generator
from contextlib import contextmanager
@contextmanager
def open_managed_file(filename):
    print("enter")
    file=open(filename,"w")
    try:
        yield file
    finally:
        file.close()
        print("exit")

with open_managed_file("notes.txt") as f:
    print("doing work with generator context manager...")
    f.write("some todo...")
