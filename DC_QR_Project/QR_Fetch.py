# QR_Fetch

# pip install opencv-python pyzbar - Required libraries

import cv2
from pyzbar.pyzbar import decode
 
# Load the image (replace with your image path)
image_path = 'Labsmart_bill.jpg'  # Ensure the image is in the same directory or provide the full path
image = cv2.imread(image_path)
 
# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale for better QR code detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # Decode QR codes in the image
    qr_codes = decode(gray)
 
    if qr_codes:
        for qr in qr_codes:
            data = qr.data.decode('utf-8')
            rect = qr.rect
            print(f"QR Code Data: {data}")
            print(f"Position: {rect}")
 
            # Draw a rectangle around the detected QR code
            x, y, w, h = rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
        # Display the image with detected QR codes
        cv2.imshow('QR Code Detection', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No QR code found in the image.")