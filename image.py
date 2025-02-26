import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

img = cv2.imread('img/IMG_3789.jpeg')

# 物体検知を実行
results = model(img)

# 結果をフレームに描画
annotated_frame = results[0].plot()

# 検出結果を取得
detections = results[0].boxes

# フレームを表示
cv2.imwrite('img/result_img.jpeg', annotated_frame)
