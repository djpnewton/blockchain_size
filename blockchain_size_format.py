#!/usr/bin/env python

import os
import json

logfile = 'blockchain_size_log.txt'
formatted_log = 'blockchain_size_fmt.txt'

def datapoint(date, values):
	d = {}
	d['date'] = date
	d['values'] = values
	return d

data = []
i = 0
c = 0
processed_btc = False
processed_eth = False
with open(logfile, 'r') as fin:
	for line in fin:
	        #i += 1
                #if processed_btc and processed_eth:
                #    if i % 10 == 0:
                #        processed_btc = False
                #        processed_eth = False
                #    else:
                #        c += 1
                #        continue
                #processed_btc = True
                #processed_eth = True
		parts = line.split(',')
                date_str = parts[0].strip('\x00')
                date = int(float(date_str))
		name = parts[1].strip()
		size = int(parts[2])
                cpu = None
                if len(parts) > 3:
                    try:
                        cpu = float(parts[3])
                    except:
                        pass
		l = len(data)-1
		if l >= 0 and data[l]['date'] == date:
			data[l]['values'].append((name, size, cpu))
		else:
			d = datapoint(date, [(name, size, cpu)])
			data.append(d)
        print c, 'passed lines'
        print 'data len', len(data)

l = len(data)
i = 0
for i in range(l-5, 0, -1):
    if i % 10:
	data.pop(i)
print 'data len', len(data)
   

with open(formatted_log, 'w') as fout:
	fout.write(json.dumps(data, indent=4))
