import os
import cv2

for path, subdirs, files in os.walk('img'):
    for name in files:
        if name[-4:] == ".png":
            filename = os.path.join(path, name)

            new = filename.replace('.png', '.jpg')
            prev = filename.replace('.png', '_preview.jpg')

            new_img = cv2.imread(filename)
            prev_img = cv2.imread(filename)
            prev_img = cv2.resize(prev_img, (854, 480))

            cv2.imwrite(new, new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
            cv2.imwrite(prev, prev_img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])