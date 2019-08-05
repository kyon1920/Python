# 进程、队列、多进程、线程、进程间通信、互斥锁

# 进程
# 什么是进程？进程就是计算机中已运行程序的实体
# 但是，进程 != 程序
# 在Python中通过调用相应Python进程模块去操纵OS中的进程

# 创建进程的几种方式
# 调用os.fork()函数
# os.fork()不支持Windows系统，只支持Linux和类Linux系统

# 使用multiprocessing模块Process创建进程
# Process([group[,target[,name[,args[,kwargs]]]]])
# 参数详解如下：
# group：参数未使用，值始终为None
# target：表示当前进程启动时执行的可调用对象
# name：为当前进程实例的别名
# args：表示传递给target函数的参数元组
# kwargs：表示传递给target函数的参数字典
# 创建进程示例：
from multiprocessing import Process
import time

def test(intervel):
    time.sleep(intervel)
    print('我是子进程')
def main():
    print('主进程开始')
    p = Process(target=test,args=(1,))
    p.start()
    print('主进程结束')

if __name__ == '__main__':
    main()
# 结果分析见下图

# Process类的常用方法和属性
# js_alive()：判断进程实例是否还在执行
# join([timeout])：是否等待进程实例执行结束，或等待多少秒
# start()：启动进程实例(创建子进程)
# run()：如果没有给定target参数，对这个对象调用start()方法时，
# 就将执行对象中的run()方法
# terminate()：不管任务是否完成，立即终止
# name：当前进程实例别名，默认为Process-N，N为从1开始递增的整数
# pid：当前进程实例的PID值
# 实例：使用Process子类创建2个子进程，并记录子进程运行时间
from multiprocessing import Process
import time
import os

def child_1(intervel):
    # getpid()获取进程id，getppid()获取它的父进程的id
    print('子进程(%s)开始执行，它的父进程是(%s)' %(os.getpid(),os.getppid()))
    t_start = time.time()
    time.sleep(intervel)
    t_end = time.time()
    print('子进程(%s)执行时间为(%0.2f)' % (os.getpid(),t_end-t_start))
def child_2(intervel): 
    print('子进程(%s)开始执行，它的父进程是(%s)' % (os.getpid(),os.getppid()))
    t_start = time.time()
    time.sleep(intervel)
    t_end = time.time()
    print('子进程(%s)执行时间为(%0.2f)' % (os.getpid(),t_end-t_start))

def main():
    print('主进程开始')
    print('主进程的PID：(%s)' % os.getpid())
    p1 = Process(target=child_1,args=(1,))
    p2 = Process(target=child_2,name='Navi',args=(2,))
    p1.start()
    p2.start()
    print('p1.is_alive=%s' % p1.is_alive())
    print('p2.is_alive=%s' % p2.is_alive())
    print('p1.name=%s' % p1.name,'p1.id=%s' % p1.pid)
    print('p2.name=%s' % p2.name,'p2.id=%s' % p2.pid)
    p1.join()
    p2.join()
    print('主进程结束')

if __name__ == '__main__':
    main()
# 运行结果
# 主进程开始
# 主进程的PID：(18416)
# p1.is_alive=True
# p2.is_alive=True
# p1.name=Process-1 p1.id=12672
# p2.name=Navi p2.id=15064
# 子进程(12672)开始执行，它的父进程是(18416)
# 子进程(12672)执行时间为(1.00)
# 子进程(15064)开始执行，它的父进程是(18416)
# 子进程(15064)执行时间为(2.00)
# 主进程结束
# [Finished in 2.8s]

# 使用Process子类创建进程
# 像前面的创建进程的方法，每创建一个进程都要使用Process类
# 如果要同时创建多个子进程的就会比较麻烦
# 子类都继承自Process类就相当于创建了进程
# 实例：使用Process子类创建2个子进程，并记录子进程运行时间
class SubProcess(Process):
    def __init__(self,intervel,name=''):
    	super(SubProcess,self).__init__()    # 也可这样写Process.__init__(self)
    	self.intervel = intervel
    	if name :
    		self.name = name
    def run(self):
    	# getpid()获取进程id，getppid()获取它的父进程的id
        print('子进程(%s)开始执行，它的父进程是(%s)' %(os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.intervel)
        t_end = time.time()
        print('子进程(%s)执行时间为(%0.2f)' % (os.getpid(),t_end-t_start))

def main():
    print('主进程开始')
    print('主进程的PID：(%s)' % os.getpid())
    p1 = SubProcess(intervel=1,name='Navi')
    p2 = SubProcess(intervel=2)
    p1.start()
    p2.start()
    print('p1.is_alive=%s' % p1.is_alive())
    print('p2.is_alive=%s' % p2.is_alive())
    print('p1.name=%s' % p1.name,'p1.id=%s' % p1.pid)
    print('p2.name=%s' % p2.name,'p2.id=%s' % p2.pid)
    p1.join()
    p2.join()
    print('主进程结束')

if __name__ == '__main__':
    main()
# 值得注意的是：在实例化对象时，并没有指定执行函数
# run()方法是进程运行时可执行的方法
# 而start()是进程执行的方法，调用该方法时会自动调用run()方法

# 使用进程池Pool创建进程
# 当创建进程较多的时候，需要实例化很多类，会占有较多资源
# 进程池Pool可以解决这样问题
# Pool类的常用方法
# apply_async(func[,args[,kwds]])：使用非阻塞方式调用func函数(并行执行，
# 堵塞方式必须等待上一个进程退出才能执行下一个进程)，args为传递给func的参数
# 传递列表，kwds为传递给func的关键字参数列表
# apply(func[,args[,kwds]])：使用阻塞方式调用func函数
# close()：关闭Pool，使其不再接收新的任务
# terminate()：不管任务是否完成，立即终止
# join()：主进程阻塞，等待子进程的退出，必须在close或terminate之后使用
# 阻塞和非阻塞：阻塞就是顺序执行，非阻塞就是多个任务并行
# 实例：使用进程池创建进程
from multiprocessing import Pool
import os
import time
def task(name):
    print('子进程(%s) 执行任务%s ' % (os.getpid(),name)
    time.sleep(1)
if __name__ == '__mian__':
    print('父进程(%s)' % os.getpid())
    p = Pool(3)
    for i in range(10):
	p.apply_async(task,args=(i,))
    p.close()
    p.join()    # join()方法必须在close()方法后面使用
    print('所有子进程结束')

# 进程间通信
# 主进程和子进程之间不能进行直接通信
# 因为每个进程都有自己的地址空间、内存、数据栈以及记录其状态的普通数据

# 如果要实现进程间通信，需要借助其它方法
# 队列、管道：下面就探究一下由队列实现的进程间通信


# 什么是队列：先进先出，即FIFO模型
# 多进程队列的使用
# Queue类常用操作
# 插入数据put()、取出数据get()、判空empty()、判满full()、数量qsize()
# Queue类的常用方法
# Queue.qsize()：返回当前队列包含的消息数量
# Queue.empty()：如果队列为空，返回True，否则返回False
# Queue.full()：如果队列满了，返回True，否则返回False
# Queue.get([block[,timeout]])：获取队列中的一条消息，然后将从队列中移除
# block的默认值为True
# Queue.get_nowait()：相当Queue.get(False)
# Queue.put(item,[block[,timeout]])：将item消息写入队列，block默认值True
# Queue.put_nowait(item)：相当Queue.put(item,False)
# 队列示例：
from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)
    q.put('消息1')
    q.put('消息2')
    print('队列是否已满：%s' % q.full())
    q.put('消息3')
    print('队列是否已满：%s' % q.full())

    try:
        q.put('消息4',True,2)
    except:
        print('消息队列已满，现在消息数量%s' % q.qsize())
    try:
        q.putnowait('消息4')
    except:
        print('消息队列以满，现在消息数量%s' % q.qsize())

    if not q.empty():
        print('--从队列中取出消息--')
        for i in range(q.qsize()):
            print(q.get_nowait())
    if not q.full():
        q.put('消息4')
        print(q.qsize())

# 使用队列在进程间通信
# 分别向队列中写入和读取数据
from multiprocessing import Process,Queue
import time

def write_task():
    if not q.full():
        for i in range(5):
            message = '消息' + str(i)
            q.put(message)
            print('写入：%s' % message)
def read_task():
    time.sleep(1)
    while not q.empty():
        print('读取：%s' % q.get(True,2))

if __name__ == '__main__':
    print('--主进程开始--')
    pw = Process(target=write_task)
    pr = Process(target=read_task)
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('--主进程结束--')

# 线程
# 什么是线程？
# 操作系统能够进行运算调度的最小单位
# 它被包含在进程之中，是进程中的实际运作单位
# 一个线程指的是进程中单一顺序的控制流
# 在一个进程中可以并发多个线程，每个线程可以执行多个任务
# CPU在每一个线程之间以时间片的形式执行
# 由于CPU处理速度非常快，使得每个线程好像在同时运行一样
# 线程的特点：
# 1、进程是资源分配的最小单位，线程是最小的执行单位
# 2、一个进程可以有多个线程
# 3、线程可以共享进程资源
# 进程与线程的关系
# 进程相当于一个容器，它不去执行操作，线程来执行不同的任务

# 创建线程的几种方式
# threading模块Thread类创建线程
# 语法及参数
# Thread([group[,target[,name[,args[,kwargs]]]]])
# group：参数未使用，始终为None
# target：表示当前线程启动时执行的可调用对象
# name：为当前线程实例的别名
# args：表示传递给target函数的参数元组
# kwargs：表示传递给target函数的参数字典
# 示例：
import threading
import time

def thread():
    for i in range(3):
        time.sleep(3)
        print('thread name is %s' % threading.current_thread().name)

if __name__ == '__main__':
    print('--主线程开始--')
    threads = [threading.Thread(target=thread) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('--主进程结束--')

# 使用Thread子类创建线程
# 实例：使用Thread子类创建线程
from threading import Thread
import time

class SubThread(Thread):    # 创建Thread子类
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = '子线程' + self.name + '执行，i='+ str(i)
            print(msg)

if __name__ == '__main__':
    print('--主线程开始--')
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('--主线程结束--')
# 与Process子类创建子进程进行比较
# Process子类使用了初始化方法和run()方法
# 而Thread子类只使用了run()方法
# 因为在线程创建的时候没有加参数，不用为Thread类初始化
# 而在创建进程时加了参数，需要调用Process类的初始化方法来接收参数

# 线程间通信
# 进程之间不能直接进行通信，而是要通过队列或者管道的中间桥梁才能通信
# 而线程间是可以直接进行通信的
# 代码测试
from threading import Thread

def plus():
    print('--子线程1开始--')
    global g_num
    g_num += 50
    print('g_num is %d' % g_num)
    print('--子线程1结束--')

def minus():
    print('--子线程2开始--')
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    print('--子线程2结束--')

g_num = 100

if __name__ == '__main__':
    print('--主线程开始--')
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('g_num is %d' % g_num)
    print('--主线程结束--')
# 最终结果及步骤结果都正确

# 但是设想一下，会发现，多个线程同时操作同一个全局变量时就会发生混乱
# 上诉就为不安全线程
# 为了实现安全的线程：给线程加锁、解锁来现象(threading.Lock())

# 互斥锁
# 防止多个线程同时读取某一内存的区域
# 互斥锁给资源引入一个状态，要么锁定，要么非锁定
# 当线程需要对某一资源进行操作时，就将其设定为锁定，其它线程不可操作
# 操作结束后解锁定，此时其它线程才可以对该资源进行操作并锁定

# 互斥锁的使用
# 步骤
# 创建锁：mutex = threading.Lock()
# 锁定：mutex.acquire([blocking])
# 释放锁：mutex.release()

# 实例：使用互斥锁实现多人同时订购电影票功能
from threading import Thread,Lock
import time

n = 100

def task():
    global n
    mutex.acquire()
    time.sleep(0.1)
    n -= 1
    print('购买成功，剩余%d张电影票' % n)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(10):
        t = Thread(target=task)
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()
# 结果正确
# 但是需要注意一个问题
# 死锁(发生概率小)：所有线程都在等待

# 使用队列在线程间通信
# 通常用于生产者与消费者之间的关系
# 产生数据的模块称为生产者，处理数据的模块称为消费者
# 在生产者和消费者之间有一个缓冲区，称为仓库
# 使用队列模拟生产者消费者模式
from queue import Queue
from threading import Thread
import time
import random

class Producer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.data = queue
    def run(self):
        for i in range(5):
            print('生产者%s将产品%d加入队列' % (self.getName(),i))
            self.data.put(i)
            time.sleep(random.random())
        print('生产者%s完成！' % (self.getName()))

class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.data = queue
    def run(self):
        for i in range(5):
            val = self.data.get()
            print('消费者%s将产品%d从队列中取出'% (self.getName(),val))
            time.sleep(random.random())
        print('消费者完成！')

if __name__ == '__main__':
    print('--主线程开始--')
    queue = Queue()
    producer = Producer('Producer',queue)
    consumer = Consumer('Consumer',queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('--主线程结束--')
# 结果为生产者和消费者的执行顺序是随机的
