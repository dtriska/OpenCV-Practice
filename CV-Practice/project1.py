import matplotlib.pylab as plt
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img) # creates blank image
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color) # want to mask everything except region of interest
    masked_image = cv2.bitwise_and(img, mask) # get area in both original image and mask
    cv2.imshow('mask', masked_image)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    # added lines is not none so that the call can be iterated even if there are currently no lines detected
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0) # blend two images together by applying a weighted sum of pixel intensities -> can control contribution to final img from each image in the params
    return img

def process(image):
    print(image.shape)
    height = image.shape[0] # gets height of image
    width = image.shape[1] # gets width of image

    region_of_interest_vertices = [(-600, height), (width/2, (height/2 + 10)), (width + 500, height)] # we want left bot corner, right bot corner, anqd something in the middle

    # putting gray and canny before the cropped image to avoid the outside lines we don't want
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # canny edge detection works better with Gray image
    canny_image = cv2.Canny(gray_image, 100, 120) # 100 and 200 are good general threshold ranges
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/180, threshold=40, lines=np.array([]), minLineLength=4, maxLineGap=10) # return line vector of image provided as source -> cropped_image

    image_with_lines = draw_the_lines(image, lines)
    return image_with_lines

cap = cv2.VideoCapture('driving.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = process(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Original code

# import matplotlib.pylab as plt
# import cv2
# import numpy as np

# def region_of_interest(img, verticies):
#     mask = np.zeros_like(img) # creates blank image
#     # channel_count = img.shape[2] # gets number of channels in orig image
#     # dont need below code as its only gonna be one color for V1 as its gray scaled
#     # match_mask_color = (255, ) * channel_count # gets our mask in the same channel as orig image
#     match_mask_color = 255
#     cv2.fillPoly(mask, verticies, match_mask_color) # want to mask everything except region of interest
#     masked_image = cv2.bitwise_and(img, mask) # get area in both orig image and mask
#     cv2.imshow('mask', masked_image)
#     return masked_image

# def draw_the_lines(img, lines):
#     img = np.copy(img)
#     blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

#     img = cv2.addWeighted(img, 0.8, blank_image, 1, 0)
#     return img

# # for image
# # image = cv2.imread('road.jpg')
# # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# def process(image):
#     print(image.shape)
#     height = image.shape[0] # gets height of image
#     width = image.shape[1] # gets width of image

#     region_of_interest_verticies = [(50, height), (width/2, (height/2) + 10), (width - 50, height)] # we want left bot corner, right bot corner, and something in the middle

#     # putting gray and canny before the cropped image to avoid the outside lines we dont want
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # canny edge detection works better with Gray image
#     canny_image = cv2.Canny(gray_image, 100, 200) # 100 and 200 are good general threshold ranges
#     cropped_image = region_of_interest(canny_image, np.array([region_of_interest_verticies], np.int32))

#     lines = cv2.HoughLinesP(cropped_image, rho=4, theta=np.pi/80, threshold=40, lines=np.array([]), minLineLength=4, maxLineGap=1) # return line vector of image provided as source -> cropped_image

#     image_with_lines = draw_the_lines(image, lines)
#     return image_with_lines

# cap = cv2.VideoCapture('driving.mp4')

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     frame = process(frame)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# # for image
# # plt.imshow(image_with_lines)
# # plt.show()
