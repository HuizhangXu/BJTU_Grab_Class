# encoding=utf-8
from PIL import Image
import pytesseract
# from pytesser import *
def capcha():
    img = Image.open('code.png')
    img_grey = img.convert('L')
    #img_grey.show()
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img_out = img_grey.point(table, '1')

    text = pytesseract.image_to_string(img_grey)  # 将图片转成字符串
    ###pytesseract验证通过率好像不高，可以试试用百度的
    return text