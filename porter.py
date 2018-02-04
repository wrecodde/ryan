# provide an interface to makeshift databases
# made with/as csv and json files

import json

def save(entry):
	locker = open("locker.db", "a")
	entry = json.dumps(entry)
	locker.write(entry + "\n")

def read():
	locker = open("locker.db", "r")
	table = []
	for e in locker.read().splitlines():
		table.append(json.loads(e))
	return table