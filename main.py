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
    while(count < num):
        count = count + 1;
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
        final = [];
        for i in range(rows-1,-1,-1):
            carveElements.append(currIndex);
            img[i,currIndex] = 255;
            row = img[i,:];
            
            out = np.delete(row,currIndex);
            final.append(out);
    
            if(PathMatrix[i,currIndex] == 0):
                currIndex = currIndex - 1;
            elif(PathMatrix[i,currIndex] == 1):
                currIndex = currIndex;
            else:
                currIndex = currIndex + 1;
            
        cv2.imshow('a',img);cv2.waitKey(1);
        final = np.array(final);
        img = cv2.flip(final,0);
        cv2.imshow('a',img);
        cv2.waitKey(2);
    return(img)
    
if __name__ == '__main__':
    img = cv2.imread('images/img2.jpg',0);
    
    img = np.double(img);
    final = carveColumns(img,100);