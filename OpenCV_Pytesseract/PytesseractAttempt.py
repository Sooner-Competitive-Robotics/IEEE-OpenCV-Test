import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def main():
    # List of .png to compare
    pictures = ['A_Testing', 'A_Testing_90', 'A_Testing_180', 'A_Testing_270',
                'B_Testing', 'B_Testing_90', 'B_Testing_180', 'B_Testing_270',
                'C_Testing', 'C_Testing_90', 'C_Testing_180', 'C_Testing_270',
                'D_Testing', 'D_Testing_90', 'D_Testing_180', 'D_Testing_270',
                'E_Testing', 'E_Testing_90', 'E_Testing_180', 'E_Testing_270',
                'F_Testing', 'F_Testing_90', 'F_Testing_180', 'F_Testing_270']
    index = 0

    while index < 24:
        name = pictures[index] + '.png'
        print(findImage(name))
        index = index + 1

    print('done')
     

def findImage(name):
    counter = 0
    # list of letters we are looking for
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    original = cv2.imread(name, 0)
    # binary thresh it at value 100. It is now a black and white image could be used later not sure
    # ret, original = cv2.threshold(original, 100, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(original, config='--psm 10')
    # rotates the image until it recognizes it as a letter. If it never does it will stop after 4 rotations
    best_text = text
    while text not in letters and counter < 3:
        # if it does not recognize the letter it will rotate the image
        original = rotate(original)
        text = pytesseract.image_to_string(original, config='--psm 10')
        counter = counter + 1
        # Case that if the text string is more than a letter it will check the first letter to see if it's in the list
        if len(text) >= 1 and text[0] in letters:
            best_text = text[0]

    return best_text


def rotate(image):
    # get the image height, width
    (h, w) = image.shape[:2]

    # calculate the center of the image
    center = (w/2, h/2)

    scale = 1.0

    # perform the counter clockwise rotation holding at the center
    m = cv2.getRotationMatrix2D(center, 90, scale)
    rotated90 = cv2.warpAffine(image, m, (w, h))

    return rotated90


if __name__ == "__main__":
    main()



