import psutil
import time

cpu_core = psutil.cpu_count(logical=False)
cpu_thread = psutil.cpu_count()
print("cpu核心数：" + str(cpu_core))
print("cpu线程数：" + str(cpu_thread))
while True:
    print(time.time())
    cpu_ratio = psutil.cpu_percent()   # 查看cpu利用率
    cpu_percent = psutil.cpu_percent(percpu=True)   
    time.sleep(5)
    print("cpu利用率：" + str(cpu_ratio))
    print("单核心利用率" + str(cpu_percent))
    memorey = psutil.virtual_memory()  # 以命名元组的形式返回内存使用情况，包括总内存，可用内存，内存利用率，buffer和cache等。单位为字节。
    print("内存：" + str(memorey))