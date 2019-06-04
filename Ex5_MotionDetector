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

def nothing(x):
    pass

def func_canny():
    cap = cv2.VideoCapture(0)
    cap.set(3,160)
    cap.set(4,120)
    cap.set(15, 0.1)
    cap.set(cv2.CAP_PROP_FPS, 3)
    fps = int(cap.get(5))
    print("fps:", fps)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    cv2.createTrackbar('R_up','image',0,255,nothing)
    cv2.createTrackbar('G_up','image',0,255,nothing)
    cv2.createTrackbar('B_up','image',0,255,nothing)
    cv2.createTrackbar('R_dw','image',0,255,nothing)
    cv2.createTrackbar('G_dw','image',0,255,nothing)
    cv2.createTrackbar('B_dw','image',0,255,nothing)
    
    ret_val, img = cap.read()
    cv2.imwrite('/var/www/html/image/buffer1.jpg',img)
    while(1):
        _, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        r_up = cv2.getTrackbarPos('R_up', 'image')
        g_up = cv2.getTrackbarPos('G_up', 'image')
        b_up = cv2.getTrackbarPos('B_up', 'image')
        r_dw = cv2.getTrackbarPos('R_dw', 'image')
        g_dw = cv2.getTrackbarPos('G_dw', 'image')
        b_dw = cv2.getTrackbarPos('B_dw', 'image')
        
        lower_blue = np.array([r_dw, g_dw, b_dw])
        upper_blue = np.array([r_up, g_up, b_up])
        
        mask = cv2.inRange(rgb, lower_blue, upper_blue)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame',frame)
        cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
        cv2.imshow('mask',mask)
        cv2.namedWindow('res', cv2.WINDOW_NORMAL)
        cv2.imshow('res',res)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()

def main():
    print('Program Starting.....')
    func_canny()
    print('End Program Now....!!!!')
    
    

if __name__ == '__main__':
    main()
