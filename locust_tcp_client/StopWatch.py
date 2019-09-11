import inspect
import random
import time

from locust import events

def timer(func):
    def timer_wrapper(*args, **kwargs):
        previous_frame = inspect.currentframe().f_back
        filename, line_number, function_name, lines, index = inspect.getframeinfo(previous_frame)
        start_time = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="TCP", name=func.__name__,response_time=total_time, response_length=0, tag=function_name)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="TCP", name=func.__name__,response_time=total_time, exception=e, tag=function_name)

        return result
    return timer_wrapper
