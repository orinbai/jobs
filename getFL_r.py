#!/usr/bin/python
import sys
output = {}
oldk = ''
for line in sys.stdin:
    lines = line.strip().split('\t')
    if oldk == lines[0]:
        output[oldk].append(lines[1])
    else:
        output[lines[0]] = [lines[1]]
        oldk = lines[0]

for tmp in sorted(output.keys()):
    print >>sys.stdout, '%s\t%s' % (tmp, ','.join(output[tmp]))

