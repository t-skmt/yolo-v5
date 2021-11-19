import logging


def set_logging(rank=-1, verbose=True):
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO if (verbose and rank in [-1, 0]) else logging.WARN)
        # ログの重大度を rankが0か-1 かつ verboseにFalseが
        # 指定されていなければINFOに、そうでなければWARNにする
