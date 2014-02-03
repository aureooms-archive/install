#!/usr/bin/python
import sys
import os
import subprocess
		
class CommandBuilder:
	
	def __init__(self,dir):
		self.dir = dir + '/'
			
	def parse(self, output):
		scripts = os.listdir(self.dir)
		for file in scripts:
			if os.path.isdir(self.dir+file):
				sub = CommandBuilder(self.dir+file)
				sub.parse(output)

			else:
				output[file] = self.dir+file;

	
if __name__ == '__main__':

	register = {}
	CommandBuilder('part').parse(register)

	if(len(sys.argv) == 1):
		for key in register:
			#print [register[key]]
			subprocess.call([register[key]])

	else:
		for i in range(1, len(sys.argv)):
			#print [register[sys.argv[i]]]
			subprocess.call([register[sys.argv[i]]])
