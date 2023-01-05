from settings import TIME_INIT
import time


def measure_time():
    Time_now = time.perf_counter()
    return round(Time_now - TIME_INIT, 1)
