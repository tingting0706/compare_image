import numpy as np

import os
from os import listdir

import cv2

path = './20190216_compare'

dir_list = listdir(path)
lenth = int(len(dir_list)/2)

for i in range(0,lenth,2):
    img_new_dir = '{}/{}'.format(path,dir_list[i])
    img_org_dir = '{}/{}'.format(path,dir_list[i+1])
    #print(img_org_dir)
    img_new = cv2.imread(img_new_dir,0)
    img_org = cv2.imread(img_org_dir,0)
    
    not_same_arr = cv2.subtract(img_new, img_org)
    total_none_zero = np.count_nonzero(not_same_arr)
    if total_none_zero > 0:
        print(img_org_dir)