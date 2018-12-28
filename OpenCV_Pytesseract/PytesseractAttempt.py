import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def main():
    original = cv2.imread('E_Testing.png', 0)
    # binary thresh it at value 100. It is now a black and white image
    ret, original = cv2.threshold(original, 100, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(original, config='--psm 10')
    print(text)



if __name__ == "__main__":
    main()



