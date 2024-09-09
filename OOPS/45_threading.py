from datetime import datetime
import threading
import time


def task1():
    print("Task 1 Started.")
    time.sleep(2)

def task2():
    print("Task 2 Started.")
    time.sleep(2)

def task3():
    print("Task 3 Started.")
    time.sleep(2)


t1 = datetime.now()

task1 = threading.Thread(target=task1)
task2 = threading.Thread(target=task2)
task3 = threading.Thread(target=task3)
task1.start()
task2.start()
task3.start()
t2 = datetime.now()

execution_time = t2 - t1
total_seconds = execution_time.total_seconds()
print(f"Execution time: {total_seconds} seconds.")