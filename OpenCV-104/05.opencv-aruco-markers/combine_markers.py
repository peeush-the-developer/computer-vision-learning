import cv2
import matplotlib.pyplot as plt

folder = '../../Data/Output/Aruco_markers'
files = ['DICT_5X5_100_id24.png',
         'DICT_5X5_100_id42.png',
         'DICT_5X5_100_id66.png',
         'DICT_5X5_100_id87.png',
         'DICT_5X5_100_id70.png']
(fig, axs) = plt.subplots(nrows=2, ncols=3, figsize=(8, 8))

for i, file_ in enumerate(files):
    row = i // 3
    i = i - 3 if i > 2 else i
    image = cv2.imread(f'{folder}/{file_}')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    axs[row, i].imshow(image)
    axs[row, i].axis('off')

plt.axis('off')
plt.tight_layout()
plt.show()
