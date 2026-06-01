from ultralytics import YOLO

yeni_model = YOLO("./train/weights/best.pt")

yeni_model.predict(source="./videos/2026_thai_gp_race.mp4", show=True, save=True, conf=0.8)