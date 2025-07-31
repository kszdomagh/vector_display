# vector_display
my humble way of creating a vector display system from scratch 

this python script is to be used as an aid for creation of vector graphics for 8bit x and y channels (osciloscope XY mode use). data format is as followed:
            data = {[8]x, [8]Y, [1]LINE, [1]POS};


python_sim.py - simulation of analog voltage signal levels for 2 channels with graphs showing the xy output, ch1 and ch2; the script takes coordinate inputs for points (x1, y1) and plots the line from the previous point to the next using breshenham’s algorithm
