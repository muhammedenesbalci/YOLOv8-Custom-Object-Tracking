## YOLOv8 Custom Object Tracking with Code  
  
 - Pip install the ultralytics package including all requirements.  
    ```  
    pip install ultralytics  
    ```  
 - Prepare ***data.yaml*** file. Necessary details are written in the file.  
 - Run ***main.py***.  
 - Best model and latest model in ***runs/detect/yolov8_custom_object_detection/weights/*** .  
  
**Models**  
  
| Model | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |  
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |  
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt) | 640 | 37.3 | 80.4 | 0.99 | 3.2 | 8.7 |  
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt) | 640 | 44.9 | 128.4 | 1.20 | 11.2 | 28.6 |  
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt) | 640 | 50.2 | 234.7 | 1.83 | 25.9 | 78.9 |  
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt) | 640 | 52.9 | 375.2 | 2.39 | 43.7 | 165.2 |  
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt) | 640 | 53.9 | 479.1 | 3.53 | 68.2 | 257.8 |  
  
**Arguments**  
  
- model None path to model file, i.e. yolov8n.pt, yolov8n.yaml
- data None path to data file, i.e. coco128.yaml
- epochs 100 number of epochs to train for
- patience 50 epochs to wait for no observable improvement for early stopping of training
- batch 16 number of images per batch (-1 for AutoBatch)
- imgsz 640 size of input images as integer or w,h
- save True save train checkpoints and predict results
- save_period -1 Save checkpoint every x epochs (disabled if < 1)
- cache False True/ram, disk or False. Use cache for data loading
- device None device to run on, i.e. cuda device=0 or device=0,1,2,3 or device=cpu
- workers 8 number of worker threads for data loading (per RANK if DDP)
- project None project name
- name None experiment name
- exist_ok False whether to overwrite existing experiment
- pretrained False whether to use a pretrained model
- optimizer 'SGD' optimizer to use, choices=['SGD', 'Adam', 'AdamW', 'RMSProp']
- verbose False whether to print verbose output
- seed 0 random seed for reproducibility
- deterministic True whether to enable deterministic mode
- single_cls False train multi-class data as single-class
- rect False rectangular training with each batch collated for minimum padding
- cos_lr False use cosine learning rate scheduler
- close_mosaic 0 (int) disable mosaic augmentation for final epochs
- resume False resume training from last checkpoint
- amp True Automatic Mixed Precision (AMP) training, choices=[True, False]
- lr0 0.01 initial learning rate (i.e. SGD=1E-2, Adam=1E-3)
- lrf 0.01 final learning rate (lr0 * lrf)  
- momentum 0.937 SGD momentum/Adam beta1  
- weight_decay 0.0005 optimizer weight decay 5e-4  
- warmup_epochs 3.0 warmup epochs (fractions ok)  
- warmup_momentum 0.8 warmup initial momentum  
- warmup_bias_lr 0.1 warmup initial bias lr  
- box 7.5 box loss gain  
- cls 0.5 cls loss gain (scale with pixels)  
- dfl 1.5 dfl loss gain  
- pose 12.0 pose loss gain (pose-only)  
- kobj 2.0 keypoint obj loss gain (pose-only)  
- label_smoothing 0.0 label smoothing (fraction)  
- nbs 64 nominal batch size  
- overlap_mask True masks should overlap during training (segment train only)  
- mask_ratio 4 mask downsample ratio (segment train only)  
- dropout 0.0 use dropout regularization (classify train only)  
- val True validate/test during training