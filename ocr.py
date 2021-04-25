import numpy as np
from matplotlib import pyplot as plt
import cv2
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pytesseract import Output

def build_tesseract_options(psm=7):
    # tell Tesseract to only OCR alphanumeric characters
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.!0123456789"
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    # set the PSM mode
    #options += " --psm {}".format(psm)
    # return the built options string
    return options

def get_text(img):

    #img= imutils.resize(img, width= 700, height=50)
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    options = build_tesseract_options(1)
    results = pytesseract.image_to_data(rgb, output_type=Output.DICT, config= options)
    print(pytesseract.image_to_string(rgb, output_type=Output.DICT, config= options))

    texts=[]
    for i in range(0, len(results["text"])):

        # We can then extract the bounding box coordinates
        # of the text region from  the current result
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]

        # We will also extract the OCR text itself along
        # with the confidence of the text localization
        text = results["text"][i]
        conf = int(results["conf"][i])

        # filter out weak confidence text localizations
        print(results)
        if conf > -1 and text != " ":
            # We will display the confidence
            #print("Confidence: {}".format(conf))
            #print("Text: {}".format(text))
            #print("")
            texts.append(text)

            text = "".join(text).strip()
            #cv2.rectangle(img,
             #             (x, y),
              #            (x + w, y + h),
               #           (0, 0, 255), 2)
            #cv2.putText(img,
                #        text,
                 #       (x, y - 10),
                  #      cv2.FONT_HERSHEY_SIMPLEX,
                   #     1.2, (0, 255, 255), 3)
            #cv2.imshow("Image", img)
            #cv2.waitKey(0)
            return text

#image = cv2.imread("pic12.JPG")
#text= get_text(image)
#print(text,'text')
