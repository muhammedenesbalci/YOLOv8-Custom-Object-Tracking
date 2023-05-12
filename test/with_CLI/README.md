## YOLOv8 Custom Object Tracking with CLI(Command Line Interface)

**Usage**

Pip install the ultralytics package including all requirements.  

    pip install ultralytics  

Run this command in CLI.  

    yolo track model=best.pt source='img.jpg' show=True save_txt=True  

**Arguments**

- source	'ultralytics/assets'	source directory for images or videos
- conf	0.25	object confidence threshold for detection
- iou	0.7	intersection over union (IoU) threshold for NMS
- half	False	use half precision (FP16)
- device	None	device to run on, i.e. cuda device=0/1/2/3 or device=cpu
- show	False	show results if possible
- save	False	save images with results
- save_txt	False	save results as .txt file
- save_conf	False	save results with confidence scores
- save_crop	False	save cropped images with results
- hide_labels	False	hide labels
- hide_conf	False	hide confidence scores
- max_det	300	maximum number of detections per image
- vid_stride	False	video frame-rate stride
- line_thickness	3	bounding box thickness (pixels)
- visualize	False	visualize model features
- augment	False	apply image augmentation to prediction sources
- agnostic_nms	False	class-agnostic NMS
- retina_masks	False	use high-resolution segmentation masks
- classes	None	filter results by class, i.e. class=0, or class=[0,2,3]
- boxes True Show boxes in segmentation predictions
