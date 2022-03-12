from PIL import Image, ImageColor
from PIL import ImageDraw
import math

def mfunc(x,y):
    return 50*math.cos(x)**2 + 50*math.sin(y)**3

sizewidth = 1000
sizeheight = 1000

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

xr = xmin
yr = ymin
f1 = mfunc(xr,yr)
f2 = mfunc(xr,yr + ylen)
f3 = mfunc(xr + xlen,yr)
f4 = mfunc(xr + xlen,yr + ylen)

for x in range(sizewidth):
    xr = xmin + x * xlen
    for y in range(sizeheight):
        yr = ymin + y * ylen

        f2 = mfunc(xr,yr + ylen)
        f4 = mfunc(xr + xlen,yr + ylen)

        if (f1 >= 0 and f2 >= 0 and f3 >= 0 and f3 >= 0) or (f1 <= 0 and f2 <= 0 and f3 <= 0 and f3 <= 0) :
            continue
        draw.point((x, y), fill=ImageColor.getrgb("red"))

        f1 = f2
        f3 = f4

image.save("/home/piligrim/SomeStuff/mybox/func-drawer/empty.png", "PNG")
