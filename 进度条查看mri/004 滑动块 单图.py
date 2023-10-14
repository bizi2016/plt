####################
# 读取数据
####################

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

img = nib.load('mri.nii.gz')
img = img.get_fdata()

img = img.astype(np.uint8)

print('img.shape =', img.shape)
print('np.max(img) =', np.max(img))
print('np.min(img) =', np.min(img))
print()

print('np.unique(img) =', np.unique(img))
print()

####################
# 直方图均衡
####################

import cv2

img_hist = np.zeros(img.shape)

for i in range(len(img)):
    img_hist[i] = cv2.equalizeHist(img[i])

####################
# 三维可视化
####################

from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust( bottom=0.2 )  # 给下面留出一块

ax_layer = plt.axes( [0.1, 0.1, 0.8, 0.03] )
slider_layer = Slider( ax_layer, 'layer',
                       0, len(img)-1,
                       valfmt='%d',
                       valinit=len(img)//2, valstep=1 )

def update(val):
    ax.clear()
    ax.imshow( img_hist[slider_layer.val] )
    fig.canvas.draw_idle()

slider_layer.on_changed(update)
slider_layer.reset()
slider_layer.set_val( len(img)//2 )

plt.show()




