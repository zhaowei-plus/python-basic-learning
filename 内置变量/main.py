

def divide(a, b):
    assert b != 0, "除数不能为 0！"  # 仅在调试模式下生效
    return a / b

print(divide(10, 2))
print(divide(10, 0))  # 正常情况下会触发 AssertionError

if __debug__:
    # 指示当前 Python 脚本是否是以“调试模式”运行。
    print("__debug__")
    # 正常模式（默认调试模式运行）：python script.py -> __debug__ = True
    # 优化运行（带 -O或 -OO参数）：python -O script.py -> __debug__ = False, 此时会禁用 assert语句

if __name__ == '__main__':
    print("__main__")


