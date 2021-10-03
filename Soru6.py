import cv2
from matplotlib import pyplot as plt

resim2 = cv2.imread("Resim2.jpeg") # Kod ile aynı dosyadan resim çekme
resim2 = cv2.cvtColor(resim2, cv2.COLOR_BGR2RGB) # Renk dönüşümü

Gaussian = cv2.GaussianBlur(resim2, (5,5), 0)
Mean = cv2.blur(resim2,(5,5))
Median = cv2.medianBlur(resim2, 5)


filtreler = [resim2, Gaussian, Mean, Median]
basliklar = ['Orijinal Resim', 'Gaussian', 'Mean', 'Median']

for i in range(4):  
    plt.subplot(1, 4, i+1)
    plt.imshow(filtreler[i])
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
