#!/usr/bin/env python

import sys

ifile = sys.argv[1]
ofile = sys.argv[2]

open(ofile, 'w').write(open(ifile).read())
