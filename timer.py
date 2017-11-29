#timer
import time
from datetime import timedelta
start_time = time.monotonic()
#do stuff here
end_time = time.monotonic()
timer_print = "Timer: ",timedelta(seconds=end_time-start_time)