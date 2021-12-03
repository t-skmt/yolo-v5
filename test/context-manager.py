import contextlib
from pathlib import Path
import os

class WorkingDirectory(contextlib.ContextDecorator):
    """一時的に作業ディレクトリを移動する"""
    def __init__(self, new_dir):
        self.dir = new_dir
        self.cwd = Path.cwd().resolve()
        pass

    def __enter__(self):
        print("enter")
        print("self.dir:", self.dir)
        print("self.cwd:", self.cwd)
        print("now:", os.getcwd())
        os.chdir(self.dir)
        print("now:", os.getcwd())
    
    def __exit__(self, exc_type, exc_value, trace):
        print("exit")
        print("now:", os.getcwd())
        os.chdir(self.cwd)
        print("now:", os.getcwd())
        print('Exception type: {}'.format(exc_type))
        print('Exception value: {}'.format(exc_value))
        print('Exception trace back {}'.format(trace))

@WorkingDirectory("/workspace")  # with文でも使用可能
def show_items():
    import subprocess
    print("-----")
    subprocess.run(["ls"])
    print("-----")


if __name__ == "__main__":
    # with WorkingDirectory("/workspace"):  # decoratorでも使用可能
    #     show_items()
    show_items()
