import cv2

from lane_detector import LaneDetector
from steering_controller import SteeringController

cap = cv2.VideoCapture(0)

detector = LaneDetector()
controller = SteeringController()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    lane_img, lane_center, frame_center = detector.detect_lane(frame)

    steering = controller.calculate_steering(
        lane_center,
        frame_center
    )

    cv2.line(
        frame,
        (lane_center, 0),
        (lane_center, frame.shape[0]),
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Steering: {steering:.2f}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Robot Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()