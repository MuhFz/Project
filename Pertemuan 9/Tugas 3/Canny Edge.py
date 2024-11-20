import cv2

image = cv2.imread("C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/Saved Pictures/wp8195355-corolla-dx-wallpapers.jpg")
canny = cv2.Canny(image, 150, 100, 3, L2gradient=True)

cv2.imshow("Original", image)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
