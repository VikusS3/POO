import cv2
import os
import numpy as np

input_images_path = "C:/Saul/fondos de pantalla"

files_names = os.listdir(input_images_path)


for file_name in files_names:
    # print(file_name)
    
    if file_name.split(".")[-1] not in ["jpg", "png", "jpeg"]:
        continue
    
    image_path = input_images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    
    if image is None:
        continue
    
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    
# cv2.destroyAllWindows()


