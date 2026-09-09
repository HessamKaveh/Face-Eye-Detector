import cv2
import time


class FPS:
    def __init__(self):
        self.start_time = time.time()
        self.frames = 0
        self.fps = 0.0

    def update(self):
        self.frames += 1

        elapsed = time.time() - self.start_time

        if elapsed >= 1.0:
            self.fps = self.frames / elapsed
            self.frames = 0
            self.start_time = time.time()

        return self.fps


def draw_detections(frame, detections):
    for detection in detections:
        x, y, w, h = detection["box"]

        # Face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Face",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # Eyes
        for (ex, ey, ew, eh) in detection["eyes"]:
            cv2.rectangle(
                frame,
                (x + ex, y + ey),
                (x + ex + ew, y + ey + eh),
                (255, 0, 0),
                2
            )

    return frame
