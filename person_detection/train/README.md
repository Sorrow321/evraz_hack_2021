# Обучение модели для детекции людей на фото

## Инструкция по обучению и получению весов
1. Скачайте данные для обучения по ссылке: https://drive.google.com/file/d/1cCPOorsjpa8RIqx_H5GNFoqWgtGbNs4J/view?usp=sharing. Это данные, которые организаторы предоставили для обучения, просто в формате разметки YOLO. Если не доверяете архиву, можете самостоятельно перегнать COCO формат в YOLO формат с помощью скрипта coco_to_yolo (см. readme в корне репозитория).
2. Расположите папку из архива evraz_data в этой директории. То есть директория должна выглядеть примерно так:
```
./Dockerfile
./evraz.yaml
./train.sh
./output/
./evraz_data/images/
./evraz_data/labels/
```
3. Сбилдите ваш докер-образ для обучения:
```bash
cd {rep}/person_detection/train/
docker build -t person_detection_train:0.1 .
```
4. Запустите докер-контейнер для обучения:
```bash
cd {rep}/person_detection/train/
nvidia-docker run --ipc=host -it -v "$PWD"/evraz_data:/usr/src/app/evraz_data -v "$PWD"/output:/usr/src/app/runs person_detection_train:0.1
```
5. Начнется процесс обучения. Во время начала вам будет предложено использовать логгер Wandb, введите 3, чтобы его не использовать (либо просто подождите 30 секунд и скрипт сам продолжит работу).
6. После окончания обучения, результаты в будут в ./output/train/expX, где X - число, соответствующее вашему последнему запуску скрипта.
7. Веса будут лежат в ./output/train/expX/weights. Для лидерборда я использовал веса last.pt