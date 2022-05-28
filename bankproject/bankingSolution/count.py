import cv2 
import numpy as np 
import cvlib as cv
import matplotlib.pyplot as plt
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly


img = cv2.imread("C:\\Users\\Admin\\Downloads\\bankproject\\bankproject\\WhatsApp Image 2022-04-11 at 4.57.13 PM.jpeg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.axis("off")
plt.figure(figsize=(10,10))
plt.imshow(img1)



box,lable,count = cv.detect_common_objects(img)
output = draw_bbox(img,box,lable,count)
plt.axis("off")
plt.figure(figsize=(10,10))
plt.imshow(output)
plt.show()

print(f"total {len(lable)}")