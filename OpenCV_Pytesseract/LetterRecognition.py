
#from tesserocr import PyTessBaseAPI, RIL, iterate_level
import pytesseract
import cv2

from tesserocr import PyTessBaseAPI

# using version 4
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def main():

    success = 0
    # list of pictures to compare
    picturesAll = ['A_Testing.png', 'A_Testing_90.png', 'A_Testing_180.png', 'A_Testing_270.png',
                'B_Testing.png', 'B_Testing_90.png', 'B_Testing_180.png', 'B_Testing_270.png',
                'C_Testing.png', 'C_Testing_90.png', 'C_Testing_180.png', 'C_Testing_270.png',
                'D_Testing.png', 'D_Testing_90.png', 'D_Testing_180.png', 'D_Testing_270.png',
                'E_Testing.png', 'E_Testing_90.png', 'E_Testing_180.png', 'E_Testing_270.png',
                'F_Testing.png', 'F_Testing_90.png', 'F_Testing_180.png', 'F_Testing_270.png']

    pictures0 = ['A_Testing.png', 'B_Testing.png', 'C_Testing.png','D_Testing.png','E_Testing.png','F_Testing.png']
    pictures90 = ['A_Testing_90.png', 'B_Testing_90.png', 'C_Testing_90.png','D_Testing_90.png','E_Testing_90.png','F_Testing_90.png']
    pictures180 = ['A_Testing_180.png','B_Testing_180.png', 'C_Testing_180.png', 'D_Testing_180.png', 'E_Testing_180.png', 'F_Testing_180.png']
    pictures270 = ['A_Testing_270.png','B_Testing_270.png','C_Testing_270.png','D_Testing_270.png','E_Testing_270.png','F_Testing_270.png']
    picturesA = ['A_Testing.png', 'A_Testing_90.png', 'A_Testing_180.png', 'A_Testing_270.png']
    picturesB = ['B_Testing.png', 'B_Testing_90.png', 'B_Testing_180.png', 'B_Testing_270.png']
    picturesC = ['C_Testing.png', 'C_Testing_90.png', 'C_Testing_180.png', 'C_Testing_270.png']
    picturesD = ['D_Testing.png', 'D_Testing_90.png', 'D_Testing_180.png', 'D_Testing_270.png']
    picturesE = ['E_Testing.png', 'E_Testing_90.png', 'E_Testing_180.png', 'E_Testing_270.png']
    picturesF = ['F_Testing.png', 'F_Testing_90.png', 'F_Testing_180.png', 'F_Testing_270.png']

    test = ['A1.png', 'B1.png', 'C1.png', 'D1.png', 'E1.png', 'F1.png']

    pictures = picturesAll

    # Text detect all the letters
    index = 0
    
    while index <  len(pictures):

        textRead = ""
        name = pictures[index]

        letter = name[0:1]
        print("Testing " + letter)

        textRead = findImage(name, str(index))
        print(textRead)

        if (textRead == letter):
            success = success + 1
        index = index + 1

    print("Done")
    print("Number of successes: " + str(success))
    print("Success rate: " + str(success / len(pictures)))
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
    gray_image = cv2.medianBlur(gray_image, 5)
    gray_image = resize(gray_image)
    ret,thresh = cv2.threshold(gray_image, 103, 255, cv2.THRESH_BINARY) #optimal threshold 103
    cv2.imshow(windowname, thresh)

    # read the picture using Tesseract
    text = pytesseract.image_to_string(thresh, config='--psm 10')
    #return text

    # rotates image until it recognizes it as a letter. Max rotation of 4
    counter = 0
    while text not in letters and counter < 4:
        thresh = rotate(thresh)
        text = pytesseract.image_to_string(thresh, config='--psm 10')
        
        counter = counter + 1
        print("rotated")

    if text not in letters:
        print("NOT IN LETTERS")
        text = pytesseract.image_to_string(thresh, config = '-c tessedit_char_whitelist=ABCDEF --psm 10')

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

# Resize images to make them smaller
def resize(image):
    resizeFactor = 0.4

    (width, height) = image.shape[:2]
    new_size = int(width*resizeFactor), int(height*resizeFactor)
    image = cv2.resize(image, new_size)
    return image

if __name__ == "__main__":
    main()