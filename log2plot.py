# This file is log2plot.py
# Created by Luke English 2012
#
# log2plot.py takes in a log.csv file generated by
# our implementation of MC-AIXI-CTW, and returns a
# CSV file with lines of the format
#
#          cycle,average_reward
#
# which can then be passed to PGFPlots.
# Argument 1 = in
# Argument 2 = out

import csv
import sys

f = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')
skip = int(sys.argv[3])
reader = csv.reader(f)

out.write("# ")
i=0
for row in reader:
    if(i==0):
        writing = row[0] + "\t" + row[-1] + "\n"
        out.write(writing)
    i+=1
    i = i % skip
