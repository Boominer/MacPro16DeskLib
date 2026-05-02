from time import sleep, time 
from threading import Thread

"""
Url: https://www.bilibili.com/video/BV1tVsyzUEtX?spm_id_from=333.788.videopod.sections&vd_source=3e0ea0bcb977cb8d47f4451ff8c0e242
主线程 与 子线程?

CPU密集形任务 - 多线程
IO密集形 - 多携程

GIL - global interper law 

1. 多线程可以让程序开始多个任务，CPU可以在他们之间交替执行，缩短运行时间
2. 通过python threading 我们可以管理线程，但是更省力的是用concurrent，线程池
3. 

"""
