# src/main.py

import cv2
from lane_detector import LaneDetector

cap = cv2.VideoCapture(0)

detector = LaneDetector()

while True:

    ret, frame = cap.read()

    lane = detector.detect_lane(frame)

    cv2.imshow("Lane Detection", lane)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()