import cv2

def scan_camera():

    cap = cv2.VideoCapture(0)

    detector = cv2.QRCodeDetector()

    while True:

        ret, frame = cap.read()

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            cap.release()
            cv2.destroyAllWindows()
            return data

        cv2.imshow("QR Scanner", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()