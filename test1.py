from PIL import Image,ImageDraw

from PIL import Image
 

 




image = Image.open("满月.png")
width = image.size[0]
height = image.size[1]
for i in range(0,width):#遍历所有长度的点
    for j in range(0,height):#遍历所有宽度的点
        r,g,b,a = image.getpixel((i,j))
        rgba = (r,g,b,a)
        if r == 255 and g ==255 and b ==255 and a == 255:
            image.putpixel((i,j),(255,255,255,0))
draw_table = ImageDraw.Draw(im=image,mode="RGBA")



image.show() # 直接显示图片

image.save('满月.png', 'PNG') # 保存在当前路径下，格式为PNG

image.close()
