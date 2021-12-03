# referece: https://qiita.com/chocomintkusoyaro/items/214f87a6300a88d15363

# デコレータの復習
def deco(func):
    def _wrapper(content):
        print("starting")
        r = func(content)
        print("done. {}".format(r))
    return _wrapper


@deco
def print_msg(text):
    print(text)
    return 1


if __name__ == "__main__":
    msg = "Hello"
    print("START")
    print_msg(msg)
    print("END")
