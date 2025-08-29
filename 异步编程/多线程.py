## 多线程（Threading）
## 多个线程运行在同一个进程内，线程之间共享内存，通信简单但要注意线程安全

import threading
import time
import queue

# 创建一个线程安全的队列：线程间通信
q = queue.Queue()

# 生产者线程：往队列中放数据
def producer(name):
    """生产者子线程"""
    for i in range(5):
        print(f"生产者{name}放入：{i}")
        q.put(i)  # 阻塞方法，队列满时会等待
        time.sleep(0.5)


# 消费者线程：从队列中取数据
def consumer(name):
    """消费者子线程"""
    while True:
        item = q.get()  # 阻塞方法，队列空时会等待
        if item is None:  # 哨兵值，表示结束
            print(f"消费者{name}收到结束信号")
            break
        print(f"消费者取出：{item}")
        q.task_done()  # 通知队列，这个任务处理完了

if __name__ == "__main__":
    # 创建子线程
    t1 = threading.Thread(target=producer, args=("Thread-1",))
    t2 = threading.Thread(target=consumer, args=("Thread-1",))

    # 启动子线程
    t1.start()
    t2.start()

    # 等待子线程完成
    t1.join()
    q.put(None)  # 发送结束信号 q.put(item)/q.get()/q.join()/q.empty()/q.full()
    t2.join()

    print("主线程结束")


# 线程池 / 进程池
# 线程间通信：queue.Queue(线程安全) threading + queue

# 锁（Lock）保护共享资源，防止冲突	threading.Lock、multiprocessing.Lock