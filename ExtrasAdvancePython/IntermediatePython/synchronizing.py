import threading as th
import time as ti

# x = 8192
# lock = th.Lock()


# def doub_le():
#     global x, lock
#     with lock:
#         while x < 16384:
#             x *= 2
#             print(x)
#             ti.sleep(1)
#         print("reached the maximum!")

# def halve():
#     global x, lock
#     with lock:
#         while x > 1:
#             x /= 2
#             print(x)
#             ti.sleep(1)
#             if x == 1:
#                 print("minimum reached!")

# thre1 = th.Thread(target=doub_le)
# thre2 = th.Thread(target=halve)

# thre1.start()
# thre2.start()

# semaphore = th.BoundedSemaphore(value=5) # limit the access to the resources

# def access(thread_number):
#     print(f"{thread_number} is trying to access.")
#     semaphore.acquire()
#     print(f"{thread_number} was granted acccess.")
#     ti.sleep(10)
#     print(f"{thread_number} is now relasing.")
#     semaphore.release()

# for thread_number in range(1,11):
#     t = th.Thread(target= access, args= (thread_number,))
#     t.start()
#     ti.sleep(2)

def math_cal(a, b):
    print("calculating..")
    ti.sleep(3)
    print(f"Result: {a*b}")


def add__num(a, b):
    print("calculating...")
    ti.sleep(3)
    print(f"result: {a+b}")


thread1 = th.Thread(target=math_cal, args=(5, 5))
thread2 = th.Thread(target=add__num, args=(10, 10))
lock = th.Lock()

with lock:
    thread1.start()

with lock:
    thread2.start()

thread1.join()
thread2.join()

print("Task finished")
