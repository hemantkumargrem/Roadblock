import os
import subprocess
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
import mmap
def hide():
	import win32console,win32gui
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
	return True
hide() 
morethan5=0

def terminateproc():
	try:
		os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /Terminate')
		#os.system(r'taskkill /IM procserv.exe /T /F')
	except:
		pass
	pass
def deletepmls():
	filelist=[]

	dirpath = r'C:\roadblock\internals'

	# get all entries in the directory w/ stats
	entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
	entries = ((os.stat(path), path) for path in entries)

	# leave only regular files, insert creation date
	entries = ((stat[ST_CTIME], path)
				for stat, path in entries if S_ISREG(stat[ST_MODE]))

	#NOTE: on Windows `ST_CTIME` is a creation date 
	#  but on Unix it could be something else
	#NOTE: use `ST_MTIME` to sort by a modification date

	for cdate, path in sorted(entries):
		filetiming=time.ctime(cdate)+'$#$'+os.path.basename(path)
		filelist.append(filetiming)
	print filelist
	count=0;callproc=0
	for i in reversed(filelist):
		#print i
		try:
			i.index('.PML')
			count+=1
			print i
			filetimeandname=i
			#if count>3:##################old was 3
			filetimeandname=filetimeandname.split('$#$')
			filetimeandname=filetimeandname[1]
			i=dirpath+os.sep+filetimeandname
			#filetimeandname=filetimeandname.split('.')
			#filetimeandname=filetimeandname[0]
			os.system('del /F /Q /A '+i)
		except:
			pass
	pass
def deletefiles():
	filelist=[]

	dirpath = r'C:\roadblock\internals'

	# get all entries in the directory w/ stats
	entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
	entries = ((os.stat(path), path) for path in entries)

	# leave only regular files, insert creation date
	entries = ((stat[ST_CTIME], path)
				for stat, path in entries if S_ISREG(stat[ST_MODE]))

	#NOTE: on Windows `ST_CTIME` is a creation date 
	#  but on Unix it could be something else
	#NOTE: use `ST_MTIME` to sort by a modification date

	for cdate, path in sorted(entries):
		filetiming=time.ctime(cdate)+'$#$'+os.path.basename(path)
		filelist.append(filetiming)
	print filelist
	count=0;callproc=0
	for i in reversed(filelist):
		#print i
		try:
			i.index('.PML')
			count+=1
			print i
			filetimeandname=i
			if count>3:##################old was 3
				filetimeandname=filetimeandname.split('$#$')
				filetimeandname=filetimeandname[1]
				i=dirpath+os.sep+filetimeandname
				#filetimeandname=filetimeandname.split('.')
				#filetimeandname=filetimeandname[0]
				os.system('del /F /Q /A '+i)
		except:
			pass
	pass
countyu=0
def countnopml():
	global countyu
	filelist=[]

	dirpath = r'C:\roadblock\internals'

	# get all entries in the directory w/ stats
	entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
	entries = ((os.stat(path), path) for path in entries)

	# leave only regular files, insert creation date
	entries = ((stat[ST_CTIME], path)
				for stat, path in entries if S_ISREG(stat[ST_MODE]))

	#NOTE: on Windows `ST_CTIME` is a creation date 
	#  but on Unix it could be something else
	#NOTE: use `ST_MTIME` to sort by a modification date

	for cdate, path in sorted(entries):
		filetiming=time.ctime(cdate)+'$#$'+os.path.basename(path)
		filelist.append(filetiming)
	countyu=0
	for i in reversed(filelist):
		#print i
		try:
			i.index('.PML')
			countyu+=1
		except:
			pass
	pass
from shutil import copyfile
import shutil

def renamefiles():
	print 'inside renaming..'
	filelist=[]

	dirpath = r'C:\roadblock\internals'

	# get all entries in the directory w/ stats
	entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
	entries = ((os.stat(path), path) for path in entries)

	# leave only regular files, insert creation date
	entries = ((stat[ST_CTIME], path)
				for stat, path in entries if S_ISREG(stat[ST_MODE]))

	#NOTE: on Windows `ST_CTIME` is a creation date 
	#  but on Unix it could be something else
	#NOTE: use `ST_MTIME` to sort by a modification date

	for cdate, path in sorted(entries):
		filetiming=time.ctime(cdate)+'$#$'+os.path.basename(path)
		filelist.append(filetiming)
	print filelist
	count=0;callproc=0
	namingfile=0
	print filelist
	try:
		shutil.rmtree(dirpath+os.sep+'pmls')
	except:
		pass
	for i in reversed(filelist):
		#print i

		try:
			
			i.index('.PML')
			namingfile+=1
			count+=1
			print i
			filetimeandname=i
			filetimeandname=filetimeandname.split('$#$')
			filetimeandname=filetimeandname[1]
			i=dirpath+os.sep+filetimeandname
			#filetimeandname=filetimeandname.split('.')
			#filetimeandname=filetimeandname[0]
			os.chdir(dirpath)
			try:
				#print 'ren '+filetimeandname+' '+str(namingfile)+'.PML'
				#os.system('ren '+filetimeandname+' '+str(namingfile)+'.PML')
				print '11111'
				os.rename(filetimeandname,str(namingfile)+'.PML')
				print filetimeandname,str(namingfile)+'.PML'
				time.sleep(5)
				raw_input('11..')
				print '222222222'
				#os.rename('ren '+i+' '+dirpath+os.sep+str(namingfile)+'.PML')
				print '33333333'
				
				raw_input('22..')

				try:
					os.makedirs(dirpath+os.sep+'pmls')
				except:
					pass
				raw_input('33..')
				copyfile(dirpath+os.sep+str(namingfile)+'.PML',dirpath+os.sep+'pmls'+os.sep+str(namingfile)+'.PML')
				raw_input('44..')
				
				raw_input('55..')
				time.sleep(10)
			except Exception as ex:
				print ex
		except:
			pass
	deletepmls()
	pass

def startprocserv():
	subprocess.Popen(r'start cmd /C C:\roadblock\internals\procserv.exe', shell=True)
	pass
"""
def checkfiles():
	
	try:
		
		filelist=[]

		dirpath = r'C:\roadblock\internals'

		# get all entries in the directory w/ stats
		entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
		entries = ((os.stat(path), path) for path in entries)

		# leave only regular files, insert creation date
		entries = ((stat[ST_CTIME], path)
					for stat, path in entries if S_ISREG(stat[ST_MODE]))

		#NOTE: on Windows `ST_CTIME` is a creation date 
		#  but on Unix it could be something else
		#NOTE: use `ST_MTIME` to sort by a modification date

		for cdate, path in sorted(entries):
			filetiming=time.ctime(cdate)+'$#$'+os.path.basename(path)
			filelist.append(filetiming)
		print filelist
		count=0;callproc=0
		for i in reversed(filelist):
			#print i
			try:
				i.index('.PML')
				count+=1
				print i
				filetimeandname=i
				if count>3:
					if callproc==0:
						callproc+=1
						try:
							os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /Terminate')
							os.system(r'taskkill /IM procserv.exe /T /F')
						except:
							pass
					filetimeandname=filetimeandname.split('$#$')
					filetimeandname=filetimeandname[1]
					i=dirpath+os.sep+filetimeandname
					#filetimeandname=filetimeandname.split('.')
					#filetimeandname=filetimeandname[0]
					os.system('del /F /Q /A '+i)
		if callproc==1:
			try:
				#rename previous files
				from glob import glob
				a=glob(r"C:\roadblock\internals\*")
				for ifc in a:
					if os.path.isdir(ifc)==False:
						try:
							ifc.index('test')
							os.system(r'ren '+ifc+)
						except:
							pass
				subprocess.Popen(r'start cmd /C C:\roadblock\internals\procserv.exe', shell=True)
			except:
				pass

				

			except Exception as ex:
				#print ex
				pass
	except:
		pass
"""	


import subprocess
import os

#os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile testhhhaaaiii')
from multiprocessing import Process, freeze_support

import multiprocessing
import time
import sys
import threading
def startsysproc():
	os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile C:\roadblock\internals\test')

import time
if __name__ == '__main__':
	try:
		print 'deleting infdtc'
		os.system('del /F /Q /A '+r'C:\roadblock\internals'+os.sep+'infdtc.exe')
	except Exception as ex:
		print ex
		pass
	freeze_support()
	#time.sleep(30) # for ransometestingreal2.exe to delete pending files on restart
	#######################################################################################
	import psutil
	import time
	process_name = "roadblockreal2.exe" 

	gotransomrr2=0
	def findroadblockreal2():
		global gotransomrr2
		for proc in psutil.process_iter(): 
		    process = psutil.Process(proc.pid)# Get the process info using PID
		    pname = process.name()# Here is the process name
		    #print pname
		    #print pname,proc.pid
		    #time.sleep(1)
		    
		    if pname == process_name: 
		        gotransomrr2=1
		    else:
		        #print ("Dont have")
		        pass

	while True:
		findroadblockreal2()
		if gotransomrr2==1:
			time.sleep(5)
			break
		else:
			time.sleep(10)
			pass
	time.sleep(10)
	#############################################################################################

	while True:
		try:
			startsysproc()
			break
		except:
			pass


	class myThread (threading.Thread):
		def __init__(self, threadID):
			threading.Thread.__init__(self)
			self.threadID = threadID
		def run(self):
			print "Starting " + self.name
			# Get lock to synchronize threads
			if self.threadID==1:
				checknoofpml()

	def checknoofpml():
		global morethan5
		while True:
			if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==True:
				sys.exit(0)
				pass
			try:
			
				filelist=[]

				dirpath = r'C:\roadblock\internals'

				# get all entries in the directory w/ stats
				entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
				entries = ((os.stat(path), path) for path in entries)

				# leave only regular files, insert creation date
				entries = ((stat[ST_CTIME], path)
							for stat, path in entries if S_ISREG(stat[ST_MODE]))

				#NOTE: on Windows `ST_CTIME` is a creation date 
				#  but on Unix it could be something else
				#NOTE: use `ST_MTIME` to sort by a modification date

				for cdate, path in sorted(entries):
					filetiming=time.ctime(cdate)+'$#$'+os.path.basename(path)
					filelist.append(filetiming)
				print filelist
				count=0;callproc=0
				for i in reversed(filelist):
					#print i
					try:
						i.index('.PML')
						count+=1
					except:
						pass

				if count>2:########################################################
					morethan5=1
					#break
					if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==True:
						sys.exit(0)
					pass
				time.sleep(20)

			
			except:
				pass
		pass

	threadLock = threading.Lock()
	# Create new threads
	thread1 = myThread(1)
	# Start new Threads
	thread1.start()

	################################################################333
	
	while True:
		print morethan5,'morethan5'
		if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==True:
			sys.exit(0)
		if morethan5==1:
			morethan5=0
			if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==False: # means machine not yet infected
				print 'terminatining..'
				terminateproc()
				time.sleep(5)
				print 'deleting..'
				deletefiles() # for 1st version, later will do it
				#print 'renaming...'
				time.sleep(1)
				#renamefiles() # for 1st version, later will activate
				while True:
					countnopml()
					print countyu,'countyu'
					if countyu==0:
						break
					else:
						countnopml()

				print 'starting server'
				startsysproc()
				pass
				pass
			else:
				sys.exit(0)
		else:
			time.sleep(5)
			pass
