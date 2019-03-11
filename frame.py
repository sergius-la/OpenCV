import cv2
import os

"""
NOTE: Save Image
https://stackoverflow.com/questions/41586429/opencv-saving-images-to-a-particular-folder-of-choice/41586549
"""

img = cv2.imread('1.jpg', 1)
path = 'D:/OpenCV/Scripts/Images'
cv2.imwrite(os.path.join(path, 'image.jpg'), img)
