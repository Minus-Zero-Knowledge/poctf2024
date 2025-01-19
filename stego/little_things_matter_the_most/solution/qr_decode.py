import cv2


def process_image(input_path, output_path):
    image = cv2.imread(input_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_mask = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)
    processed_image = binary_mask
    cv2.imwrite(output_path, processed_image)

def detect_qr_code(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr_decoder = cv2.QRCodeDetector()
    data, points, _ = qr_decoder.detectAndDecode(gray_image)
    
    if data:
        print(f"Decoded Data: {data}")
        if points is not None:
            points = points[0].astype(int)
            for i in range(len(points)):
                next_point = points[(i + 1) % len(points)]
                cv2.line(image, tuple(points[i]), tuple(next_point), (0, 255, 0), 2)
        
        cv2.imshow("QR Code Detected", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No QR code detected.")

input_image_path = "qr_paint.png"
output_image_path = "output_image.png"
process_image(input_image_path, output_image_path)

image_path = "output_image.png"
detect_qr_code(image_path)