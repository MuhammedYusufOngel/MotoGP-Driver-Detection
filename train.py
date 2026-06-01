from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data="./dataset_final/YOLODataset/dataset.yaml",
    epochs=50,
    imgsz=640,
    device='0',

    degrees=10.0,
    hsv_h=0.015, hsv_s=0.7, hsv_v=0.4,
    scale=0.5,
    perspective=0.001,
    fliplr=0.5,
    mosaic=0.5,
)