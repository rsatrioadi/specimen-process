import sys
import os
from PIL import Image

x = int(sys.argv[1])
y = int(sys.argv[2])

for fname in sys.argv[3:]:
    im1 = Image.open(fname)
    im2 = Image.new(im1.mode, (x, y))
    x1 = (x-im1.width)//2
    y1 = (y-im1.height)//2
    im2.paste(im1, (x1, y1, x1 + im1.width, y1 + im1.height))
    im1.close()
    im2.save(os.path.splitext(fname)[0]+".rsz.png")
    im2.close()
