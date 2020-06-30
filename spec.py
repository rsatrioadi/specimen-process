import sys
from PIL import Image

def brightness(R,G,B):
    return (0.2126*(R/255.0) + 0.7152*(G/255.0) + 0.0722*(B/255.0))

for fname in sys.argv[1:]:
    im1 = Image.open(fname)
    pixelMap = im1.load()

    im2 = Image.new("RGBA", im1.size)
    pixelsNew = im2.load()
    for i in range(im2.size[0]):
        for j in range(im2.size[1]):
            c = pixelMap[i,j]
            pixelsNew[i,j] = (0,0,0,int((1-brightness(c[0],c[1],c[2]))*255))
            
    im1.close()
    im2.save(fname+".out.png") 
    im2.close()
