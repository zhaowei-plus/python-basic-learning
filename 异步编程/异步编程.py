import asyncio

# 协程间通信（异步队列，用于 asyncio 协程）
queue = asyncio.Queue()

async def producer(name):
    for i in range(5):
        print(f"生产者{name}放入：{i}")
        await queue.put(i)  # 异步放入
        await asyncio.sleep(0.5)

async def consumer(name):
    while True:
        item = await queue.get()  # 异步获取
        if item is None:
            print(f"消费者{name}收到结束信号")
            break
        print(f"消费者{name}取出：{item}")
        queue.task_done()


#### asyncio.Semaphore/asyncio.gather
######################### asyncio.Semaphore #####################################

# Semaphore 是 asyncio 提供的一个信号量（Semaphore）对象，用于限制同时访问某一资源的协程储量
# 并发控制器，设置最大并发数，那么同时最多只能有 5 个协程运行，其他协程必须等待，直到有“名额”空出来
async def task(semaphore, id):
    async with semaphore:  # 表示进入时，自动获取信号量
        print(f"🔥 任务 {id} 开始")
        await asyncio.sleep(2)  # 模拟耗时操作(异步，不会阻塞事件循环，让控制权，让其他协程可以运行), TODO: 注意与 time.sleep(2)(同步，会阻塞代码执行，在异步环境中切勿使用) 的区别
        print(f"✅ 任务 {id} 结束")
        return {"id": id}


async def run():
    # 场景：如当有10个请求，但是为了控制并发量，仅允许最多同时发起5个请求，避免服务器压力过大或被封，可以使用信号量设置并发请求数量
    # 设置最多允许 3 个协程同时进入临界区
    semaphore = asyncio.Semaphore(3)  # 允许设定的 3 个并发
    tasks = [task(semaphore, i) for i in range(10)]
    res = await asyncio.gather(*tasks)
    # asyncio.wait
    # asyncio.wait_for 为单个协程设置超时，超时未完成则抛 TimeoutError
    print("res:", res)

    # 创建子协程任务，并发运行：asyncio.create_task 在一个协程中创建并调度一个“子协程”
    prod_task = asyncio.create_task(producer("Coroutine-1"))
    cons_task = asyncio.create_task(consumer("Coroutine-1"))

    print("🟡 主协程继续执行，没有等待子协程")

    # 等待子协程完成（await）
    await prod_task
    await queue.put(None)  # 发送结束信号
    await cons_task

    print("主协程结束")

if __name__ == '__main__':
    asyncio.run(run())  # asyncio.run 方法，运行一个协程
