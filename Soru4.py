import cv2


resim = cv2.imread("StarryNight.jpg") # Kod ile aynı dosyadan resim çekme

cv2.line(resim, (50,300), (500,50), (0,255,0), 5) # Çizgi çizdirme
cv2.rectangle(resim, (50,50), (400,400), (255,0,0), 2) # Dikdörtgen çizdirme
cv2.circle(resim, (400,400), 60, (0,0,255), 3) # Daire çizdirme

cv2.imshow("Starry Night", resim) # Üzerine şekil eklenmiş resmi gösterme

key = cv2.waitKey(0) # Bir tuş basılana kadar bekletme

cv2.destroyAllWindows() # açık pencereleri kapatma

if key == ord("s"): # Basılan tuş s ise Shapes.png dosyası kaydetme
    print("Shapes.png kaydedildi")
    cv2.imwrite("Shapes.png", resim)
