import cv2

from detector import FaceEyeDetector
from utils import draw_detections


def process_image(input_path, output_path):
    image = cv2.imread(input_path)

    if image is None:
        print(f"Error: Cannot read image: {input_path}")
        return False

    detector = FaceEyeDetector()

    detections = detector.detect(image)

    result = draw_detections(image, detections)

    face_count = len(detections)
    eye_count = sum(len(detection["eyes"]) for detection in detections)

    cv2.putText(
        result,
        f"Faces: {face_count}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        result,
        f"Eyes: {eye_count}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.imwrite(output_path, result)

    print(f"Faces detected: {face_count}")
    print(f"Eyes detected: {eye_count}")
    print(f"Output saved to: {output_path}")

    return True


if __name__ == "__main__":
    process_image(
        "images/test.jpg",
        "outputs/result.jpg"
    )
