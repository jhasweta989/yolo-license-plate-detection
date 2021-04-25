import licence_detection
import cv2
import numpy as np
input_image = cv2.imread("car1.jpg")#give image url here
licence_detection.get_Licence_no(input_image)