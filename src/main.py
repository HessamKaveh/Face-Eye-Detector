import cv2

from detector import FaceEyeDetector
from utils import FPS, draw_detections


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open webcam.")
        return

    detector = FaceEyeDetector()
    fps_counter = FPS()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Cannot read frame.")
            break

        detections = detector.detect(frame)

        frame = draw_detections(frame, detections)

        face_count = len(detections)
        eye_count = sum(len(detection["eyes"]) for detection in detections)

        fps = fps_counter.update()

        cv2.putText(
            frame,
            f"Faces: {face_count}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Eyes: {eye_count}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"FPS: {fps:.1f}",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.imshow("Face & Eye Detector", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q") or key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
