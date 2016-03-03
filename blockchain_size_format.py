#!/usr/bin/env python

import json

logfile = 'blockchain_size_log.txt'
formatted_log = 'blockchain_size_fmt.txt'

def datapoint(date, values):
	d = {}
	d['date'] = date
	d['values'] = values
	return d

data = []
with open(logfile, 'r') as fin:
	for line in fin:
		parts = line.split(',')
		date = int(float(parts[0]))
		name = parts[1].strip()
		size = int(parts[2])
		l = len(data)-1
		if l > 0 and data[l]['date'] == date:
			data[l]['values'].append((name, size))
		else:
			d = datapoint(date, [(name, size)])
			data.append(d)

with open(formatted_log, 'w') as fout:
	fout.write(json.dumps(data, indent=4))
