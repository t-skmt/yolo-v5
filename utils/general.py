import logging


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
