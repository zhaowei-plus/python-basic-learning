## 多进程是指启动多个独立的进程，每个进程都有自己独立的 Python 解释器和内存空间，因此不受 GIL 限制，可以真正实现并行计算

import multiprocessing
import time

# 创建一个进程间安全的队列： 进程间通信
q = multiprocessing.Queue()

# 生产者进程
def producer(name):
    """生产者子进程"""
    for i in range(5):
        print(f"生产者{name}放入：{i}")
        q.put(i)
        time.sleep(1)

# 消费者进程
def consumer(name):
    """消费者子进程"""
    while True:
        item = q.get()
        if item is None:
            print("消费者{name}收到结束信号")
            break
        print(f"消费者取出：{item}")

if __name__ == "__main__":
    # 创建子进程
    p1 = multiprocessing.Process(target=producer, args=("Process-1",))
    p2 = multiprocessing.Process(target=consumer, args=("Process-2",))

    # 启动子进程
    p1.start()
    p2.start()

    # 等待子进程完成
    p1.join()
    q.put(None)  # 发送结束信号
    p2.join()

    print("所有进程执行完毕")


# 线程池 / 进程池
# 进程间通信（IPC）：Queue、Pipe、Manager	multiprocessing.Queue、Pipe、Manager

# 锁（Lock）保护共享资源，防止冲突	threading.Lock、multiprocessing.Lock