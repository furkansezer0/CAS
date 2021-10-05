import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("ShapesForContour.jpg")
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(resim, 50,200)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(resim, contours,-1, (0,255,0),5)

icerik = [resim, canny]

basliklar = ['Kontür', 'Canny']

for i in range(2):
    plt.subplot(1,2,i+1)
    if i == 0:
        plt.imshow(icerik[i])
    else:
        plt.imshow(icerik[i], 'gray')
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])