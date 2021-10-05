import cv2
from matplotlib import pyplot as plt
import numpy as np

resim = cv2.imread("siyahbeyaz.jpg")
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

kernel = np.ones((3,3), np.uint8) #Morfoloji işlemleri için kernel tanımlaması
kernel2 = np.array([[-1, -1, -1], #Keskinleştirme işlemi için kernel tanımı
                    [-1, 9, -1],
                    [-1, -1, -1]])

# Gürültüyü azaltıp ön planda olması gereken nesneyi netleştirme denemesi
erosion = cv2.erode(resim, kernel, iterations=2) 
dilation = cv2.dilate(erosion, kernel, iterations=6)
Gaussian = cv2.GaussianBlur(dilation, (3,3), 0)
ret,thresh = cv2.threshold(Gaussian, 32, 255, cv2.THRESH_BINARY)
sharpness = cv2.filter2D(thresh, -1, kernel2)


erosion = cv2.erode(resim, kernel, iterations=1)
dilation = cv2.dilate(resim, kernel, iterations=1)
opening = cv2.morphologyEx(resim, cv2.MORPH_OPEN, kernel)
# Opening = Önce Erosion sonra Dilation
closing = cv2.morphologyEx(resim, cv2.MORPH_CLOSE, kernel)
# Closing = Önce Dilation sonra Erosion
tophat = cv2.morphologyEx(resim, cv2.MORPH_TOPHAT, kernel)
# Top Hat = Resim Opening Farkı
blackhat = cv2.morphologyEx(resim, cv2.MORPH_BLACKHAT, kernel)
# Black Hat = Resim Closing Farkı
gradient = cv2.morphologyEx(resim, cv2.MORPH_GRADIENT, kernel)
# Gradient = Dilation Erosion Farkı
ellipse = cv2.morphologyEx(resim, cv2.MORPH_ELLIPSE, kernel)
# Elips şeklinde kernel ile işlem
rect = cv2.morphologyEx(resim, cv2.MORPH_RECT, kernel)
# Kare şeklinde kernel ile işlem
cross = cv2.morphologyEx(resim, cv2.MORPH_CROSS, kernel)
# Artı şeklinde kernel ile işlem

icerik = [resim, sharpness, erosion, dilation, opening, closing, tophat, 
          blackhat, gradient, ellipse, rect, cross]

basliklar = ['Normal', 'Sharpness', 'Erosion', 'Dilation', 'Opening',
             'Closing', 'Top Hat', 'Black Hat', 'Gradient', 
             'Ellipse', 'Rect', 'Cross']

for i in range(12):
    plt.subplot(4,3,i+1)
    plt.imshow(icerik[i])
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])