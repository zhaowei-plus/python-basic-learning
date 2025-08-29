import time
import datetime

## 支持 with 语句

############文件读写、数据库、网络连接、锁（threading.Lock）#############

### 场景1: 文件读写
with open("example.txt", "r") as f:
    content = f.read()
    print(content)


"""
with context_manager as variable:
    # 使用资源
    
等效于

variable = context_manager.__enter()__ # 进入时调用
try: 
    # with 块中的代码
finally:
    context_manager.__exit__(None, None, None) # 退出时调用，用于清理资源
"""

### 自定义实现
class MyResource:
    def __enter__(self):
        print("🔓 资源已获取（比如打开连接、分配内存等）")
        return self  # 可以返回一个对象，用 as 接收

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type 异常类型
        # exc_val 异常值
        # exc_tb 异常
        print("🔒 资源已释放（比如关闭连接、清理内存等）：", exc_type, exc_val, exc_tb)
        if exc_type:
            print(f"⚠️ 发生了异常：{exc_val}")
        # 返回 False 会重新抛出异常，True 则抑制异常（一般不推荐）

# 使用 with
with MyResource() as res:
    print("✅ 正在使用资源...")
    raise ValueError("测试异常")  # 你可以取消注释测试异常情况



class LogWriter:
    def __init__(self, filename):
        self.filename = filename

    # __enter__/__exit__ 是用于实现上下文管理协议（Context Manager Protocol）的两个特殊方法，使得 with 语句能够正常工作

    # __enter__ 在进入 with 语句代码块时调用，通常用于获取资源，如打开文件、获取锁等
    # 其返回值会赋予给 as 后面的变量
    def __enter__(self):
        self.file = open(self.filename, "a")
        return self

    # __exit__ 在退出 with 语句代码块时调用，无论发生什么异常，都会执行，通常用于释放资源，如关闭文件、释放锁等
    # 这里可以处理异常，决定是否抑制异常
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def write_log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"[{timestamp}] {message}\n")

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        self.interval = self.end - self.start
        print(f'Execution time: {self.interval:.2f} seconds')


# 使用上下文管理器写入日志
with LogWriter("log.txt") as logger, Timer() as timer:
    logger.write_log("Starting the logging process.")
    for i in range(5):
        time.sleep(1)
        logger.write_log(f"Log entry {i+1}")
    logger.write_log("Logging process completed.")



