from datetime import datetime
import requests
from tqdm import tqdm

image_data = [
    "https://www.shopify.com/stock-photos",
    "https://www.shutterstock.com/photos",
    "https://www.shopify.com/stock-photos",
    "https://www.istockphoto.com/stock-photos",
    "https://www.istockphoto.com/stock-photos",
    "https://www.istockphoto.com/stock-photos",
]


t1 = datetime.now()
def get_suffix(index):
    if index == 1:
        return "st"
    elif index == 2:
        return "nd"
    elif index == 3:
        return "rd"
    else:
        return "th"
    

i = 0
for img_url in image_data:
    i += 1
    index = get_suffix(i)
    data = requests.get(img_url)
    
    with open(f"{i}.png","wb") as f:
        with tqdm(desc=f"\nDownloading {i}{index} image.") as fp:
            f.write(data.content)
    print(f"{i}{index} Image Downloaded!\n")
    

t2 = datetime.now()
execution_time = t2 - t1
total_seconds = execution_time.total_seconds()
print(f"Execution time: {total_seconds} seconds.\n")


