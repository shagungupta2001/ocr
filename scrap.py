# import cv2
# import pytesseract
# img = cv2.imread("Invoice_02.jpg")
# text = pytesseract.image_to_string(img)
# print(text)

import cv2
import pytesseract
image = cv2.imread("sportscar1.bmp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)