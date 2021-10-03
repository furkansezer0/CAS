import cv2
from matplotlib import pyplot as plt

resim1 = []
uzanti = [".bmp", ".tiff", ".png"]

for i in range(3): # Döngü ile resmin dosyadan alınıp 3 ayrı formatta kaydedilmesi
    resim1.append(cv2.imread("Resim1.jpeg", 1))
    cv2.imwrite(f"Resim1_{i+1}{uzanti[i]}", resim1[i])  

for i in range(3): # Renk dönüşümünün yapılıp tabloda çıktıların gösterilmesi
    plt.subplot(1, 3, i+1)
    resim1[i] = cv2.cvtColor(resim1[i], cv2.COLOR_BGR2RGB)
    plt.imshow(resim1[i])
    plt.title(f"Resim1_{i+1}{uzanti[i]}")
    plt.xticks([]),plt.yticks([])


