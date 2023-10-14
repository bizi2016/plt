# pip install nibabel
import nibabel as nib

import numpy as np
import matplotlib.pyplot as plt

# nii 来自网络公开数据
img = nib.load('mri.nii.gz')
img = img.get_fdata()
print('img.shape =', img.shape)
# img.shape = (181, 217, 181)

img = img.astype(int)

####################
# 绘制扫描图
####################

# pip install scikit-image
from skimage.util import montage

fig, ax = plt.subplots( 1, 1, figsize=(20, 20) )
ax.imshow( montage(img), cmap='bone')

fig.savefig( 'mri.nii.png',
             bbox_inches='tight',
             dpi=200,
             pad_inches=0,
             )
plt.close()
