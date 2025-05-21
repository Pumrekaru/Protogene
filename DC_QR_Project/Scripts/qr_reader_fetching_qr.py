# pip install qreader
from qreader import QReader
import cv2


image_path = r'C:\Users\bmkug\Desktop\qr\Protogene\DC_QR_Project\Inputs\dataset\images_test\img3.jpg'  # Replace with your actual image path
img = cv2.imread(image_path)


detector = QReader()


decoded_qrs, qr_locations = detector.detect_and_decode(image=img, return_detections=True)


for i, (decoded_qr, qr_location) in enumerate(zip(decoded_qrs, qr_locations)):
    print(f"QR {i+1}: {decoded_qr}")
    print(f"QR {i+1} position: x: {qr_location['cxcyn'][0]}, y: {qr_location['cxcyn'][1]}")
