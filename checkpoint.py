#!/usr/bin/env python3
import json
import os
import sys
import shutil
import functions
import threading
import time

config = functions.get_config()
sync_per = config["sync_period"]
#sync_per = 20
#fs_path = config['fs_path']
#path = os.path.join(fs_path,'namenode')
#print(path)

def copy_content():
	while True:
		try: 
			with open(config["path_to_namenodes"] + '/' + 'namenode.txt','r') as nfile, open(config["namenode_checkpoints"] + '/' + 'namenode_checkpoints.txt','w') as cfile:
		#read content from first file
				for line in nfile:
			#append content to second file
					cfile.write(line)
			print("Copied contents sussessfully")
			time.sleep(sync_per)
		except:
			pass	
	
def check_nn():
	while True:
		if (os.path.exists(config["path_to_namenodes"] + '/' + 'namenode.txt')) == False:
			print("hello")
			with open(config["path_to_namenodes"] + '/' + 'namenode.txt','w') as nfile, open(config["namenode_checkpoints"] + '/' + 'namenode_checkpoints.txt','r') as cfile:
		#read content from first file
				for line in cfile:
			#append content to second file
					nfile.write(line)
		print("Hi")
		time.sleep(2)

  
#timer = threading.Timer(2.0, copy_content)
#timer.start()	
#while True:
#	flag = True
#	c = 1
#	while flag:
#		check_nn()
#		time.sleep(1)
#		c += 1
#		if c == sync_per:
#			flag = False
#	copy_content()
	


# Use variable or instantly start thread
        
threading.Thread(target=copy_content).start() # Task_One()
threading.Thread(target=check_nn).start() # Task_Two()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
