import matplotlib.pyplot as plt
import os

# --- Configuration ---
data_entries = []
last_x = None
last_y = None
screen_mode = True  # True = screen coordinates (0,0 top-left)
start_idx = 0       # Starting index for SV export

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# --- Plotting ---
def new_plot():
    plt.figure()
    xs = [d[0] for d in data_entries]
    ys = [d[1] for d in data_entries]
    plt.plot(xs, ys, marker='o', linestyle='-')
    plt.title("XY Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show(block=False)
    plt.pause(0.1)  # ensures the plot updates

# --- File Saving ---
def save_files():
    global start_idx
    python_path = os.path.join(output_dir, "data_python.txt")
    sv_path = os.path.join(output_dir, "data_sv.txt")

    # Python array
    with open(python_path, "w") as f_py:
        f_py.write("   # x   y   line pos\n")
        f_py.write("data_entries = [\n")
        for x, y, line, pos in data_entries:
            f_py.write(f"    ({x}, {y}, {line}, {pos}),\n")
        f_py.write("]\n")

    # SystemVerilog array
    with open(sv_path, "w") as f_sv:
        f_sv.write("            //                  x       y       line    pos\n")
        for offset, (x, y, line, pos) in enumerate(data_entries):
            idx = start_idx + offset
            f_sv.write(f"            {idx}:  data_out = {{8'd{x}, 8'd{y}, 1'b{line}, 1'b{pos}}};\n")

    print(f"Files saved in '{output_dir}':\n- {python_path}\n- {sv_path}")

# --- Mode Toggle ---
def toggle_mode():
    global screen_mode
    screen_mode = not screen_mode
    print(f"Input mode: {'Screen (0,0 top-left)' if screen_mode else 'Math (0,0 bottom-left)'}")

# --- CLI Interface ---
print("Commands:\nPOS X Y\nLIN X Y\nRESET\nPRINT\nMODE\nINDEX N\nType 'exit' to quit.")

while True:
    cmd = input("> ").strip().split()
    if not cmd:
        continue

    command = cmd[0].upper()

    if command == "EXIT":
        break

    elif command == "MODE":
        toggle_mode()

    elif command == "INDEX" and len(cmd) == 2:
        try:
            start_idx = int(cmd[1])
            print(f"SV starting index set to {start_idx}")
        except ValueError:
            print("Invalid index number.")

    elif command == "POS" and len(cmd) == 3:
        try:
            x, y = int(cmd[1]), int(cmd[2])
            if screen_mode:
                y = 255 - y
            data_entries.append((x, y, 0, 1))
            last_x, last_y = x, y
            new_plot()
        except ValueError:
            print("Invalid numbers.")

    elif command == "LIN" and len(cmd) == 3:
        try:
            x, y = int(cmd[1]), int(cmd[2])
            if screen_mode:
                y = 255 - y
            data_entries.append((x, y, 1, 0))
            last_x, last_y = x, y
            new_plot()
        except ValueError:
            print("Invalid numbers.")

    elif command == "RESET":
        if last_x is not None and last_y is not None:
            data_entries.append((last_x, last_y, 1, 1))
            new_plot()
        else:
            print("No previous coordinates to reset.")

    elif command == "PRINT":
        save_files()

    else:
        print("Unknown command.")
