

from datetime import datetime
import threading
import requests


image_data = [
    "https://www.shopify.com/stock-photos",
    "https://www.shutterstock.com/photos",
    "https://www.shopify.com/stock-photos",
    "https://www.istockphoto.com/stock-photos",
    "https://www.istockphoto.com/stock-photos",
    "https://www.istockphoto.com/stock-photos",
]

t1 = datetime.now()
threads = []

# i = 0
# for img_urls in image_data:
#     i += 1
def img_urls(i):
    data = requests.get(img_urls)
    with open(f"{i}.png","wb") as f:
        f.write(data.content)

 
image_data = threading.Thread(target=img_urls)
threads.append(image_data)
image_data.start()
image_data.join()

t2 = datetime.now()
execution_time = t2 - t1
total_seconds = execution_time.total_seconds()
print(f"Execution time: {total_seconds} seconds.")