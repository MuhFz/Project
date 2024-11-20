import cv2

image = cv2.imread("C:/Users/HP/Downloads/1ljmqxinvgkb25e.jpg", cv2.IMREAD_COLOR)
image = cv2.GaussianBlur(image, (3, 3), 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ddepth = cv2.CV_16S
kernel_size = 3
laplacian = cv2.Laplacian(gray, ddepth, ksize=kernel_size)
laplacianAbsolute = cv2.convertScaleAbs(laplacian)

cv2.imshow("Original", image)
cv2.imshow("LoG", laplacianAbsolute)
cv2.waitKey(0)
cv2.destroyAllWindows()
