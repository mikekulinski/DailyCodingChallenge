#TODO figure out what this should actually do

import time

def job_scheduler(f, n):
    n_in_seconds = n / 1000
    time.sleep(n_in_seconds)
    f()

def func1():
    print(sum([i for i in range(20)]))

def func2():
    print(sum([i for i in range(1000)]))



if __name__ == "__main__":
    job_scheduler(func1, 1000)
    job_scheduler(func2, 5000)