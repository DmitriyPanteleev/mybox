from PIL import Image, ImageColor
from PIL import ImageDraw
import math

def mfunc(x,y):
    return (x**2+y**2-320*math.cos(x))**2 - 1440*(x**2+y**2)

sizewidth = 4000
sizeheight = 4000

image = Image.new("RGB", (sizewidth, sizeheight))
draw = ImageDraw.Draw(image)

xmin = -100
xmax = 100
xlen = (xmax-xmin) / sizewidth
xlen = max(xlen,-xlen)
ymin = -100
ymax = 100
ylen = (ymax-ymin) / sizeheight
ylen = max(ylen,-ylen)

for x in range(sizewidth):
    xr = xmin + x * xlen
    for y in range(sizeheight):
        yr = ymin + y * ylen

        f1 = mfunc(xr,yr)
        f2 = mfunc(xr,yr + ylen)
        f3 = mfunc(xr + xlen,yr)
        f4 = mfunc(xr + xlen,yr + ylen)

        if (f1 >= 0 and f2 >= 0 and f3 >= 0 and f3 >= 0) or (f1 <= 0 and f2 <= 0 and f3 <= 0 and f3 <= 0) :
            continue
        draw.point((x, y), fill=ImageColor.getrgb("red"))

image.save("/home/dpanteleev/SomeStuff/simpleDraw/empty.png", "PNG")
