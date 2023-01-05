from settings import SCREEN, FACE_POINT_BOTTOM, FACE_POINT_CENTER, FACE_POINT_LEFT, FACE_POINT_RIGHT, FACE_POINT_TOP, ROSE, WHITE, GREEN, MAX_ANGLE, MIN_ANGLE, BLUE, KEY_DELETE
from camera.draw import drawLine
from camera.utils import obtainCoordinates, scale
import cv2
import mediapipe as mp
import math

# Camera
camera = cv2.VideoCapture(0)
camera.set(3, SCREEN[0])
camera.set(4, SCREEN[1])

my_face_mesh = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils
faceMaping = my_face_mesh.FaceMesh(max_num_faces=1)


async def viewCamera(view_window_of_camera: bool = True, view_maping_in_face: bool = False, print_values: bool = True):

    # read frames of camera
    ret, frame = camera.read()

    # get size of frame
    height, width, _ = frame.shape

    # validate if frame is not null
    if ret:
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        response = faceMaping.process(frameRGB)
        pointsOfTheFace = response.multi_face_landmarks

        if pointsOfTheFace is not None:
            for face_landmarks in pointsOfTheFace:
                bottom = obtainCoordinates(
                    FACE_POINT_BOTTOM, face_landmarks, width, height)
                top = obtainCoordinates(
                    FACE_POINT_TOP, face_landmarks, width, height)
                left = obtainCoordinates(
                    FACE_POINT_LEFT, face_landmarks, width, height)
                right = obtainCoordinates(
                    FACE_POINT_RIGHT, face_landmarks, width, height)

                drawLine(frame, bottom, top, ROSE)
                drawLine(frame, left, right, WHITE)

                radians = math.atan2(bottom[1] - top[1], bottom[0] - top[0])
                degrens = math.degrees(radians)
                degrens = round(degrens)
                value = scale(MAX_ANGLE, MIN_ANGLE, degrens)

                radians_y = math.atan2(left[1] - right[1], left[0] - right[0])
                degrens_y = math.degrees(radians_y)
                degrens_y = round(degrens_y)
                value_y = scale(MAX_ANGLE, MIN_ANGLE, degrens)

                if view_maping_in_face:
                    mp_draw.draw_landmarks(
                        frame,
                        face_landmarks,
                        my_face_mesh.FACEMESH_CONTOURS,
                        mp_draw.DrawingSpec(
                            color=GREEN, thickness=1, circle_radius=1),
                        mp_draw.DrawingSpec(color=GREEN, thickness=1, circle_radius=1))

        if print_values:
            try:
                cv2.putText(frame,
                            "Value-X: {}".format(round(value, 2)),
                            (0, 30),
                            cv2.QT_FONT_NORMAL,
                            1,
                            BLUE)
                cv2.putText(frame,
                            "Angle-X: {}".format(int(degrens)),
                            (0, 60),
                            cv2.QT_FONT_NORMAL,
                            1,
                            BLUE)
                cv2.putText(frame,
                            "Value-Y: {}".format(round(value_y, 2)),
                            (0, 90),
                            cv2.QT_FONT_NORMAL,
                            1,
                            BLUE)
                cv2.putText(frame,
                            "Angle-Y: {}".format(int(degrens_y)),
                            (0, 120),
                            cv2.QT_FONT_NORMAL,
                            1,
                            BLUE)
            except:
                cv2.putText(frame,
                            "Face not found",
                            (100, 50),
                            cv2.QT_FONT_NORMAL,
                            1,
                            BLUE)

        if view_window_of_camera:
            cv2.imshow("Camara", frame)
            if cv2.waitKey(1) == KEY_DELETE:
                try:
                    return {
                        "frame": frame,
                        "is_loop": True,
                        "value": float(value)
                    }
                except:
                    return {
                        "frame": frame,
                        "is_loop": True,
                        "value": 0
                    }
        try:
            return {
                "frame": frame,
                "is_loop": False,
                "value": float(value)
            }
        except:
            return {
                "frame": frame,
                "is_loop": False,
                "value": 0
            }
    return {
        "frame": None,
        "is_loop": False,
        "value": 0
    }
