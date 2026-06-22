import cv2

def read_qr(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return None

    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(img)

    print("QR Data:", data)

    if bbox is not None and data:
        return data.strip()

    return None