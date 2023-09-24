from PIL import Image
pict = Image.open("Invoice_12.jpg")
#We will have to use the .bmp extension.
#This allows for other functions to be performed in the image
#Storing the image using save() function
# pict.save('sportscar.bmp')
# pict = Image.open('sportscar.bmp')
pict.show()
#We create a loop that allows for ixteration between the X and Y pixels
for x in range(pict.size[0]):
    for y in range(pict.size[1]):
        r, g, b = pict.getpixel((x, y))
        pict.putpixel((x, y), (r, g, 0))
 #Used for displaying the executed image.
pict.save('sportscar1.bmp')
pict.show()









# import pytesseract
# import cv2
# import numpy as np

# img = cv2.imread('Invoice_01.jpg')

# #  img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
# img = cv2.resize(img, None, fx=2, fy=2)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# kernel = np.ones((1,1), np.uint8)
# #  img = cv2.dilate(img, kernel, iterations=1)
# #  img = cv2.erode(img, kernel, iterations=1)

# #  img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.imwrite('thresh.png', img)

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    
# for psm in range(6,13+1):
#     config = '--oem 3 --psm %d' % psm
#     txt = pytesseract.image_to_string(img, config = config, lang='eng')
#     print('psm ', psm, ':',txt)