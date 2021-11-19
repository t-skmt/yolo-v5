import logging


def set_logging(rank=-1, verbose=True):
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO if (verbose and rank in [-1, 0]) else logging.WARN)
        # ログの重大度を rankが0か-1 かつ verbose=Falseが
        # 指定されていなければINFOに、そうでなければWARNにする

def print_args(name, opt):
    """Print argparser arguments"""
    print("" + ",".join(f"{k}={v}" for k, v in vars(opt).items()))


