import cv2
import numpy as np
import utils
import time
import os

image = cv2.imread('document.jpg')


image = cv2.resize(image, (1000, 1600))

cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow('Blurred Gray Image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges = cv2.Canny(blurred, 0, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv2.contourArea, reverse=True)

for contour in contours:
    peri = cv2.arcLength(contour, True)
    approx = cv2. approxPolyDP(contour, 0.02* peri, True)

    if len(approx) == 4:
        document_contour = approx
        break

cv2.drawContours(image, [document_contour], -1, (0, 255, 0), 2)

cv2.imshow('Document Contour', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

warped = utils.four_points_transfom(image, document_contour.reshape(4, 2))

warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

mask = warped_gray > 220
warped_gray[mask] = 255

# uncommenting this code would make the document text darker/more defined
# warped_gray = cv2.convertScaleAbs(warped_gray, alpha=1.5, beta=-100)

timestamp = time.strftime("%Y%m%d_%H%M%S")
output_dir = './Scanned'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_filename = f'scanned_{timestamp}.jpg'
output_path = os.path.join(output_dir, output_filename)

cv2.imshow('Scanned Documment', warped_gray)
cv2.imwrite(output_path, warped_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
