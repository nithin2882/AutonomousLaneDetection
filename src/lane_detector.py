import cv2
import numpy as np

class LaneDetector:

    def detect_lane(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5,5), 0)

        edges = cv2.Canny(blur, 50, 150)

        height, width = edges.shape

        histogram = np.sum(
            edges[height//2:, :],
            axis=0
        )

        lane_center = np.argmax(histogram)

        frame_center = width // 2

        return edges, lane_center, frame_center