import time
import NTTS
from PIL import Image
import random

def query(q, image_only, file_type=None):
    try:
        time.sleep(1)
        print_now(f"好的，我将为你{q}...")
        print_now("正在生成图片...")
        img = Image.open('./home/hide/output.jpeg')
        time.sleep(6)
        print_now("图片生成完成！")
        return img
    except IOError:
        print_now("抱歉，出错了，请您稍后重试")
        return None

def print_now(text, min_delay=0.1, max_delay=0.4):
    time.sleep(0.5)
    for character in text:
        print(character, end='', flush=True)
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
    print()

# print_now("抱歉，出错了，请您稍后重试。")
