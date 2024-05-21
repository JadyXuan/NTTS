import rag
import NTTS
from PIL import Image

def read_image():
    q = input(">> ")
    ret = rag.query(q, image_only=True, file_type="JPEG")
    # 将输出保存到本地文件
    ret.write('./home/demo/output.jpeg')
    
read_image()
