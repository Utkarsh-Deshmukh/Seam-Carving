# Seam-Carving
Content aware image resizing

## Abstract
The usual image resizing operation does not take into account the image content. In this project, we can reduce the size of the image using an approach called seam carving (also known as content aware image resizing). A seam is an optimal 8-connected path of pixels on a single image from top to bottom, or left to right, where optimality is defined by an image energy function [1]. 

## Results

![animation2](https://cloud.githubusercontent.com/assets/13918778/26339853/d1b5f098-3f3f-11e7-81e1-a895efb9d599.gif)

## Energy function:
The energy function used is the magnitude of simple first order partial derivatives in x and y axis.
![first equation](http://latex.codecogs.com/gif.latex?E%28x%2Cy%29%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%5E%7B2%7D%20&plus;%20%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%5E%7B2%7D%20%7D)

## Overall algorithm

![temp](https://cloud.githubusercontent.com/assets/13918778/26340060/1b9289fa-3f41-11e7-9b99-f4718e659803.PNG)


# How to run the file?
run the main.py file

# Notes:
Presently the code only carves out columns in the image (Vertical seams). I will push the code to carve horizontal seams soon.

# Refrences
[1] S. Avidan and A. Shamir. Seam carving for content-aware image resizing. ACM Trans. on Graphics, 26(3), 2007


# Acknowledgements
I would like to thank Swanand Pathak for his help and guidance
