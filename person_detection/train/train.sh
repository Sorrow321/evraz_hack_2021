#!/bin/sh
python train.py --data evraz.yaml  --epochs 40 --cfg yolov5l.yaml --img 640 --weights yolov5l.pt --batch-size 4