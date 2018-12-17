import cv2
import numpy as np
from matplotlib import pyplot as plt

def proccess_image(image_path):
    img = cv2.imread(image_path,0)
    img2 = img.copy()
    calling_template = cv2.imread('image_src/new_template2.jpg',0)
    ringing_template = cv2.imread('image_src/new_template.jpg',0)
    not_answered_template = cv2.imread('image_src/not_answered_template.jpg',0)
    connecting_template = cv2.imread('image_src/new_template3.jpg', 0)

    #List of templates
    templates = [calling_template, ringing_template, not_answered_template, connecting_template]

    #Flag for templates
    template_number = 1

    for index, template in enumerate(templates):
        w, h = template.shape[::-1]

        #Threshold for recognize the image
        threshold = 0.8

        # All the 6 methods for comparison in a list
        #methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
        #            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        img = img2.copy()

        # Apply template Matching
        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #print ('min_val: ', min_val, ' max_val: ', max_val)

        if max_val >= threshold:
            return ('STATE: ' + switch(index))

            #For showing graphical. delete it for real or headless programming
            #++++++++++++++++++++++++++++++++++++++++++++++++++++
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(img,top_left, bottom_right, 255, 2)

            plt.subplot(121),plt.imshow(res,cmap = 'gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(img,cmap = 'gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle('Test')

            plt.show()
            #+++++++++++++++++++++++++++++++++++++++++++++++++++

            break
        else:
            return(True)

#Switch function for differs templates in for loop
def switch(index):
    return {
        0: 'calling',
        1: 'ringing',
        2: 'not answered' ,
        3: 'connecting',
    }[index]


if __name__ == '__main__':
    proccess_image('image_src/new_temp2.jpg')
