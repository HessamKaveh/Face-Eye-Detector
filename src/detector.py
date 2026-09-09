import cv2


class FaceEyeDetector:

    def __init__(self):

        base = cv2.data.haarcascades

        self.face_cascade = cv2.CascadeClassifier(
            base + "haarcascade_frontalface_default.xml"
        )

        self.eye_cascade = cv2.CascadeClassifier(
            base + "haarcascade_eye.xml"
        )

    def detect(self, frame):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        results = []

        for (x, y, w, h) in faces:

            face_gray = gray[
                y:y+h,
                x:x+w
            ]

            eyes = self.eye_cascade.detectMultiScale(
                face_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(20, 20)
            )

            results.append(
                {
                    "box": (x, y, w, h),
                    "eyes": eyes
                }
            )

        return results
