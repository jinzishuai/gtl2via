## Usage Case

We use [CVAT](https://github.com/opencv/cvat) to annotate the images using the labels provided by [COCO](https://cocodataset.org/#home)'s 80 catagories/classes, which is used by [YOLOv5](https://github.com/ultralytics/yolov5/blob/master/data/coco.yaml).

These 8 classes are
```yaml
# number of classes
nc: 80

# class names
names: ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
        'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
        'hair drier', 'toothbrush']
```

When creating a CVAT task, we need to define labels. One way is to copy-paste a json document. This command intends to generate the needed json document.

### Challengens of CVAT Labels

* the id field is globally numbers, across different tasks: but they are not used in the exported YOLO index
  * the input id field will be overwritten by the system
* the labels are saved with alphabetic order

So we have to provide (almost) the same number of labels with only one label we are interested and the rest of them padded with pure numbers.

### Result of using the "cup" label only

* `cup` is at index 41 out of the 80 COCO classes (starting from 0)
* result of the labels used in CVAT
![image](https://user-images.githubusercontent.com/1074685/90991521-08c8f000-e567-11ea-9ec3-ab7922ed46c7.png)
* example result of an exported annonation file in YOLO format, noting that index `41` is still  used:
```
41 0.404139 0.546949 0.505878 0.536368
```
