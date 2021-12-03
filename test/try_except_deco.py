
def try_exception(func):
    def hander(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    
    return hander

@try_exception
def say_hello(str):
    print(str)
    raise ZeroDivisionError("Zero")


if __name__ == "__main__":
    say_hello("aaa")
