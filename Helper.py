import time

def sleep_for(t):
    print("Halting execution for", t, "sec")
    time.sleep(t)
    print("Resuming script execution")