import cv2
from matplotlib import pyplot as plt
import numpy as np

resim1 = cv2.imread('Resim1.jpeg')
griresim1 = cv2.cvtColor(resim1, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(griresim1, (3,3), 0)

# Değişen sigma değerlerine göre resime uygun canny miktarı ayarlama
def autocanny(gauss, sigma = 0.35):
    median = np.median(gauss)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(min(255,(1.0+sigma)*median))
    canny = cv2.Canny(gauss,lower, upper)
    
    return canny

auto = autocanny(gauss)

icerik = [griresim1, auto]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(icerik[i],'gray', vmin= 0, vmax = 255)
    plt.xticks([]),plt.yticks([])
