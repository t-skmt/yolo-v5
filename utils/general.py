import logging
import platform
from pathlib import Path
from subprocess import check_output
import contextlib
import os
import pkg_resources as pkg

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]


class WorkingDirectory(contextlib.ContextDecorator):
    """一時的にカレントディレクトリを移動する"""
    def __init__(self, dir):
        self.dir = dir
        self.cwd = Path.cwd().resolve()

    def __enter__(self):
        os.chdir(self.dir)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.cwd)


def set_logging(rank=-1, verbose=True):
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO if (verbose and rank in [-1, 0]) else logging.WARN)
        # ログの重大度を rankが0か-1 かつ verbose=Falseが
        # 指定されていなければINFOに、そうでなければWARNにする

def print_args(name, opt):
    """Print argparser arguments"""
    print(colorstr(f"{name}: ") + ", ".join(f"{k}={v}" for k, v in vars(opt).items()))

def colorstr(*input):
    *args, string = input if len(input) > 1 else ("blue", "bold", input[0])
    colors = {'black': '\033[30m',  # basic colors
              'red': '\033[31m',
              'green': '\033[32m',
              'yellow': '\033[33m',
              'blue': '\033[34m',
              'magenta': '\033[35m',
              'cyan': '\033[36m',
              'white': '\033[37m',
              'bright_black': '\033[90m',  # bright colors
              'bright_red': '\033[91m',
              'bright_green': '\033[92m',
              'bright_yellow': '\033[93m',
              'bright_blue': '\033[94m',
              'bright_magenta': '\033[95m',
              'bright_cyan': '\033[96m',
              'bright_white': '\033[97m',
              'end': '\033[0m',  # misc
              'bold': '\033[1m',
              'underline': '\033[4m'}
    return "".join(colors[x] for x in args) + f"{string}" + colors['end']

def try_except(func):
    # try-except function. Usage: @try_except decorator
    def handler(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    return handler

def is_docker():
    """Is environment a Docker container?"""
    return Path("/workspace").exists()  # or Path("/.dockerenv").exists()

def check_online():
    """Check internet connectivity"""
    import socket
    try:
        socket.create_connection(("1.1.1.1", 443), 5)  # check host accessibility
        return True
    except OSError:
        return False

def emojis(str=""):
    # Return platform-dependent emoji-safe version of string
    return str.encode().decode("ascii", "ignore") if platform.system() == "Windows" else str

@try_except  # エラーが起きても以降の処理を止めないようにする
@WorkingDirectory(ROOT)
def check_git_status():
    # Recommend 'git pull' if code is out of date
    msg = ", for updates see https://github.com/ultralytics/yolov5"
    print(colorstr("github: "), end="")
    assert Path(".git").exists(), "skipping check (not a git repository)" + msg
    assert not is_docker(), "skipping check (Docker image)" + msg
    assert check_online(), "skipping check (offline)" + msg

    cmd = "git fetch && git config --get remote.origin.url"
    url = check_output(cmd, shell=True, timeout=5).decode().strip().rstrip(".git")  # git fetch
    branch = check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode().strip()
    n = int(check_output(f"git rev-list {branch}..origin/master --count", shell=True))  # commits behind
    if n > 0:
        s = f"⚠️ YOLOv5 is out of date by {n} commit{'s' * (n > 1)}"
    else:
        s = f"up to date with {url}✅"
    print(emojis(s))

def check_python(minimun="3.6.2"):
    # check current python version vs. required python version
    check_version(platform.python_version(), minimun, name="Python ", hard=True)

def check_version(current="0.0.0", minimum="0.0.0", name="version", pinned=False, hard=False):
    # check version vs. required version
    # <class 'pkg_resources.extern.packaging.version.Version'>形式にparse_version()で変換する
    # 同じバージョンでも表記方法が複数あるため、正常に判定するために必要(例: "1.2.0" と "1.2"など)
    current, minimum = (pkg.parse_version(x) for x in (current, minimum))
    result = (current == minimum) if pinned else (current >= minimum)  # bool
    if hard:
        assert result, f"{name}{minimum} required by YOLOv5, but {name}{current} is currently installed"
    else:
        return result

@try_except
def check_requirements(requirements=ROOT / "requirements.txt", exclude=(), install=True):
    # check installed dependencies meet requirements (pass *.txt file or list of packages)
    prefix = colorstr("red", "bold", "requirements:")
    check_python()
    if isinstance(requirements, (str, Path)):  # requirementsがstrかPathクラスなら
        file = Path(requirements)
        assert file.exists(), f"{prefix} {file.resolve()} not found, check failed."
        with file.open() as f:
            requirements = [f"{x.name}{x.specifier}" for x in pkg.parse_requirements(f) if x.name not in exclude]
    print(requirements)
    pass
