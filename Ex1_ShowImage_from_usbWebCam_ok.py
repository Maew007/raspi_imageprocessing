"""
  This is  simple program  for capture image from web camera usb  after that
  save it to image file.
  if you want to quit program please  Press <esc> to quit.
"""
import cv2
import time



def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    cam.set(15, 0.1)
    i = 0
    while True:  
        ret_val, img = cam.read()
        #cv2.imwrite('/home/pi/img_capture.jpg',img)
        cv2.imwrite('/var/www/html/image/img.jpg',img)
        #/var/www/html/image
        img_in = cv2.imread('/var/www/html/image/img.jpg')
        # Create the resizeable window
        cv2.namedWindow('my webcam', cv2.WINDOW_NORMAL)
        # Display the image
        cv2.imshow('my webcam',img_in)
        print('test')
        print(i)
        i=  i +1
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

