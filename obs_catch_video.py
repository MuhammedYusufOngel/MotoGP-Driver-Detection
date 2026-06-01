import cv2
from ultralytics import YOLO

model = YOLO("./train/weights/best.pt")

# OBS VIRTUAL CAMERA
cap = cv2.VideoCapture(1) 

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("OBS Sanal Kameradan görüntü alınamadı.")
        break
        
    results = model(frame, stream=True, conf=0.8)
    
    for r in results:
        annotated_frame = r.plot()
        
    cv2.imshow("Live MotoGP Analysis", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()