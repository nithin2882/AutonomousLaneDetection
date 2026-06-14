# src/lane_detector.py

import cv2
import numpy as np

class LaneDetector:

    def detect_lane(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blur, 50, 150)

        return edges