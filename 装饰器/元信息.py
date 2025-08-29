from functools import wraps

def my_decorator(func):
    @wraps(func)
    # ✅ 重点：保留原函数的元信息，如函数名、文档字符串、模块信息等， 让装饰后的函数“看起来”更像原函数，对调试、日志、测试、文档、Web 框架等都非常重要， 通常用在装饰器内部的包装函数上
    def wrapper(*args, **kwargs):
        print("🔒 执行前...")
        result = func(*args, **kwargs)
        print("🔒 执行后...")
        return result
    return wrapper

@my_decorator
def say_hello():
    """这是一个打招呼的函数"""
    print("Hello, world!")

# 调用
say_hello()

# 查看函数信息
print(say_hello.__name__)  # 输出：say_hello ✅
print(say_hello.__doc__)   # 输出：这是一个打招呼的函数 ✅