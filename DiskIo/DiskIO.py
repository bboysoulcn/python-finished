from psutil import disk_io_counters
from time import sleep
from os import system

try:
    while True:
        t1 = disk_io_counters()
        sleep(1)
        system("clear")
        t2 = disk_io_counters()
        read_bytes =  t2.read_bytes - t1.read_bytes
        read_bytes = read_bytes / 1024 / 1024
        write_bytes = t2.write_bytes - t1.write_bytes
        write_bytes = write_bytes / 1024 / 1024
        print('read:{}M/S'.format(read_bytes))
        print('write:{}M/S'.format(write_bytes))
except KeyboardInterrupt:
    print("By Bboysoul")