# vector display development tools

THESE TOOL WERE CREATED IN ORDER TO AID THE PROCESS OF CREATING A VECTOR DISPLAY SYSTEM ON AN FPGA


#Tools:

## draw_points.py
draws x(time), y(time) and y(x) plots (points only) from an array of points [x, y]. it is to be used with a testbench module which prints x and y coordinates.

## draw_vectors.py
draws x(time), y(time) and y(x) vector plots from standardized memory array [x, y, line, pos]. it is to be used with a testbench for memory modules in the design.

## vector_memory_assembler.py
is a tool which helps with creating the ROM memory and creating vector images. available commands:
- ```POS X Y```: plots a point at specified coordinates
- ```LIN X Y```: creates a line from previous coordinates to specified coordinates
- ```RESET```: creates a memory reset at previous coordinates (double line AND pos signal) [x, y, 1, 1]
- ```PRINT```: prints the full history to two .txt files; one suited for **draw_vectors.py** and one suited for SystemVerilog ROM module 
