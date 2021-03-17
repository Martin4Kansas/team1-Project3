#!/usr/bin/env python

import csv
import sys

class Initializer(object):
    def __init__(self, stream):
        self.stream = stream
        self.v_zero = set()
        self.size   = 0
        
    def emit(self, value):
        sys.stdout.write("%s\n" % (value))

    def initialize(self):
        reader = csv.reader(self.stream)
        for row in reader:
            self.v_zero.add(int(row[0]))
        output = ','.join(str(val) for val in [1.0/len(self.v_zero)] * len(self.v_zero))
        with open('v.csv', "w") as outfile:  
            outfile.write(output)
        self.emit(output)
        
if __name__ == '__main__':      
    initializer = Initializer(sys.stdin)
    initializer.initialize()
  