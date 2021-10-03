import cv2
from matplotlib import pyplot as plt

resim3 = cv2.imread('Resim3.jpeg',0)
ret,thresh1 = cv2.threshold(resim3, 127, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(resim3, 127, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(resim3, 127, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(resim3, 127, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(resim3, 127, 255, cv2.THRESH_TOZERO_INV)
ret,thresh6 = cv2.threshold(resim3, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh7 = cv2.adaptiveThreshold(resim3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11,2)
thresh8 = cv2.adaptiveThreshold(resim3, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11,2)
basliklar = ['Orijinal Resim','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'
          , 'BINARY + OTSU', 'ADP GAUS BINARY', 'ADP MEAN BINARY']
resimler = [resim3, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6,
            thresh7, thresh8]

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(resimler[i],'gray',vmin=0,vmax=255)
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])

