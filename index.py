from PIL import Image

im = Image.open("image.jpg")

im2 = Image.new( 'RGB',im.size, 0)


width = im.size[0]
height = im.size[1]
rgb_im = im.convert("RGB")

threshHeight = round(height / 20)
threshWidth = round(width / 20)


pixels_old = im.load()
pixels_new = im2.load()


for i in range(im.size[0]):    # for every pixel:
    for j in range(im.size[1]):
        pixel = pixels_old[i,j]
        if (i / threshWidth) % 2 < 1:
            pixels_new[i,j] = (pixel[0], 0, 0)
        else :
            pixels_new[i,j] = (0, pixel[1], 0)
         # set the colour accordingly

im2.show()

im2.save("imagergb.jpg")