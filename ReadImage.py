import cv2 as cv
img= cv.imread('images\lena.jpg', 1)
print((img))
print(len(img))
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
