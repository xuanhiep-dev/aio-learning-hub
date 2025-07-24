# Helmet Detection Tutorial

This file show the way to train YOLOv10 with new dataset. Use in helmet_detection.ipynb file

### 1. Download dataset

```
!gdown "1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R"
!mkdir safety_helmet_dataset
!unzip -q "/content/Safety_Helmet_Dataset.zip" -d "/content/safety_helmet_dataset"
```

### 2. Download Yolov10 and install some Yolov10's libraries

```
!git clone https://github.com/THU-MIG/yolov10.git
%cd yolov10
!pip install -q -r requirements.txt
!pip install -e .
```

### 3. Download Yolov10 and create the model (Nano version: yolov10n.pt)

```
!wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt

from ultralytics import YOLOv10
MODEL_PATH = "yolov10n.pt"
model = YOLOv10(MODEL_PATH)
```
### 4. Train the model

```
# Setup configs
YAML_PATH = "../safety_helmet_dataset/data.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 64

# Call function
model.train(data = YAML_PATH, epochs = EPOCHS, batch = BATCH_SIZE, imgsz = IMG_SIZE)
```
### 5. Evaluate the model

```
# Model path from training
TRAINED_MODEL_PATH = "runs/detect/train/weights/best.pt"
model = YOLOv10(TRAINED_MODEL_PATH)

# Call function
model.val(data = YAML_PATH, imgsz = IMG_SIZE, split ="test")
```

### 6. For running the Helmet Detection Demo using Streamlit, do it in local

```
streamlit run helmet_detection.py
```