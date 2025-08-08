import cv2
import numpy as np
import Imagelocation

image = cv2.imread(Imagelocation.image_6)

#create an HSV of the image
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Define white value for HSV
lower_white = np.array([0, 0, 200])
upper_white = np.array([255, 30, 255])

mask = cv2.inRange(HSV, lower_white, upper_white)

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
 

image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
          



























def ShowImage(pic,windowname="ShowImage"):
    """Displays the image in a window only for development
    """
    (height_og,width_og) = pic.shape[:2]

    new_width = 400
    aspect_ratio = new_width/width_og
    new_height = int(height_og * aspect_ratio)

    resize_pic = cv2.resize(pic,(new_width,new_height))

    cv2.imshow(windowname,resize_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ShowImage(image_copy)
