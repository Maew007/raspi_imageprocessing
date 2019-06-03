import cv2
import numpy as np

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True

cv2.namedWindow('image capture', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image capture', onMouse)
#initialize the camera object with VideoCapture
camera = cv2.VideoCapture(0)
sucess, frame = camera.read()
cv2.imwrite('/var/www/html/image/img.jpg',frame)
#cv2.imwrite('snapshot.png', frame)
gray = cv2.imread('snapshot.png', cv2.IMREAD_GRAYSCALE)
while sucess and cv2.waitKey(1) == -1 and not clicked:
    #cv2.imwrite('snapshot.png', frame)
    cv2.imwrite('/var/www/html/image/img.jpg',gray)
    gray = cv2.imread('/var/www/html/image/img.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image capture', gray)
    sucess, frame = camera.read()

#cv2.imwrite('snapshot.png', frame)
cv2.imwrite('/var/www/html/image/img.jpg', gray)
print ('photo taken press any key to exit')
cv2.waitKey()
cv2.destroyAllWindows()
