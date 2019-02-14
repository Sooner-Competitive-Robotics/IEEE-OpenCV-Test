import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def main():
    # List of .png to compare
    pictures = ['A_Testing.jpg', 'A_Testing_90.jpg', 'A_Testing_180.jpg', 'A_Testing_270.jpg',
                'B_Testing.png', 'B_Testing_90.png', 'B_Testing_180.png', 'B_Testing_270.png',
                'C_Testing.png', 'C_Testing_90.png', 'C_Testing_180.png', 'C_Testing_270.png',
                'D_Testing.png', 'D_Testing_90.png', 'D_Testing_180.png', 'D_Testing_270.png',
                'E_Testing.png', 'E_Testing_90.png', 'E_Testing_180.png', 'E_Testing_270.png',
                'F_Testing.png', 'F_Testing_90.png', 'F_Testing_180.png', 'F_Testing_270.png']
    index = 0

    while index < 24:
        name = pictures[index]
        print(findImage(name))
        index = index + 1

    print('done')
     

def findImage(name):
    # list of letters we are looking for
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    original = cv2.imread(name, 0)

    # read the picture
    text = pytesseract.image_to_string(original, lang = "Stencil", config='-c tessedit_char_whitelist=ABCDEF --psm 10')
    best_text = text
    # rotates the image until it recognizes it as a letter. If it never does it will stop after 4 rotations
    counter = 0
    while text not in letters and counter < 4:
        # if it does not recognize the letter it will rotate the image
        original = rotate(original)
        text = pytesseract.image_to_string(original, lang = "Stencil", config='-c tessedit_char_whitelist=ABCDEF --psm 10')
        counter = counter + 1


        # Case that if the text string is more than a letter it will check the first letter to see if it's in the list
        #if len(text) >= 1 and text[0] in letters:
         #   best_text = text[0]

    return text


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



