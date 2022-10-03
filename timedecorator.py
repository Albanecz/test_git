from datetime import (datetime,)
import time 
import random

def timer(fn):
    def check_time(*args, **kwargs):
        fn(*args, **kwargs)
        print(f"\n\t[Log] функция {fn.__name__} завершилась в  - {datetime.now()}")
    return check_time

@timer
def say_hello():
    print("hello world")
