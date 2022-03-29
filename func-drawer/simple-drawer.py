from PIL import Image, ImageColor
from PIL import ImageDraw
import math

sizewidth = 1000 # size of pictures in pixels
sizeheight = 1000 # size of pictures in pixels
formule = "x**2 + y**2 - 2500" # formula of function
exec_string = formule

# real area of drawing
xmin = -100
xmax = 100
xlen = abs((xmax-xmin) / sizewidth)
ymin = -100
ymax = 100
ylen = abs((ymax-ymin) / sizeheight)

def mfunc(x,y,exec_formule):
    return eval(exec_formule)

image = Image.new("RGB", (sizewidth, sizeheight))
draw = ImageDraw.Draw(image)

xr = xmin
yr = ymin
f1 = mfunc(xr,yr,exec_string)
f2 = mfunc(xr,yr + ylen,exec_string)
f3 = mfunc(xr + xlen,yr,exec_string)
f4 = mfunc(xr + xlen,yr + ylen,exec_string)

for x in range(sizewidth):
    xr = xmin + x * xlen
    for y in range(sizeheight):
        yr = ymin + y * ylen

        f2 = mfunc(xr,yr + ylen,exec_string)
        f4 = mfunc(xr + xlen,yr + ylen,exec_string)

        if (f1 > 0 and f2 > 0 and f3 > 0 and f3 > 0) or (f1 < 0 and f2 < 0 and f3 < 0 and f3 < 0) :
            continue
        draw.point((x, y), fill=ImageColor.getrgb("red"))

        f1 = f2
        f3 = f4

image.save("/home/dpanteleev/SomeStuff/mybox/func-drawer/empty.png", "PNG")
