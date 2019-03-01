import PIL
from PIL import ImageColor
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
import os.path
image = Image.open('cancer.jpg')
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'cancer.jpg')
img = plt.imread('cancer.jpg')

fig, axes = plt.subplots(1, 1)
axes.imshow(img, interpolation='none')


directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'canceruk2.jpg')
img = plt.imread('canceruk2.jpg')

fig, axes = plt.subplots(1, 1)
axes.imshow(image, interpolation='none')
fig.show()



image = Image.open('canceruk.jpg')
logo = Image.open('canceruk2.jpg')
image_copy = image.copy()
image_copy.paste(logo, (9, 8))
image_copy.save('pasted_image.jpg')


height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(175):
        if sum(img[r][c])<600: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,0]   

height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(175):
        if sum(img[r][c])<500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,0,255]   
height = len(img) 
width = len(img[0])
for r in range(height):
    for c in range(175):
        if sum(img[r][c])<100: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,255,255] # R + B = magenta
            

            

            
            
fig.show()

