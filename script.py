import cv2
import glob

images = glob.glob("*jpg")


for image in images:
    img = cv2.imread(image, 1)    
    re = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
    cv2.imshow("Hey", re)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, re)
