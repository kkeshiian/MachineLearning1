import os
import numpy as np
from PIL import Image

input_folder = "../dataset"
output_folder = "../dataset_after_preprocess"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        path = os.path.join(input_folder, filename)
        img = Image.open(path)
        
        # grayscale
        img = img.convert("L")
        
        # resize 256x256
        img = img.resize((256, 256))

        img.save(os.path.join(output_folder, filename))

print("Selesai preprocessing")