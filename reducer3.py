#!/usr/bin/env python

import sys

from itertools import groupby
from operator import itemgetter
import json

SEP = "\t"

class Reducer(object):

    def __init__(self, stream, sep=SEP):
        self.stream   = stream
        self.sep      = sep
        self.val_dict = {}
        self.n = 1

    def emit(self, key, value):
        sys.stdout.write("%s%s%s\n" % (key, self.sep, value))

    def reduce(self):
        beta = 0.85
        for current, group in groupby(self, itemgetter(0)):
            if current not in self.val_dict.keys():
                self.val_dict[str(current)] = ((1.0-beta) / float(self.n))
            for item in group:
                self.val_dict[current] += item[1]
        for key in sorted(self.val_dict.keys()):
            self.emit(key, self.val_dict[key])
        with open('v.json', 'w') as f:
            json.dump(self.val_dict, f)

    def __iter__(self):
        for line in self.stream:
            try:
                parts = line.split(self.sep)
                if parts[0] == 'n':
                    self.n = parts[1]
                else:
                    yield parts[0], float(parts[1])
            except:
                continue

if __name__ == '__main__':
    reducer = Reducer(sys.stdin)
    reducer.reduce()
