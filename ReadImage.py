import cv2 as cv
img= cv.imread('images\leuvenA.jpg', 1)
#print((img))
#print(len(img)) 
print(img.shape)
if img is None:
    print("image vide")
else:
    cv.imshow('image', img) 
    cv.waitKey(0)
    cv.destroyAllWindows()


