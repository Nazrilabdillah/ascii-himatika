
import time
import random

def rand_color_frame(frame,index):
    ar = [[random.randint(31,37) for i in range(6)] for _ in range(8)]
    rep = ['B',"@",'i','?','#','%']
    for i in range(len(rep)):
       frame = frame.replace(rep[i],f"\033[1;{ar[index][i]}m{rep[i]}\033[0m")
    return frame

async def generate_himatika_ascii(fr:str):
    while True:
      ran_num = random.randint(0,7)
      frame = rand_color_frame(fr,ran_num)
      yield f"{frame}\n"
      time.sleep(5)     

    
async def generate_bird_ascii(list_dir):
    while True:
        for frame in list_dir:
            ran_num = random.randint(0,7)
            yield f"{rand_color_frame(frame,ran_num)}\n"
            time.sleep(0.2)  # jeda antar frame


