class UserHandler:
    species = "UserHandler"  # 类方法

    def __init__(self, species):
        self.species = species

    @classmethod
    def create_default_person(cls):
        # 类方法作为“工厂方法”，返回一个默认的 Person 实例
        return cls("Default User")  # cls 相当于 UserHandler

    @classmethod
    async def register(cls, username: str, password: str):
        return "用户注册"

    # @classmethod 内置装饰器，用于定义类方法，可以通过类调用，也可以通过实例调用，与之对应的还有 @staticmethod
    @classmethod
    async def login(cls, username: str, password: str):
        # cls 表示是类对象本身，不是某个示例，可以通过 cls 来访问类变量，或者调用其他里类方法
        print("login:", username, password)
        # if not username:
        #     # TODO: 注意区分状态码
        #     raise HTTPException(status_code=404, detail="Username is not allow empty")
        return "用户登录"

    @classmethod
    async def get_user_detail(cls, user_id: int):
        return "获取用户详情"

    @classmethod
    async def get_users(cls, username: str):
        """获取用户列表"""
        # 参数校验
        # 调用业务层处理
        # 响应出参
        return "获取用户列表"
