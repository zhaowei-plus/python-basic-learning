## 用于支持以模块方式运行一个包（package）
# 使用 python -m 包名的方式运行一个 Python 包时，Python 会自动执行该包下的 __main__.py文件
# 适用于模块化项目、工具包、库，想支持 python -m方式运行

from .user import UserHandler

print("🚀 你正在通过 `python -m myapp` 运行这个包！")

def main():
    UserHandler.register("张三", "123456")

    print("Hello from __main__.py!")

if __name__ == "__main__":
    # 对于单py文件直接运行该脚本时才会执行的代码
    main()

# 使用场景：
# 1. 让一个包支持命令行直接运行（python -m 包名）
#  当希望 Python 工具包 即可以作为模块导入使用，也可以直接运行，则可以设置 __main__.py 入口文件，用于独立运行
# 2、替代独立的 CLI 入口脚本（更 Pythonic 的方式）
# 很多项目会做一个单独的 main.py或者可执行脚本，但其实使用 python -m 包名+ __main__.py是更符合 Python 模块化思想的方式