import json
from pathlib import Path


input_file = 'violation_data_coco.json'

Path("output_yolo").mkdir(parents=True, exist_ok=True)
with open(input_file) as f:
    d = json.load(f)

image_to_annotations = {}
for labels in d['annotations']:
    if labels['image_id'] in image_to_annotations:
        image_to_annotations[labels['image_id']].append(labels['bbox'])
    else:
        image_to_annotations[labels['image_id']] = [labels['bbox']]

for img in d['images']:
    idx = img['id']
    if idx in image_to_annotations:
        labels = image_to_annotations[idx]
        orig_w = img['width']
        orig_h = img['height']
        img_name = img['file_name']
        yolo_format = []
        for bbox in labels:
            bbox[0] += bbox[2] / 2
            bbox[1] += bbox[3] / 2
            yolo_format.append((bbox[0] / orig_w, bbox[1] / orig_h, bbox[2] / orig_w, bbox[3] / orig_h))
        with open('output_yolo/' + Path(img_name).stem + '.txt', 'wt') as file:
            for bbox in yolo_format:
                res = '0 ' + ' '.join(map(str, bbox))
                file.write(res)
                file.write('\n')
    else:
        img_name = img['file_name']
        with open('output_yolo/' + Path(img_name).stem + '.txt', 'wt') as file:
            pass