import argparse
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]

# ========= parse_opt ========
known = False

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

opt = parser.parse_known_args()[0] if known else parser.parse_args()

print(opt)
print(opt.resume)
