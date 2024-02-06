from concurrent.futures.thread import ThreadPoolExecutor
import random
import time

def A(x):
    for i in range(x):
        sleep_time = random.randint(i, i*2)
        print(f"{__name__}A Sleeping for {sleep_time} secs")
        time.sleep(sleep_time)
def B(x):
    for i in range(x):
        sleep_time = random.randint(i, i*5)
        print(f"{__name__}B Sleeping for {sleep_time} secs")
        time.sleep(sleep_time)

executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(A, 2)
b = executor.submit(B, 5)

