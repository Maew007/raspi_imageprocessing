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

    cv2.createTrackbar('H_up','image',0,255,nothing)
    cv2.createTrackbar('S_up','image',0,255,nothing)
    cv2.createTrackbar('V_up','image',0,255,nothing)
    cv2.createTrackbar('H_dw','image',0,255,nothing)
    cv2.createTrackbar('S_dw','image',0,255,nothing)
    cv2.createTrackbar('V_dw','image',0,255,nothing)
    
    ret_val, img = cap.read()
    cv2.imwrite('/var/www/html/image/buffer1.jpg',img)
    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h_up = cv2.getTrackbarPos('H_up', 'image')
        s_up = cv2.getTrackbarPos('S_up', 'image')
        v_up = cv2.getTrackbarPos('V_up', 'image')
        h_dw = cv2.getTrackbarPos('H_dw', 'image')
        s_dw = cv2.getTrackbarPos('S_dw', 'image')
        v_dw = cv2.getTrackbarPos('V_dw', 'image')
        # golf color             0,  195,  162
        lower_color = np.array([h_dw, s_dw, v_dw])
        #                       13,  255,  255
        upper_color = np.array([h_up, s_up, v_up])
        
        mask = cv2.inRange(hsv, lower_color, upper_color)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow('image',frame)
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
