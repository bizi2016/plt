import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

img = nib.load('mri.nii.gz')
img = img.get_fdata()

img = img.astype(int)

print('img.shape =', img.shape)
print('np.max(img) =', np.max(img))
print('np.min(img) =', np.min(img))
print()

print('np.unique(img) =', np.unique(img))
print()

####################
# 绘制直方图
####################

from matplotlib.pyplot import MultipleLocator

plt.figure( figsize=(30, 6), dpi=200 )

# 坐标刻度，每5
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(5))

img_hist = img[ img != 0 ]

plt.hist( img_hist,
          bins = np.max(img_hist)-np.min(img_hist),
          facecolor='blue',
          edgecolor='black',
          alpha=0.7,
          )

plt.title('Histogram of nii')
plt.tight_layout()
plt.savefig('hist.png', dpi=200)
plt.close()

####################
# 直方图均衡 3D
####################

def hist(img):

    hist, bins = np.histogram( img.flatten(), 256, [0, 256] )

    cdf = hist.cumsum()
    # cdf_normalized = cdf * hist.max() / cdf.max()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min())*255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img_hist = cdf[img]

    return img_hist



img = hist(img)  # 直方图均衡

####################
# 绘制扫描图
####################

# pip install scikit-image
from skimage.util import montage

fig, ax = plt.subplots( 1, 1, figsize=(20, 20) )
ax.imshow( montage(img), cmap='bone')

fig.savefig( 'mri_hist.nii.png',
             bbox_inches='tight',
             dpi=200,
             pad_inches=0,
             )
plt.close()












