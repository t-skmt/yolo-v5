from pathlib import Path
import sys
import os
import logging

# print(__file__, type(__file__))  # train.py <class 'str'>

FILE = Path(__file__).resolve()

# print(Path(__file__)))  # train.py
# print(type(Path(__file__))  # <class 'pathlib.PosixPath'>

# print(FILE)  # /home/tskmt/Github/yolov5_t-skmt/yolov5-t-skmt/train.py

# print(FILE.parents)  # <PosixPath.parents>
# print(type(FILE.parents))  # <class 'pathlib._PathParents'>


# for i in FILE.parents:
#     print(i)

# /home/tskmt/Github/yolov5_t-skmt/yolov5-t-skmt
# /home/tskmt/Github/yolov5_t-skmt
# /home/tskmt/Github
# /home/tskmt
# /home
# /


ROOT = FILE.parents[0]
# print(ROOT)  # /home/tskmt/Github/yolov5_t-skmt/yolov5-t-skmt

# print(sys.path)  # ['/home/tskmt/Github/yolov5_t-skmt/yolov5-t-skmt', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']  モジュール検索パス

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # train.pyがあるフォルダまでの相対パス
# print(ROOT)  # .

LOGGER = logging.getLogger(__name__)
# print(__name__)  # __main__
# print(LOGGER)  # <Logger __main__ (WARNING)>

def parse_opt(known=False):

    pass


if __name__ == "__main__":
    opt = parse_opt()