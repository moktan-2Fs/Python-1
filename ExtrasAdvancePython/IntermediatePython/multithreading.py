import threading as th
import time


def func1():
    for i in range(1000):
        print("ones")


def func2():
    for i in range(1000):
        print("twos")


ta = time.time()
th1 = th.Thread(target=func1)
th2 = th.Thread(target=func2)
th1.start()
th2.start()
th1.end()
th2.end()
# func1()
# func2()
th1.join()
th2.join()
# print('hello sagar')
sa = time.time()
print(sa-ta)
