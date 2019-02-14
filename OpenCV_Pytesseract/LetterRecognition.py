import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def main():

    # list of pictures to compare
    pictures = ['A_Testing.png', 'A_Testing_90.png', 'A_Testing_180.png', 'A_Testing_270.png',
                'B_Testing.png', 'B_Testing_90.png', 'B_Testing_180.png', 'B_Testing_270.png',
                'C_Testing.png', 'C_Testing_90.png', 'C_Testing_180.png', 'C_Testing_270.png',
                'D_Testing.png', 'D_Testing_90.png', 'D_Testing_180.png', 'D_Testing_270.png',
                'E_Testing.png', 'E_Testing_90.png', 'E_Testing_180.png', 'E_Testing_270.png',
                'F_Testing.png', 'F_Testing_90.png', 'F_Testing_180.png', 'F_Testing_270.png']

    # Text detect all the letters
    index = 0
    while index < 24:
        if (index <4):
            print("Testing A")
        elif (index <8):
            print("Testing B")
        elif (index <12):
            print("Testing C")
        elif (index <16):
            print("Testing D")
        elif (index <20):
            print("Testing E")
        elif (index <24):
            print("Testing F")
        name = pictures[index]
        print(findImage(name, str(index)))
        index = index + 1

    print("Done")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def findImage(name, windowname):
    # list of letters we are looking for
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    
    # read image
    image = cv2.imread(name)
    # convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = crop(gray_image)
    ret,thresh = cv2.threshold(gray_image, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow(windowname, thresh)

    # read the picture using Tesseract
    text = pytesseract.image_to_string(thresh, lang = "Stencil",  config='-c tessedit_char_whitelist=ABCDEF --psm 10')

    # rotates image until it recognizes it as a letter. Max rotation of 4
    counter = 0
    while text not in letters and counter < 4:
        thresh = rotate(thresh)
        text = pytesseract.image_to_string(thresh, lang = "Stencil", config='-c tessedit_char_whitelist=ABCDEF --psm 10')
        counter = counter + 1

    return text

# rotates image 90 degrees
def rotate(image):
    # get image height and width
    (h, w) = image.shape[:2]
    # get the center of the image
    center = (w/2, h/2)

    scale = 1.0

    m = cv2.getRotationMatrix2D(center, 90, scale)
    rotated90 = cv2.warpAffine(image, m, (w, h))

    return rotated90

# crops outer edges
def crop(image):
    # image dimensions
    (x,y) = image.shape[:2]
    numCrop = 50

    # crop image
    cropped = image[numCrop:x-numCrop, numCrop:y-numCrop]

    return cropped

if __name__ == "__main__":
    main()