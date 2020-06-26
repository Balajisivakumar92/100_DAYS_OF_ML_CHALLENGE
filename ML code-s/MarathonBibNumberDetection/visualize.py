import cv2 

Image = cv2.imread("img1.jpg")


# (16,111),(46,105),(51,127),(20,133)

x = 111
y = 105
w = 51
h = 20

image = cv2.rectangle(Image,(x,y),(x+w,y+h), (36,255,12), 2)
cv2.putText(image, '194', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36,255,12), 2)

cv2.imwrite("Detected1.png",image)




