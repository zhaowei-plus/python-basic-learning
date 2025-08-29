
############################## 案例：__init__ /__del__调用案例 ######################################
class Greeter:
    def __new__(cls, *args, **kwargs):
        print("__new__")
        # 1、创建对象（通常调用父类的 __new__，例如object.__new__(cls)）
        instance = super().__new__(cls)  # 通常这么写
        # 2、必须返回一个对象（通常是这个 instance）
        return instance


    def __init__(self, name):
        # 构造函数：初始化代码，通用该实例绑定属性
        print("类的构造函数（初始化方法）")
        self.name = name

    def __del__(self):
        # 类的析构函数（销毁方法）
        # 在对象被垃圾回收（即销毁）时，可能会调用 __del__方法，一般用于执行一些清理操作，如关闭文件、断开网络连接、释放资源等
        # 推荐使用上下文管理器（with语句）和 .close()方法来管理资源
        # TODO: 请注意不推荐依赖__del__方法做关键的资源管理，因为__del__方法的调用时机不确定，具体是有Python的垃圾回收机制决定的
        print("析构函数（销毁方法）")

        # 推荐：用 with 自动管理资源（比如文件）
        with open("example.txt", "r") as f:
            content = f.read()
        # 文件会在离开 with 块后自动关闭，无需依赖 __del__


g = Greeter("Alice") # -> 类的构造函数（初始化方法）
# 当一个对象没有任何引用指向它时，Python 可能会在某个时刻销毁它，并调用 __del__
g = None #  -> 析构函数（销毁方法）


############################## 案例：__new__ 实现单例模式 ######################################
## 1、使用 __new__ 方法实现单例模式
class Singleton:
    _instance = None

    # __new__(cls, xxx) 是一个类方法，在对象被创建时第一个被调用，负责实际创建并返回一个新的对象实例
    def __new__(cls, *arg, **kwargs):
        if not cls._instance:
            # 1、创建对象（通常调用父类的 __new__，例如object.__new__(cls)）
            cls._instance = super(Singleton, cls).__new__(cls, *arg, **kwargs)

        # 2、必须返回一个对象（通常是这个 instance）
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

print("singleton:", singleton1 is singleton2)  # True


## 2、控制一个不可变类型的子类化（比如继承str、tuple、int等）
# 实现：自定义一个字符串子类，在创建时修改内容

class GreetingStr(str):
    def __new__(cls, value):
        # 1、在创建字符串时就修改内容
        value = "哈喽, " + value + " 你好"

        # 2、必须通过 __new__ 创建并返回字符串对象
        return super().__new__(cls, value)


s = GreetingStr("张三")
print(s) ## 哈喽, 张三 你好













