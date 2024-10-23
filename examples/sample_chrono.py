import time
from chronowatch import Stopwatch

stopwatch = Stopwatch('Building it')
stopwatch.start("Preparing files")
time.sleep(3.0)
stopwatch.stop()
print(stopwatch.last_task_info())
# TaskInfo(task_name='Preparing files', time_nanos=3009159300)

stopwatch.start("Processing files")
time.sleep(2.0)
stopwatch.stop()

print(stopwatch.pretty_print())
# StopWatch 'Building it': 5.013895300 seconds
# ---------------------------------------------
# Seconds         %         Task name
# ---------------------------------------------
# 3.009159300     60%       Preparing files
# 2.004736000     40%       Processing files
