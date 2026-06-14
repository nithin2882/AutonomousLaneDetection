import numpy as np

class SteeringController:

    def calculate_steering(self, lane_center, frame_center):

        error = lane_center - frame_center

        steering_angle = error * 0.1

        return steering_angle