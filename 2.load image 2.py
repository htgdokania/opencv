#use matplot lib to show image
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100],linewidth=5)
plt.show()
