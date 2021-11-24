class MyManager():
    def __enter__(self):
        print("enter☟")
        print(self.__dict__)
    
    def __exit__(self):
        print("exit ☞")

m = MyManager()
with m:
    print(1 + 1)

# import contextlib
# from pathlib import Path
# import os

# FILE = Path(__file__).resolve()
# ROOT = FILE.parents[1]
# print(ROOT)
# print(type(ROOT))

# class WorkingDirectory(contextlib.ContextDecorator):
#     def __init__(self, newdir):
#         self.dir = newdir
#         self.cwd = Path.cwd().resolve()
    
#     def __enter__(self):
#         print("enter☟")
#         os.chdir(self.dir)

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type, exc_val, exc_tb)
#         print("exit ☞")
#         print(self.cwd)
#         os.chdir(self.cwd)

# print(Path.cwd().resolve())

# @WorkingDirectory(ROOT)
# def sayhello():
#     print("Hello,")
#     print(os.getcwd())
#     print("ROOT -> ")
#     a, b, c, d = ROOT
#     print(a, b, c, d)  #TypeError: cannot unpack non-iterable PosixPath object


# if __name__ == "__main__":
#     sayhello()