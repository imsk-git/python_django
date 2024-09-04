from tqdm import tqdm
import time

# Display a progress bar
for i in tqdm(range(100), desc="Processing"):
    time.sleep(0.1)
