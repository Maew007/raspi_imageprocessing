#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  Created by Asst. Prof. Apicharti Hajaturus 
  Head of Electronic and Computer Industry Program
  Chandrakasem Rajabhat University
  Bangkok Thailand.
  E-mail apichart.h@chandra.ac.th
  website: www.sci.chadra.ac.th/elecnet/
'''
import cv2
import time
import numpy as np

def nothing(x):
    pass

def func_1():
    img = np.zeros((300,512,3),np.uint8)
    # cv2.namedWindow('image')
    # Create the resizeable window
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)

    switch = '0:OFF\n1:ON'
    cv2.createTrackbar(switch,'image',0,1,nothing)
    while(1):
        cv2.imshow('image',img)
        k=cv2.waitKey(1)
        if k == ord('q'):# press q for Exit program
            break

        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:]=0
        else:
            img[:]=[r,g,b]
    cv2.destroyAllWindows()


def main():
    print('Program Starting.....')
    func_1()
    print('End Program Now....!!!!')
    ed = input("Press any key  for close program")
    

if __name__ == '__main__':
    main()
