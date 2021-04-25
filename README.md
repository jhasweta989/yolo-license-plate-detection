# License-plate Detection by YOLO

This repository contains a method to detect **Iranian vehicle license plates** as a representation of vehicle presence in an image. We have utilized **You Only Look Once version 3 (YOLO v.3)** to detect the license plates inside an input image. The method has the advantages of high accuracy and real-time performance, according to YOLO v.3 architecture. The presented system receives a series of vehicle images and produces the processed image with added bounding-boxes containing the vehicles' license plates. The flow of how we have trained and tested the application is published in a paper accessible from the citation section.
This repositery has a method to detect number of licence plate. It use a yolo-licence-plate detection method to detect number plate. Then crop Region of interest from the image.
Then detect Text in the image using pytesseract

![Sample Output of Licence plate detection model](image.JPG "Sample Output of Licence plate detection model")

![Region of interest](roi.JPG "Region of interest")
![Text detected](no.detected.JPG "Text detected")
![Sample final Output](output.JPG "Sample final Output")

## How to employ?

You can download the weight file from [this](https://drive.google.com/file/d/1vXjIoRWY0aIpYfhj3TnPUGdmJoHnWaOc/ "this") link.

###Step to follow
run index.py
can change image in index.py to test for another image
```

## Citation

Please cite us as below formation:
1. S. Khazaee, A. Tourani, S. Soroori, A. Shahbahrami, and C. Y. Suen, “**A Real-time License-Plate Detection Method using a Deep Learning Approach**,” 2nd International Conference on Pattern Recognition and Artificial Intelligence, Zhongshan, 2020. ([link](https://users.encs.concordia.ca/~icprai20/ "link"))

## Collaborators

- [Sajjad Soroori](https://github.com/SajjadSo "Sajjad Soroori")
- [Ali Tourani](https://github.com/alitourani "Ali Tourani")
