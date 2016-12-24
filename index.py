from PIL import Image
import os
import re
import threading
 
def split_list(a_list):
    half = int(len(a_list)/2)
    return a_list[:half], a_list[half:]
def transform_images(imageList):
    print("Transforming",imageList)
    for file in imageList:
        im = Image.open(file)
        #im2 = Image.new( 'RGB',im.size, 0)


        width = im.size[0]
        height = im.size[1]
        rgb_im = im.convert("RGB")

        threshHeight = round(height / 20)
        threshWidth = round(width / 20)


        pixels_old = im.load()
        pixels_new = []
        #pixels_new = im2.load()

        print("Transforming ", file)
        for i in range(im.size[0]):    # for every pixel:
            for j in range(im.size[1]):
                pixel = list(pixels_old[i,j])
                pixel[2] = 0
                if (i / threshWidth) % 2  < 1:
                    if (j / threshHeight) % 2 < 1:
                        pixel[1] = 0
                        #pixels_new[i,j] = (pixel[0], 0, 0)
                    else:
                        pixel[0] = 0
                        #pixels_new[i,j] = (0, pixel[1], 0)
                    
                else :
                    if (j / threshHeight) % 2 < 1:
                        pixel[0] = 0
                        #pixels_new[i,j] = (0, pixel[1], 0)
                    else:
                        pixel[1] = 0
                        #pixels_new[i,j] = (pixel[0], 0, 0)
                # set the colour accordingly
                pixels_new.append(pixel)
        #im2.save("output/rg_" + file)
        im.paste(pixels_new)
        im.save("output/rg_" + file)
        print("Success")

fileEnding = "\.png$|\.jpg$|\.jpeg$"
#fileEnding = "\.jpg"
images = []

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if re.search(fileEnding, str.lower(f)) != None :
        images.append(f)

f1,f2 = split_list(images)
f11,f12 = split_list(f1)
f21,f22 =  split_list(f2)
t1 = threading.Thread(target=transform_images, args = (f11,))
t2 = threading.Thread(target=transform_images, args = (f12,))
t3 = threading.Thread(target=transform_images, args = (f21,))
t4 = threading.Thread(target=transform_images, args = (f22,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("Done")





