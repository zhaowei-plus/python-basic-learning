
# setup.py 为打包配置文件，通常用于打包和发布Python项目

from setuptools import setup, find_packages

setup(
    name="models",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",  # 依赖其他库
    ]
)

# 本地开发模式安装此包：
# pip install -e .
