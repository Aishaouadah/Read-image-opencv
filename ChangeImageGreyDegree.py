import cv2 as cv
import numpy as np
img= cv.imread('images\leuvenA.jpg', 0)
#print((img))
#print(len(img)) 
print(img.shape)
if img is None:
    print("image vide")
else:
    h , w = img.shape
    img2 = np.zeros((h,w), np.uint8)
    for y in range(h):
        for x in range(w):
            img2[y,x] = 255 - img [y,x]

    cv.imshow('image', img)
    cv.imshow('image2', img2)
    #imwrite('test.jpg' , img2 )
    cv.waitKey(0)
    cv.destroyAllWindows()

