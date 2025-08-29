class BookHandler:
    @classmethod
    async def get_books(cls, book_name: str):
        """获取图书列表"""
        # 参数校验
        # 调用业务层处理
        # 响应出参
        return "获取图书列表"

    @classmethod
    async def get_book_detail(cls, book_id: int):
        return "获取图书详情"
