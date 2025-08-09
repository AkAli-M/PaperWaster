import cv2
import numpy as np
import Imagelocation
import time

def ReSizeToAspect(pic,aspect=400):
    (height_og,width_og) = pic.shape[:2]

    new_width = 400
    aspect_ratio = new_width/width_og
    new_height = int(height_og * aspect_ratio)

    resize_pic = cv2.resize(pic,(new_width,new_height))
    return resize_pic


def Filter(Image):
    image = cv2.imread(Image)

    #create an HSV of the image
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #Define white value for HSV
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([255, 30, 255])

    mask = cv2.inRange(HSV, lower_white, upper_white) #HSV mask



    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)


    image_copy = image.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    return image_copy


def BlackFilter(Image):
    #need to update the test,use ShowImage2 to display
    #beacuse image is resized internally
    image1 = cv2.imread(Image)
    image = ReSizeToAspect(image1)

    #create an HSV of the image
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #Define white value for HSV
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([255, 30, 255])

    mask = cv2.inRange(HSV, lower_white, upper_white) #HSV mask



    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    
    (height_og,width_og) = image.shape[:2]

    width = 400
    aspect_ratio = width/width_og
    height = int(height_og * aspect_ratio)
    
    
    black_image = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.drawContours(black_image, contours, -1, (255, 255, 255), 2)
    black_image = cv2.resize(black_image,(width,height))

    image_copy = image.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    return black_image

def ShowImage2(resize_pic,windowname="ShowImage",Loop=False):
    """Displays the image in a window only for development
    """
    # resize_pic = ReSizeToAspect(pic)
    if not Loop:
        cv2.imshow(windowname,resize_pic)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cv2.imshow(windowname,resize_pic)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()

def ShowImage(pic,windowname="After Transformation",Loop=False):
    """Displays the image in a window only for development
    """
    resize_pic = ReSizeToAspect(pic)
    if not Loop:
        cv2.imshow(windowname,resize_pic)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cv2.imshow(windowname,resize_pic)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()

def ShowImageRaw(image,windowname="Original",Loop=False):
    """Displays the image in a window only for development
    """
    pic = cv2.imread(image)
    resize_pic = ReSizeToAspect(pic)
    if not Loop:
        cv2.imshow(windowname,resize_pic)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cv2.imshow(windowname,resize_pic)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()
