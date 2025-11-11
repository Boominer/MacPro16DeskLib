from time import sleep, time 
from concurrent import futures

start_time = time()

def download_img(url):
    sleep(1)
    print(f"{url} download completed")


with futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(download_img, range(10))

end_time = time()

print(f"Elapsed time: {end_time - start_time:.2f}s")