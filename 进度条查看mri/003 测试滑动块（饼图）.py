import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
ax.pie( [50, 50], autopct='%1.2f%%' )
plt.subplots_adjust(bottom=0.2)

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes( [0.1, 0.1, 0.8, 0.03], facecolor=axcolor )
sfreq = Slider( axfreq, 'Freq',
                0.0, 100.0,
                valfmt='% .2f',
                valinit=50, valstep=0.01 )

def update(val):
    freq = sfreq.val
    ax.clear()
    ax.pie( [freq, 100-freq], autopct='%1.2f%%' )
    fig.canvas.draw_idle()

sfreq.on_changed(update)
sfreq.reset()
sfreq.set_val(50.0)

plt.show()
