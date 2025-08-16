import matplotlib.pyplot as plt

# --- Read data from file ---
data_entries = []
with open("../../sim/.output_files/top_rtl_results.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            parts = line.split(",")
            x = int(parts[0].split("=")[1].strip())
            y = int(parts[1].split("=")[1].strip())
            data_entries.append((x, y))
        except Exception as e:
            print(f"Skipping line: {line} ({e})")
            continue

time = list(range(len(data_entries)))
x_vals = [point[0] for point in data_entries]
y_vals = [point[1] for point in data_entries]

# --- Plotting ---
fig, axs = plt.subplots(2, 1, figsize=(20, 16))

# Top plot: x and y vs sample number
axs[0].plot(time, x_vals, label='x', color='red')
axs[0].plot(time, y_vals, label='y', color='blue')
axs[0].set_title('x and y vs Sample Number')
axs[0].set_xlabel('Sample Number')
axs[0].set_ylabel('Value')
axs[0].legend()
axs[0].grid(True)

# Bottom plot: y vs x
axs[1].scatter(x_vals, y_vals, color='purple')
axs[1].set_title('y vs x')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].grid(True)
axs[1].set_aspect('equal', adjustable='box')
axs[1].set_xlim(0, 255)
axs[1].set_ylim(0, 255)

plt.tight_layout()
plt.show()
