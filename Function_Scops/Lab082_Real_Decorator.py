import time

from Function_Scops.Lab081_Without_Decore import start

def time_decorator(func):
    def wrapper():
            start_time = time.time()
            print(start_time)
            func()
            end_time = time.time()
            print(end_time)
            print("Total time taken by function",end_time - start_time)

        return wrapper()

def print_logs(func):
    def wrapper():
        print("starting log")
        func()
        print("Ending log")

        return wrapper()

@time_decorator
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)