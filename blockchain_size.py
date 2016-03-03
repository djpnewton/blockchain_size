#!/usr/bin/env python

import os
import subprocess
import time

blockchains = [('bitcoin', '/home/daniel/.bitcoin', 'bitcoind'), ('ethereum', '/home/daniel/.ethereum', 'geth')]
logfile = 'blockchain_size_log.txt'

def dir_size(start_path):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	return total_size

def cpu_percent(process_name):
	#output = subprocess.check_output('ps -C %s -o %%cpu' % process_name, shell=True)
	#return output.split()[1]

	cmd = "/usr/bin/top -p $(/usr/bin/pgrep %s) -n1 | /usr/bin/tail -n3 | /usr/bin/awk '{ print $10 }'" % process_name
	output = subprocess.check_output(cmd, shell=True)
	return output.strip()

timestamp = time.time()
f = open(logfile, 'a')

for bc in blockchains:
	name = bc[0]
	path = bc[1]
        process_name = bc[2]
	size = dir_size(path)
        cpu = cpu_percent(process_name)
	entry = '%f, %s, %d, %s' % (timestamp, name, size, cpu)
	print entry
	f.write(entry)
	f.write('\n')
