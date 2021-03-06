import numpy as np
from PIL import Image
for i in range(1,4):
    img = Image.open(f'lunar_images/lunar0{i}_raw.jpg')
    data = np.array(img)
    data = data - data.min()
    improved_data = data / data.max() * 255
    improved_data = np.array(improved_data, dtype=np.uint8)
    res_img = Image.fromarray(improved_data)
    res_img.save(fp=f'better0{i}.jpg')