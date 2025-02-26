import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# ビデオキャプチャを初期化
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 物体検知を実行
    results = model(frame)

    # 結果をフレームに描画
    annotated_frame = results[0].plot()

    # 検出結果を取得
    detections = results[0].boxes

    # フレームを表示
    cv2.imshow('Real-time Object Detection', annotated_frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# リソースを解放
cap.release()
cv2.destroyAllWindows()
