import os
import rawpy
import imageio
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

# Directory of image source.
SOURCE_DIR = '../Datasets/raw-images'
# Directory of target location.
TARGET_DIR = '../Datasets/raw-jpgs'
# Log file
LOG_FILE_NAME = 'conversion_log.csv'

# If target location is not present, then create.
os.makedirs(TARGET_DIR, exist_ok=True)

# Log file
log_file = "file_name, width, height, width_n, height_n\n"
counter = 0

# Iterate samples
for root, dirs, files in os.walk(SOURCE_DIR):
    for file_name in files:
        # Process dng image only
        if file_name.lower().endswith('.dng') or file_name.lower().endswith('.nef'):
            
            # Load and process
            path = os.path.join(root, file_name)
            raw = rawpy.imread(path)
            rgb = raw.postprocess()

            # Original size
            width, height = int(rgb.shape[1]), int(rgb.shape[0]) 
            width_n, height_n = width, height

            # --- half ---
            # Adjust size (half)
            # width_n, height_n = int(int(width / 2) * 1), int(int(height / 2) * 1) # the original size
            # rgb = cv2.resize(rgb, (width_n, height_n))
            
            # --- 540 ---
            # Adjust size (minimum 540 )
            # if width > height:
            #     height_n = 540
            #     width_n = int((540 / height) * width)
            # else:
            #     width_n = 540
            #     height_n = int((540 / width) * height)
            # rgb = cv2.resize(rgb, (width_n, height_n))
            
            # Save image
            imageio.imsave(os.path.join(TARGET_DIR, file_name[0:-4] + '.jpg'), rgb, quality=95)
            
            print(" Size from {}x{} to {}x{}".format(str(width), str(height), str(width_n), str(height_n)))
            
            log_file += "{},{},{},{},{}\n".format(file_name, str(width), str(height), str(width_n), str(height_n))
            
            print()
            counter += 1

    #         if counter == 20:
    #            break

    # if counter == 20:
    #    break

# save logfile
with open(LOG_FILE_NAME, "w") as fhandle:
    fhandle.write(log_file)

print('Finished.')
