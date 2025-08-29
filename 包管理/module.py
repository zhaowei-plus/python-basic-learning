
## __all__ 控制 from module import *的行为

__all__ = ["func1", "ClassA"] # 只有 func1 和 ClassA 会被 from mymodule import * 导入

def func1():
    return "func1"


def func2():
    return "func2"


class ClassA:
    pass

class ClassB:
    pass