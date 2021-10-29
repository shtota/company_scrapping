import subprocess
from sys import argv, executable
import time

if len(argv) == 2:
    start_chunk = int(argv[-1])
    end_chunk = start_chunk+1
elif len(argv) == 3:
    start_chunk = int(argv[-2])
    end_chunk = int(argv[-1]) + 1
else:
    print('Provide start chunk or start and end chunks as arguments')
    print(len(argv), argv)
    raise NotImplementedError

for i in range(start_chunk, end_chunk):
    subprocess.run([executable, "gospider.py", str(i)])
    time.sleep(10)