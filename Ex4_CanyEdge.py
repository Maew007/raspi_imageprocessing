#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  Created by Asst. Prof. Apicharti Hajaturus 
  Head of Electronic and Computer Industry Program
  Chandrakasem Rajabhat University
  Bangkok Thailand.
  E-mail apichart.h@chandra.ac.th
  website: www.sci.chadra.ac.th/elecnet/
  reference from
  https://pythonprogramming.net/canny-edge-detection-gradients-python-opencv-tutorial/
'''
import cv2
import time
import numpy as np

def func_canny():
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    cam.set(15, 0.1)
    ret_val, img = cam.read()
    cv2.imwrite('/var/www/html/image/buffer1.jpg',img)
    while(True):   
        ret_val, img = cam.read()
        cv2.imwrite('/var/www/html/image/buffer1.jpg',img)
        #/var/www/html/image
        frame = cv2.imread('/var/www/html/image/buffer1.jpg')
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([30,150,50])
        upper_red = np.array([255,255,180])
        
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        # Create the resizeable window
        cv2.namedWindow('Edges', cv2.WINDOW_NORMAL)
        # Display the image
        #cv2.imshow('Original',frame)
        edges = cv2.Canny(frame,100,200)
        cv2.imshow('Edges',edges)
        cv2.imwrite('/var/www/html/image/img.jpg',edges)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()

def main():
    print('Program Starting.....')
    func_canny()
    print('End Program Now....!!!!')
    
    

if __name__ == '__main__':
    main()
