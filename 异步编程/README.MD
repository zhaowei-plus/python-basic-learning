# Python 异步编程


## 多进程

多进程是指启动多个独立的进程，每个进程都有自己独立的 Python 解释器和内存空间，因此不受 GIL 限制，可以真正实现并行计算

### 进程池

### 进程间通信（IPC）
Queue、Pipe、Manager	multiprocessing.Queue、Pipe、Manager

### 锁（Lock）保护共享资源
防止冲突	multiprocessing.Lock

## 多线程
### 线程池 / 进程池
### 线程间通信
queue.Queue(线程安全) threading + queue
### 锁（Lock）保护共享资源
防止冲突	threading.Lock


## 异步编程

asyncio


## 协程

在异步编程中，协程是非常轻量的，可以启动成千上万个协程，但是如果这协程同时执行一下操作：
- 访问API（可能有速率限制）
- 操作数据库连接（连接池限制）
- 读写文件或网络请求
- 抓取网页（爬虫）

等操作，可能会导致如下问题：
- 资源耗尽（如连接数过多、服务器拒绝、IP封禁等）
- 性能下降（无限制请求或过多请求，可能会造成争抢或阻塞）
- 被目标服务封禁或限流

此时，即可以通过使用 asyncio.Semaphore 信号量限制并发数量

```python
import asyncio

semaphore = asyncio.Semaphore(5) # 最多同时允许云巡更5个协程
```

# asyncio 库