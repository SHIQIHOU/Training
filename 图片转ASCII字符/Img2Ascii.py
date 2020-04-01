from PIL import Image

#载入图像
img = Image.open('b.png')

#灰度图
out = img.convert('L')

#缩放，由于字符的高度是宽度的两倍左右，所以高度需要再乘上0.5
width, height = out.size
out = out.resize((int(width * 0.5), int(height * 0.5 * 0.5)))
width, height = out.size

#将每一个像素点按照灰度值转换为对应的字符
asciis = "@%#*+=-. "
texts = ""
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        texts += asciis[int(gray / 255 * 8)]
    texts += "\n"

#保存成txt文件
with open('test.txt', 'w') as file:
    file.write(texts)
