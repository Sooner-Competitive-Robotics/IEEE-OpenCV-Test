import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def main():

    im = Image.open('E_Testing.png')
    print(im)
    text = pytesseract.image_to_string(im, config='--psm 10')
    print(text)


if __name__ == "__main__":
    main()



