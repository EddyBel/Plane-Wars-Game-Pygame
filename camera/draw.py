from settings import ROSE
import cv2


def drawLine(frame, point_1, point_2, color=ROSE):
    cv2.circle(frame, point_1, 10, color, 2)
    cv2.circle(frame, point_2, 10, color, 2)
    cv2.line(frame, point_1, point_2, color, 3)
