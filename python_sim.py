import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

    




time = np.linspace(0, 10, 1000)
ch1 = 0.5*signal.sawtooth(2*time)
ch2 = signal.sawtooth(2*time)

fig, axs = plt.subplots(2, 1, figsize=(8, 8))  # 2 rows, 1 column

axs[0].plot(time, ch1, color='red')
axs[0].plot(time, ch2, color='blue')
axs[0].set_title('vector signals')
axs[0].grid(True)

axs[1].plot(ch1, ch2, color='green')
axs[1].set_title('output xy vector display')
axs[1].set_aspect('equal')  # Force square aspect
axs[1].grid(True)
axs[1].set_xlim(-1.5, 1.5)
axs[1].set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.show()