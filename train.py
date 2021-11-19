from pathlib import Path
import sys
import os
import logging
import argparse

from utils.general import print_args, set_logging

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

RANK = int(os.getenv("RANK", -1))

def parse_opt(known=False):
    parser = argparse.ArgumentParser()

    parser.add_argument("--weights", type=str, default=ROOT / "yolov5s.pt", help="initial weights path")
    #  print(opt.weights, type(opt.weights))  # /workspaces/yolo-v5/yolov5s.pt <class 'pathlib.PosixPath'>
    parser.add_argument("--cfg", type=str, default="", help="model.yaml path")
    parser.add_argument("--data", type=str, default=ROOT / "data/coco128.yaml", help="dataset.yaml path")
    parser.add_argument("--hyp", type=str, default=ROOT / "data/hyps/hyp.scratch.yaml", help="hyperparameters path")
    parser.add_argument("--epochs", type=int, default=300)
    parser.add_argument("--batch-size", type=int, default=16, help="total batch size for all GPUs")
    parser.add_argument("--imgsz", "--img", "--img-size", type=int, default=640, help="train, val image size (pixels)")
    parser.add_argument("--rect", action="store_true", help="rectangular training")
    # --rect: 長辺を指定サイズに合わせるリサイズ処理を行い、短辺側は短辺が収まる最小の32の倍数の長さでパディングする
    parser.add_argument("--resume", nargs="?", const=True, default=False, help="resume most resent training")
    # --resumeの後ろに引数が1つあるならそれを、なければconstの値(=True)を使用
    parser.add_argument("--nosave", action="store_true", help="only save final checkpoint")
    parser.add_argument("--noval", action="store_true", help="only validate final epoch")
    parser.add_argument("--noautoanchor", action="store_true", help="disable autoanchor check")
    parser.add_argument("--evolve", type=int, nargs="?", const=300, help="evolve hyperparameters for x generations")
    #  --evolve: ハイパーパラメータの最適化手法に遺伝的アルゴリズムを使用する
    parser.add_argument("--bucket", type=str, default="", help="gsutil bucket")
    # evolve.csvをダウンロードするためのGoogle Cloud Storageのバケットを指定。--evolveを使用するときのみ有効。
    parser.add_argument("--cache", type=str, nargs="?", const="ram", help="--cache images in 'ram' (default) or 'disk'")
    parser.add_argument("--image-weights", action="store_true", help="use weighted image selection for training")
    # 前のエポックでのmAPの逆数で重み付けされた画像をサンプリングする
    parser.add_argument("--device", default="", help="cuda device, i.e. 0 or 0,1,2,3 or cpu")
    parser.add_argument("--multi-scale", action="store_true", help="vary img-size +/-50%%")
    # 学習中に画像サイズを+/-50%変化させる
    parser.add_argument("--single-cls", action="store_true", help="train multi-class data as single-class")
    # すべてのクラスを1クラス("item")として学習させる
    parser.add_argument("--adam", action="store_true", help="use torch.optim.Adam() optimizer")
    parser.add_argument("--sync-bn", action="store_true", help="use SyncBatchNorm, only available in DDP mode")
    # 複数GPUでの学習時にミニバッチ全体の入力を正規化する
    parser.add_argument("--workers", type=int, default=8, help="maximum number of dataloader workers")

    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt


def main(opt):
    # Checks
    set_logging(RANK)
    if RANK in [-1, 0]:
        # print(FILE.stem)  # train
        print_args(FILE.stem, opt)
    pass


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
