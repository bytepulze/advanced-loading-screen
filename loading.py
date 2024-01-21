# ethfavcoin.xyz
import time
import os
from tqdm import tqdm
import random
from alive_progress import alive_bar; import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('alive_progress')

os.system('cls')


my_list = ['LibWireTap.dll', 'randomint.dll', 'vcomp100.dll', 'vectormath.dll', 'imagedisplay_lib.dll', 'ac1st17.dll', 'acdb17.dll', 'aclua.dll']
slow_list = ['LibWireTap.dll']


print("Welcome to the bomba")
option = input("1. Start Downloading\n\n")

if option == "1":
    print("Starting Download")
    pass
elif option == "2":
    os.system('cls')
    print("V0.3")
    print("ethfavcoin.xyz")
    exit()
os.system('cls')
with alive_bar(total=len(my_list), theme='classic') as bar:
    for s in my_list:
        wait_time = random.uniform(0.5, 1)
        if s in slow_list:
            wait_time = wait_time * random.uniform(1, 8)
        bar.text = f"Working on {s}..."
        time.sleep(wait_time)
        bar()
