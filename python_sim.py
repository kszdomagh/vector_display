import matplotlib.pyplot as plt

    # x   y   line pos
data_entries = [
    (150, 150, 0, 1),
    (200, 100, 1, 0),
    (190,  90, 1, 0),
    (0,     0, 0, 1),
    (254,   1, 1, 0),
    (255, 254, 1, 0),
    (0,   255, 1, 0),
    (0,     0, 1, 0),
    (250, 250, 1, 0),
    (10,  20,  1, 0),
    (0,     0, 1, 1),
]

time = list(range(len(data_entries)))
ch1 = [x for x, y, line, pos in data_entries]
ch2 = [y for x, y, line, pos in data_entries]

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

axs[0].plot(time, ch1, label='ch1 (x)', color='red')
axs[0].plot(time, ch2, label='ch2 (y)', color='blue')
axs[0].set_title('ch1 and ch2 vs Time')
axs[0].set_xlabel('time (samples)')
axs[0].set_ylabel('value')
axs[0].legend()
axs[0].grid(True)

axs[1].set_title('xy vector display')
axs[1].set_aspect('equal')
axs[1].set_xlim(-10, 265)
axs[1].set_ylim(-10, 265)
axs[1].grid(True)

last_point = None
for x, y, line, pos in data_entries:
    if pos:
        last_point = (x, y)
    elif line:
        if last_point is not None:
            axs[1].plot([last_point[0], x], [last_point[1], y], color='green')
        last_point = (x, y)

plt.tight_layout()
plt.show()
