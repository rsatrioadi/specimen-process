import sys
import os
from PIL import Image

x = int(sys.argv[1])
y = int(sys.argv[2])

for fname in sys.argv[3:]:
    im1 = Image.open(fname)
    pixelMap = im1.load()

    imin = 0
    imax = im1.size[0] - 1
    jmin = 0
    jmax = im1.size[1] - 1
    for i in range(im1.size[0]):
        for j in range(im1.size[1]):
            t = pixelMap[i, j][3]
            if t > 100:
                imin = max(imin, i - 1)
                break
        else:
            continue
        break
    for i in reversed(range(im1.size[0])):
        for j in range(im1.size[1]):
            t = pixelMap[i, j][3]
            if t > 100:
                imax = min(imax, i + 1)
                break
        else:
            continue
        break
    for j in range(im1.size[1]):
        for i in range(im1.size[0]):
            t = pixelMap[i, j][3]
            if t > 100:
                jmin = max(jmin, j - 1)
                break
        else:
            continue
        break
    for j in reversed(range(im1.size[1])):
        for i in range(im1.size[0]):
            t = pixelMap[i, j][3]
            if t > 100:
                jmax = min(jmax, j + 1)
                break
        else:
            continue
        break

    im1 = im1.crop((imin, jmin, imax, jmax))

    im1.thumbnail((x,y), Image.ANTIALIAS)
    im2 = Image.new(im1.mode, (x, y))
    x1 = (x-im1.width)//2
    y1 = (y-im1.height)//2
    im2.paste(im1, (x1, y1, x1 + im1.width, y1 + im1.height))
    im1.close()
    im2.save(os.path.splitext(fname)[0]+".rsz.png")
    im2.close()
