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


opt = parser.parse_known_args()[0] if known else parser.parse_args()

print(opt)
