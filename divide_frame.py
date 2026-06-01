import cv2
import os

video = '2026_mugello_sprint'

video_yolu = 'videos/' + video + '.mkv'
kayit_klasoru = 'dataset_' + video + '/'
os.makedirs(kayit_klasoru, exist_ok=True)

cap = cv2.VideoCapture(video_yolu)
fps = cap.get(cv2.CAP_PROP_FPS)
kare_araligi = int(fps / 3)

kare_sayaci = 0
kaydedilen_sayac = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    if kare_sayaci % kare_araligi == 0:
        cv2.imwrite(f"{kayit_klasoru}{video}_frame_{kaydedilen_sayac}.jpg", frame)
        kaydedilen_sayac += 1
        
    kare_sayaci += 1

cap.release()
print(f"{kaydedilen_sayac} adet görsel başarıyla kaydedildi.")