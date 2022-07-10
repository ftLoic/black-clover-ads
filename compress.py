import os
import cv2

for path, subdirs, files in os.walk('img'):
    for name in files:
        if name[-4:] == ".png":
            filename = os.path.join(path, name)
            new = filename.replace('.png', '.jpg')

            img = cv2.imread(filename)
            # img = cv2.resize(img, (854, 480))
            cv2.imwrite(new, img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])