from PIL import Image, ImageColor
from PIL import ImageDraw
import math
import time
import taichi as ti
ti.init()

sizewidth = 1000 # size of pictures in pixels
sizeheight = 1000 # size of pictures in pixels

image = Image.new("RGB", (sizewidth, sizeheight))
draw = ImageDraw.Draw(image)

@ti.func
def draw_grafic(x,y):
    draw.point((x, y), fill=ImageColor.getrgb("red"))

@ti.func
def mfunc(x,y):
    # formula of function
    return x**2 + y**2 - 2500

@ti.kernel
def calc():
    sizewidth = 1000 # size of pictures in pixels
    sizeheight = 1000 # size of pictures in pixels

    # real area of drawing
    xmin = -100
    xmax = 100
    xlen = abs((xmax-xmin) / sizewidth)
    ymin = -100
    ymax = 100
    ylen = abs((ymax-ymin) / sizeheight)

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

            if (f1 > 0 and f2 > 0 and f3 > 0 and f3 > 0) or (f1 < 0 and f2 < 0 and f3 < 0 and f3 < 0) :
                continue
            draw_grafic(x,y)

            f1 = f2
            f3 = f4

tic = time.perf_counter()
calc()
image.save("/home/dpanteleev/SomeStuff/mybox/func-drawer/empty.png", "PNG")
toc = time.perf_counter()
print(f"Execution time {toc - tic:0.4f} seconds")
