# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for contour in contours:
#         # Approximate the contour to a polygon
#         epsilon = 0.04 * cv2.arcLength(contour, True)
#         approx = cv2.approxPolyDP(contour, epsilon, True)

#         # Check if the shape has 4 vertices (a rectangle)
#         if len(approx) == 4:
#             # Check if the area is large enough to be the object you want
#             area = cv2.contourArea(contour)
#             if area > 10:  # Adjust this value based on your image
#                 # Draw the contour on the original image
#                 x, y, w, h = cv2.boundingRect(approx)
#                 cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


# for contour in contours:
#     epsilon = 0.04 * cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, epsilon, True)

#     # Check if the shape has approximately 4 vertices and a significant area
#     if len(approx) == 4 and cv2.contourArea(contour) > 100:
#         # A possible rectangle found
#         # You can add more checks here, like aspect ratio
        
#         # Draw the contour on the original image
#         cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)


def Filter2(Image):
    image = cv2.imread(Image)

    #create an HSV of the image
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #Define white value for HSV
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 25, 255])

    mask = cv2.inRange(HSV, lower_white, upper_white) #HSV mask

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result = np.zeros_like(image)
    cv2.drawContours(result, contours, -1, (255, 255, 255), -1)
    result = cv2.bitwise_and(image, image, mask=mask)


    result = cv2.bitwise_and(image, image, mask=mask)


    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)


    image_copy = image.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    return result

def Filter3(Image):
    image = cv2.imread(Image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    output_image = image.copy()

    for contour in contours:
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            cv2.drawContours(output_image, [approx], -1, (0, 255, 0), 2)

            x, y, w, h = cv2.boundingRect(approx)

            aspect_ratio = float(w) / h

            if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                cv2.putText(output_image, 'Square', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.putText(output_image, 'Rectangle', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return output_image


def Filter1(Image):
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




