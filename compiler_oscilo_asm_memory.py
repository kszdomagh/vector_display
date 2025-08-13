import matplotlib.pyplot as plt

data_entries = []
last_x = None
last_y = None

def new_plot():
    plt.figure()
    xs = [d[0] for d in data_entries]
    ys = [d[1] for d in data_entries]
    plt.plot(xs, ys, marker='o', linestyle='-')
    plt.title("XY Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show(block=False)  # Show without blocking input

def save_files():
    # Python array format
    with open("data_python.txt", "w") as f_py:
        f_py.write("   # x   y   line pos\n")
        f_py.write("data_entries = [\n")
        for x, y, line, pos in data_entries:
            f_py.write(f"    ({x}, {y} , {line}, {pos}),\n")
        f_py.write("]\n")

    # SystemVerilog format
    with open("data_sv.txt", "w") as f_sv:
        f_sv.write("            //                  x       y       line    pos\n")
        for idx, (x, y, line, pos) in enumerate(data_entries):
            f_sv.write(f"            4'd{idx}:  data_out = {{8'd{x}, 8'd{y}, 1'b{line}, 1'b{pos}}};\n")

    print("Files saved: data_python.txt, data_sv.txt")

print("Commands:\nPOS X Y\nLIN X Y\nRESET\nPRINT\nType 'exit' to quit.")

while True:
    cmd = input("> ").strip().split()

    if not cmd:
        continue
    if cmd[0].lower() == "exit":
        break

    if cmd[0].upper() == "POS" and len(cmd) == 3:
        try:
            x, y = int(cmd[1]), int(cmd[2])
            data_entries.append((x, y, 0, 1))
            last_x, last_y = x, y
            new_plot()
        except ValueError:
            print("Invalid numbers.")

    elif cmd[0].upper() == "LIN" and len(cmd) == 3:
        try:
            x, y = int(cmd[1]), int(cmd[2])
            data_entries.append((x, y, 1, 0))
            last_x, last_y = x, y
            new_plot()
        except ValueError:
            print("Invalid numbers.")

    elif cmd[0].upper() == "RESET" and len(cmd) == 1:
        if last_x is not None and last_y is not None:
            data_entries.append((last_x, last_y, 1, 1))
            new_plot()
        else:
            print("No previous coordinates to reset.")

    elif cmd[0].upper() == "PRINT":
        save_files()

    else:
        print("Unknown command.")
