## __init__.py 用于标识这是一个资源包

from .book import BookHandler
from .movie import MovieHandler
from .user import UserHandler

__all__ = ['BookHandler', 'MovieHandler', 'UserHandler']  # 定义仅导出这几个模块
