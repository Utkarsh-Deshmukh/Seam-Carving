# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:23:34 2017

@author: Utkarsh
"""

import cv2
import numpy as np


def calcEnergy(img):
    rows,cols = img.shape;
    img = cv2.copyMakeBorder(img,0,1,0,1,cv2.BORDER_REPLICATE)
    diffX = (np.diff(img,axis=0));
    diffY = (np.diff(img,axis=1));

    diffX = cv2.copyMakeBorder(diffX,1,0,0,0,0)
    diffY = cv2.copyMakeBorder(diffY,0,0,1,0,0)
    EnergyImg = np.sqrt(np.power(diffX,2) + np.power(diffY,2));
    EnergyImg = EnergyImg[0:rows,0:cols]
    return(EnergyImg);

def carveColumns(img, num):
    count = 0;
    color_img = img;
    while(count < num):
        count = count + 1;
        img = cv2.cvtColor(np.uint8(color_img),cv2.COLOR_BGR2GRAY)
        img = np.double(img);
        EnergyImg = calcEnergy(img);
        cumsumEnergy = np.zeros(EnergyImg.shape);
        PathMatrix = np.zeros(EnergyImg.shape);
        rows, cols = EnergyImg.shape;
        
        cumsumEnergy[0,:] = EnergyImg[0,:];
        for i in range(1,rows):
            for j in range(0,cols):
                
                if(j == 0):
                    temp = [99999, cumsumEnergy[i-1,j], cumsumEnergy[i-1,j+1]];
                elif(j == cols-1):
                    temp = [cumsumEnergy[i-1,j-1], cumsumEnergy[i-1,j], 99999];
                else:
                    temp = [cumsumEnergy[i-1,j-1], cumsumEnergy[i-1,j], cumsumEnergy[i-1,j+1]];
    
                cumsumEnergy[i,j] = EnergyImg[i,j] + min(temp)
                PathMatrix[i,j] = temp.index(min(temp))
    
        ## Start Carving
        temp = np.array(cumsumEnergy[rows-1,:]);
        temp = temp.tolist();
        startIndex = temp.index(min(temp))
        currIndex = startIndex;
        carveElements = [];
        img = np.uint8(img);
        final_b = [];  final_g = [];  final_r = [];
        for i in range(rows-1,-1,-1):
            carveElements.append(currIndex);
            color_img[i,currIndex,2] = 255;         # This step is only for visualisation purpose.
            row_b = color_img[i,:,0];
            row_g = color_img[i,:,1];
            row_r = color_img[i,:,2];
        
            out_b = np.delete(row_b,currIndex);
            out_g = np.delete(row_g,currIndex);
            out_r = np.delete(row_r,currIndex);

            final_b.append(out_b);
            final_g.append(out_g);
            final_r.append(out_r);

            if(PathMatrix[i,currIndex] == 0):
                currIndex = currIndex - 1;
            elif(PathMatrix[i,currIndex] == 1):
                currIndex = currIndex;
            else:
                currIndex = currIndex + 1;
        
        cv2.imshow('a',color_img/255);cv2.waitKey(1);
        r,c = np.shape(final_b)
        temp_final = np.zeros((r,c,3))
        cv2.imshow('a',color_img/255);
        temp_final[:,:,0] = final_b;
        temp_final[:,:,1] = final_g;
        temp_final[:,:,2] = final_r;
        color_img = temp_final;
        color_img = np.array(color_img);
        
        color_img = cv2.flip(color_img,0);
        cv2.imshow('a',color_img/255);
        cv2.waitKey(1);
    return(color_img)
    
if __name__ == '__main__':
    img = cv2.imread('images/img2.jpg',1);
    
    img = np.double(img);
    out = carveColumns(img,100);
    
    