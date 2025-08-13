import matplotlib.pyplot as plt

    # x   y   line pos
data_entries = [
    (0, 0, 0, 1),
    (0, 255, 1, 0),
    (255, 255, 1, 0),
    (255, 0, 1, 0),
    (0 , 0, 1, 0),
    (174, 162, 0, 1),
    (161, 147, 1, 0),
    (148, 162, 1, 0),
    (92 , 148, 0, 1),
    (80 , 165, 1, 0),
    (105, 167, 1, 0),
    (210, 98 , 0, 1),
    (208, 65 , 1, 0),
    (189, 49 , 1, 0),
    (151, 49 , 1, 0),
    (133, 68 , 1, 0),
    (118, 50 , 1, 0),
    (79 , 51 , 1, 0),
    (54 , 65 , 1, 0),
    (54 , 105, 1, 0),
    (255, 255, 1, 1),
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
