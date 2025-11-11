from time import sleep, time 
from threading import Thread

start_time = time()

def download_img(url):
    sleep(1)
    print(f"{url} download completed")

# for i in range(5):
#     ## single thread execution
#     # download_img(f"{i}")

#     ## multi thread execution
#     thread = threading.Thread(target=download_img, args=(f"{i}",))
#     thread.start()

t1 = Thread(target = download_img, args=("https://google.com",))
t2 = Thread(target = download_img, args=("https://google.com",))
t3 = Thread(target = download_img, args=("https://google.com",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_time = time()

print(f"Elapsed time: {end_time - start_time:.2f}s")