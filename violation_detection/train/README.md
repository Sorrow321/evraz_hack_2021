# Обучение модели для детекции нарушений техники безопасности

## Инструкция по обучению и получению весов
1. Скачайте данные для обучения по ссылке: https://drive.google.com/file/d/1QCI2OSmOtXZAmJb5afv2UiyWyRiLq3_r/view?usp=sharing. В качестве картинок использовался train от организаторов. Разметка на детекцию нарушений безопасности проводилась лично автором. В этом архиве она в формате YOLO.
2. Расположите папку из архива violation_data в этой директории. То есть директория должна выглядеть примерно так:
```
./Dockerfile
./evraz.yaml
./train.sh
./output/
./violation_data/images/
./violation_data/labels/
```
3. Сбилдите ваш докер-образ для обучения:
```bash
cd {rep}/violation_detection/train/
docker build -t violation_detection_train:0.1 .
```
4. Запустите докер-контейнер для обучения:
```bash
cd {rep}/violation_detection/train/
nvidia-docker run --ipc=host -it -v "$PWD"/violation_data:/usr/src/app/violation_data -v "$PWD"/output:/usr/src/app/runs violation_detection_train:0.1
```
5. Начнется процесс обучения. Во время начала вам будет предложено использовать логгер Wandb, введите 3, чтобы его не использовать (либо просто подождите 30 секунд и скрипт сам продолжит работу).
6. После окончания обучения, результаты в будут в ./output/train/expX, где X - число, соответствующее вашему последнему запуску скрипта.
7. Веса будут лежать в ./output/train/expX/weights, где X - номер последнего запуска контейнера. Для этой модели best.pt и last.pt работают примерно одинаково, возможно last.pt чуть лучше (учитывая, что качество оценивалось "на глаз")