from ultralytics import YOLO

# Load the model. You can choose other models.
model = YOLO('yolov8m.pt')

# Train model. I set device to 'CPU' because YOLOv8 give errors on GTX1650 GPUs.
model.train(
    data='data.yaml',
    imgsz=640,
    epochs=10,
    batch=4,
    name='yolov8_custom_object_tracking',
    device='CPU',
    pretrained=True
)
