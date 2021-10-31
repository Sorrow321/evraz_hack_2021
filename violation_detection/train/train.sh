#!/bin/sh
python train.py --data violations.yaml  --epochs 150 --cfg yolov5m.yaml --weights yolov5m.pt --batch-size 4