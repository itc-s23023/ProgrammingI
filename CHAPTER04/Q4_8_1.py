import time


def show_begin_end(func):
    """呼ばれた関数のはじめと終わりを表示するデコレータ"""

    def deco_func(*args, **kwargs):
        """関数を実行する前とあとにメッセージを追加"""
        print("== start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func


@show_begin_end
def sleep_for_a_while():
    """しばらく眠る"""
    print("Sleeping")
    time.sleep(2)
    print("Done Sleeping")


sleep_for_a_while()
