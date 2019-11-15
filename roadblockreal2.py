# I do monitoring.. that's my job.. don't disturb me..
# todo: add autorun taking functionality every 10 days
import os
import sys
import hashlib
import win32event, win32api, winerror
import string 
import random
import malwaredeinfection
import time
from datetime import date
import datetime
import random
import subprocess
def hide():
	import win32console,win32gui
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
	return True
hide()

from glob import glob

def deletealloldfiles():
	"""
	a=glob(r"C:\roadblock\*")
	for i in a:
		if os.path.isdir(i)==False:
			try:
				i.index('the1stautodatentime')
			except:
				os.system('del /F /Q /A '+i)
				pass
			try:
				i.index('the1stwhitelistauto')
			except:
				os.system('del /F /Q /A '+i)
				pass
	"""
	try:
		from glob import glob
		a=glob(r"C:\roadblock\internals\*")
		listofresource=[r'C:\roadblock\internals'+os.sep+'roadblockreal.exe',r'C:\roadblock\internals'+os.sep+'roadblock_sysauto.exe',\
		r'C:\roadblock\internals'+os.sep+'sysauto.exe',r'C:\roadblock\internals'+os.sep+'syssys.exe',\
		r'C:\roadblock\internals'+os.sep+'sysproc.exe',r'C:\roadblock\internals'+os.sep+'syshand.exe',\
		r'C:\roadblock\internals'+os.sep+'roadblockreal2.exe',\
		r'C:\roadblock\internals'+os.sep+'roadblock_procdelete.exe',r'C:\roadblock\internals'+os.sep+'procserv.exe',r'C:\roadblock\internals'+os.sep+'roadblock_procstop.exe',\
		r'C:\roadblock\internals'+os.sep+'roadblock_procprocess.exe',r'C:\roadblock\internals'+os.sep+'roadblock_autoprocess.exe',\
		r'C:\roadblock\internals'+os.sep+'firstnet.exe',r'C:\roadblock\internals'+os.sep+'conne.exe',\
		r"C:\roadblock\internals"+os.sep+'firstnetdone.exe']
		for i in a:
			print i
			time.sleep(5)
			if os.path.isdir(i)==False:
				deletei=0
				for ku in listofresource:
					try:
						i.index(ku)
						deletei=1
					except:
						pass
					try:
						i.index('test')
						deletei=1
					except:
						pass
				if deletei==0:
					print 'deleting...',i
					try:
						os.system('del /F /Q /A '+i)
					except Exception as ex:
						print ex
						print 'inside deleting exception'
						time.sleep(5)
						pass
					time.sleep(5)
					pass
		dsdd=open(r"C:\roadblock\internals"+os.sep+'donedeletion.exe',"w")
		dsdd.write()
		dsdd.close()
	except Exception as ex:
		print ex
		print 'outside deletion exception'
		pass



	pass

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# tell if its for server or end user system , 1 for server, 2 for system
iaminwhat=1
gofordeinfection=0
countofdeinfection=0
########
#Disallowing Multiple Instance
def createmutex():
	mutex = win32event.CreateMutex(None, 1, 'mutex_var_xbozx')
	if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
		mutex = None
		print "Multiple Instance not Allowed"
		sys.exit(0)
#raw_input('place roadblockcheck.exe in system32 folder..')
"""
gettheusername=os.environ.get("USERNAME")
location1='C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Desktop'
location2='C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'
location3='C:'+os.sep+'Users'+os.sep+'hemant'
location4='C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Downloads'
location5='C:'
filename1="1aaa_crypto.txt"
filename2="eee_crypto.txt"
filename3="zzz_crypto.txt"
filename4="99hh__crypto.txt"
"""

def getuptime():
	import uptime
	

def placefiles(username):
	print 'in placefiles'
	#global location1,location2,location3,location4,location5,filename1,filename2,filename3,filename4
	#--- List of users Locations ---#
	try:
		location1=username+os.sep+'Desktop'
		location2=username+os.sep+'Documents'
		location3=username
		location4=username+os.sep+'Downloads'
		location5='C:'
	except Exception as ex:
		print ex
		##sys.exit(0)

	#--- List of files with specific names to be generated ---#
	filename1="1aaa_crypto.txt"
	filename2="eee_crypto.txt"
	filename3="zzz_crypto.txt"
	filename4="99hh__crypto.txt"


	#--- Creating specific files in particular locations ---#
	try:
		if os.path.exists(location1+os.sep+filename1)==False:
			f=open(location1+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename1)
		if os.path.exists(location1+os.sep+filename2)==False:
			f=open(location1+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename2)
		if os.path.exists(location1+os.sep+filename3)==False:
			f=open(location1+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename3)
		if os.path.exists(location1+os.sep+filename4)==False:
			f=open(location1+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	try:
		if os.path.exists(location2+os.sep+filename1)==False:
			f=open(location2+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename1)
		if os.path.exists(location2+os.sep+filename2)==False:
			f=open(location2+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename2)
		if os.path.exists(location2+os.sep+filename3)==False:
			f=open(location2+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename3)
		if os.path.exists(location2+os.sep+filename4)==False:
			f=open(location2+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)


	try:
		if os.path.exists(location3+os.sep+filename1)==False:
			f=open(location3+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename1)
		if os.path.exists(location3+os.sep+filename2)==False:
			f=open(location3+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename2)
		if os.path.exists(location3+os.sep+filename3)==False:
			f=open(location3+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename3)
		if os.path.exists(location3+os.sep+filename4)==False:
			f=open(location3+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	try:
		if os.path.exists(location4+os.sep+filename1)==False:
			f=open(location4+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename1)
		if os.path.exists(location4+os.sep+filename2)==False:
			f=open(location4+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename2)
		if os.path.exists(location4+os.sep+filename3)==False:
			f=open(location4+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename3)
		if os.path.exists(location4+os.sep+filename4)==False:
			f=open(location4+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	try:
		if os.path.exists(location5+os.sep+filename1)==False:
			f=open(location5+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename1)
		if os.path.exists(location5+os.sep+filename2)==False:
			f=open(location5+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename2)
		if os.path.exists(location5+os.sep+filename3)==False:
			f=open(location5+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename3)
		if os.path.exists(location5+os.sep+filename4)==False:
			f=open(location5+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	#--- Calculating hashes and saving it in a file placed in Temp folder
	try:
		hashfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
		

		try:
			os.system(r'mkdir c:\roadblock\hashvalue')
		except:
			pass

		f=open(r'c:\roadblock\hashvalue'+os.sep+'Hashlist.exe',"w")
		f.write(hashfile1)
		f.close()
	except Exception as ex:
		print ex
		##sys.exit(0)


#checking if running for 1st time, if yes, then place the files
def checkfirsttime():
	print 'in checkfirsttime'
	# get username folder lisitng
	from glob import glob
	a=glob(r"C:\Users\*")
	for i in a:
		if os.path.isdir(i)==True:
			try:
				if i!=r'C:\Users\All Users' and i!=r'C:\Users\Default' and i!=r'C:\Users\Default User' and i!=r'C:\Users\Public':
					placefiles(i)
			except:
				pass
		
###############################################################

#checking if roadblockcheck is present in c drivefolder, if no, then place the files
def copyransomcheck():
	haikya=os.path.exists(r'C:\roadblock\internals'+os.sep+'roadblockcheck.exe')
	## not needed as of now, will tell check software is in this folder
	"""
	if haikya==False:
		try:
			from shutil import copyfile
			copyfile(r'C:\roadblock\internals'+os.sep+'roadblockcheck.exe',r"C:\roadblock"+os.sep+'roadblockcheck.exe')
		except:
			pass
	"""
	pass
###############################################################


hashfile1=hashfile2=hashfile3=hashfile4=''

def gethashes():
	global hashfile1,hashfile2,hashfile3,hashfile4
	#### getting the hashes.....
	try:
		filewa=r"C:\roadblock\hashvalue"+os.sep+'hashlist.exe'
		f=open(filewa,"r")
		icount=0
		"""
		while True:
			icount+=1
			if icount==5:
				break
			linee=f.readline()
			linee=linee.strip()
			if icount==1:
				hashfile1=str(linee)
			elif icount==2:
				hashfile2=str(linee)
			elif icount==2:
				hashfile3=str(linee)
			elif icount==2:
				hashfile4=str(linee)
		"""
		linee=f.readline()
		linee=linee.strip()
		hashfile1=hashfile2=hashfile3=hashfile4=str(linee)
		f.close()
	except Exception as ex:
		print ex
		#sys.exit(0)

#############################################################


#### Module to monitor file and Terminate abruptly###########
import time
import ctypes
import threading
import datetime

def monitorfile(username):
	#print 'in monitorfile',username
	#print 'slee for 5 sec'
	#time.sleep(5)

	global countofdeinfection
	if countofdeinfection>1:
		#print 'no need of monitoring file now.. deinfection completed...i mean will satrt again fresh'
		return 1
	
	location1=username+os.sep+'Desktop'
	location2=username+os.sep+'Documents'
	location3=username
	location4=username+os.sep+'Downloads'
	location5='C:'
	

	#--- List of files with specific names to be generated ---#
	filename1="1aaa_crypto.txt"
	filename2="eee_crypto.txt"
	filename3="zzz_crypto.txt"
	filename4="99hh__crypto.txt"

	try:
		class myThread (threading.Thread):
			def __init__(self, threadID, name, counter):
				threading.Thread.__init__(self)
				self.threadID = threadID
				self.name = name
				self.counter = counter
			def run(self):
				#print "Starting " + self.name
				# Get lock to synchronize threads
				if self.threadID==5:
					checkforautorun()
				elif self.threadID==6:
					goingfordeinfection()
				elif self.threadID==7:
					startsysproc()
				elif self.threadID==8:
					#userconsent()
					pass
				else:
					print_time(self.name, self.counter, 3)
				# Free lock to release next thread
		"""
		def startsysproc():
			global countofdeinfection
			if countofdeinfection>1:
				print 'startsysproc not needed now..'
				return 1
			try:
				os.chdir(r'C:\roadblock\internals')
				#os.system(r'rocmon.exe /AcceptEula /Quiet /Minimized /BackingFile test /Runtime 10')
				#os.system(r'sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile test ')
				print 'sysproc running'
			except:
				pass
			pass

		def goingfordeinfection():
			global gofordeinfection,iaminwhat

			global countofdeinfection
			while True:
				if iaminwhat==1 and gofordeinfection==1:
					countofdeinfection+=1
					if countofdeinfection>1:
						print 'no need of deinfecting....'
						return 1
					print 'Terminating sysproc..'
					try:
						#os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /Terminate')
						fcd=open(r'C:\roadblock\internals'+os.sep+'infdtc.exe','a+')
						fcd.write('infection detected')
						fcd.close()
						pass
					except Exception as ex:
						print ex
						pass
					print 'Going to deinfect....................'
					malwaredeinfection.mainc()
					#sys.exit(0)
					break
					return 1
				else:
					print 'waiting for an alert'
					time.sleep(5)
			return 1


		def checkforautorun(): # this get autorun in every 15 days, so logic is correct
			global gofordeinfection
			try:
				while True:
					if gofordeinfection==1:
						break
					time.sleep(10)
					# get autorun date and time
					commdate='date /T'
					output = subprocess.check_output(commdate,shell=True)
					commtime='time /T'
					output = output.replace('\r\n','')
					nowdate= output
					output = output+'___'+subprocess.check_output(commtime,shell=True)
					output = output.replace('\r\n','')

					def calculatedatediff(y1,m1,d1,y2,m2,d2):
						from datetime import date
						d0 = date(y1, m1, d1)
						d1 = date(y2, m2, d2)
						delta = d1 - d0
						return int(delta.days)
						pass

					def takeautorunlist():
						os.system(r'C:\roadblock\internals'+os.sep+'sysauto.exe -a * * /accepteula > '+r'C:\roadblock'+os.sep+'the2ndwhitelistauto.exe')

					if os.path.exists(r"C:\roadblock"+os.sep+'concurrenttime.exe')==False:
						# check if date is >=15 than time noted in the1stautoodatetime.exe
						ghb=open(r"C:\roadblock"+os.sep+'the1stautodatentime.exe','r')
						datefirst=ghb.read().strip()
						ghb.close()

						#Mon 11/13/2017___hh:mm:ss  m/d/y
						datefirst=datefirst.split('___')[0]
						datefirst=datefirst.split(' ')[1]
						datefirst=datefirst.split(os.sep)
						m1=datefirst[0]
						d1=datefirst[1]
						y1=datefirst[2]

						nowdate=nowdate.split(' ')[1]
						nowdate=nowdate.split(os.sep)
						m2=nowdate[0]
						d2=nowdate[1]
						y2=nowdate[2]

						diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

						if diffdays>=15:
							dcf=open(r"C:\roadblock"+os.sep+'concurrenttime.exe','w')
							dcf.write(output)
							dcf.close()
							takeautorunlist()

					else:
						ghb=open(r"C:\roadblock"+os.sep+'concurrenttime.exe','r')
						datefirst=ghb.read().strip()
						ghb.close()

						#Mon 11/13/2017___hh:mm:ss  m/d/y
						datefirst=datefirst.split('___')[0]
						datefirst=datefirst.split(' ')[1]
						m1=datefirst[0]
						d1=datefirst[1]
						y1=datefirst[2]

						nowdate=nowdate.split(' ')[1]
						nowdate=nowdate.split(os.sep)
						m2=nowdate[0]
						d2=nowdate[1]
						y2=nowdate[2]

						diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

						if diffdays>=15:
							dcf=open(r"C:\roadblock"+os.sep+'concurrenttime.exe','w')
							dcf.write(output)
							dcf.close()
							takeautorunlist()






						


					
					
					try:
						os.system(r'mkdir "C:\roadblock"')
					except:
						pass
					f=open(r"C:\roadblock"+os.sep+'the1stautodatentime.exe','w')
					#f=open('C:\Windows\System32'+os.sep+'roadblock'+os.sep+'the1stautodatentime.exe','w')
					f.write(output)
					f.close()
					
					pass
			except:
				pass		

		def userconsent(): # getuserconsent
			global gofordeinfection
			try:
				while True:
					if gofordeinfection==2:
						fg=open(r"C:\roadblock\internals"+os.sep+'hey0.exe',"w")
						fg.close()
						time.sleep(10)# waiting for roadblock_desktop to return its output
						if os.path.exists(r"C:\roadblock\internals"+os.sep+'hey2.exe')==True:# user know what its doing
							checkfirsttime()
						else:
							gofordeinfection=1
						break
					time.sleep(1)
					# get autorun date and time
					
			except:
				gofordeinfection=1
				pass		
		"""
		def delkaro():
			try:
				def deleteschtask():
					try:
						os.system(r'C:\windows\System32\schtasks.exe /delete /tn roadblock_starter /f')
					except:
						pass
					pass

				
				def deletesoftwares():
					try:
						
						listofresource=[r'C:\roadblock\internals'+os.sep+'roadblockreal.exe',\
						r'C:\roadblock\internals'+os.sep+'roadblock_sysauto.exe',\
						r'C:\roadblock\internals'+os.sep+'sysauto.exe',r'C:\roadblock\internals'+os.sep+'syssys.exe',\
						r'C:\roadblock\internals'+os.sep+'sysproc.exe',r'C:\roadblock\internals'+os.sep+'syshand.exe',\
						r'C:\roadblock\internals'+os.sep+'roadblockreal2.exe',\
						r'C:\roadblock\internals'+os.sep+'roadblock_procdelete.exe',r'C:\roadblock\internals'+os.sep+'roadblock_procstop.exe',\
						r'C:\roadblock\internals'+os.sep+'MBRFilter.inf',r'C:\roadblock\internals'+os.sep+'MBRFilter.sys',\
						r'C:\roadblock\internals'+os.sep+'roadblock_procprocess.exe',r'C:\roadblock\internals'+os.sep+'roadblock_autoprocess.exe',\
						r'C:\roadblock\internals'+os.sep+'Roadblock_desktop.exe',r'C:\roadblock\internals'+os.sep+'Roadblock_conn.exe',\
						r'C:\roadblock\internals'+os.sep+'roadblock_starter.exe',r'C:\roadblock\internals'+os.sep+'syspsex.exe',\
						r'C:\roadblock\internals'+os.sep+'image.exe',r'C:\roadblock\internals'+os.sep+'syssig.exe',r'C:\roadblock\internals'+os.sep+'image1.exe']

						for ij in listofresource:
							try:
								deleteme(ij)
							except:
								pass
					except:
						pass
					pass

				def killallprocess():
					import psutil
					try:
						PROCNAMEb = ['roadblockreal.exe','roadblockreal2.exe',\
						'roadblock_sysauto.exe',\
						'sysauto.exe',\
						'sysproc.exe','syshand.exe',\
						'roadblock_procdelete.exe','procserv.exe',\
						'roadblock_procstop.exe',\
						'roadblock_autoprocess.exe','roadblock_procprocess.exe']

						for proc in psutil.process_iter():
							# check whether the process name matches
							if proc.name() in PROCNAMEb:
								try:
									proc.kill()
								except:
									pass
					except:
						pass
					pass
				def killallprocess1():
					import psutil
					try:
						PROCNAMEb = ['Roadblock_conn.exe']

						for proc in psutil.process_iter():
							# check whether the process name matches
							if proc.name() in PROCNAMEb:
								proc.kill()
					except:
						pass
					pass
				
				def uninstallmenow():
					print "Unistalling software..."
					# delete schtasks
					deleteschtask()
					# delete softwares
					killallprocess()
					try:
						os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /Terminate')
					except:
						pass
					deletesoftwares()
					# kill process

					killallprocess1()


					pass
				uninstallmenow()
			except:
				pass

			pass
		def print_time(threadName, delay, counter):
			#global hashfile1,hashfile2,hashfile3,hashfile4,location1,location2,location3,location4
			global iaminwhat,gofordeinfection
			while counter:
				time.sleep(delay)
				if gofordeinfection==1:
					break
				#print 'I am '+threadName
				if threadName=="Thread-1":
					try:
						##################################################################################
						# this code is to see the difference
						
						try:
							fcf=open(r'C:\roadblock\internals\rbchingu.exe','r')
						except:
							delkaro()
						dfg=fcf.read()
						fcf.close()
						print dfg
						yearr=dfg[3:5]
						yearr=yearr+dfg[6:8]
						monthh=dfg[19:21]
						dayy=dfg[24:26] 
						print yearr,monthh,dayy
	  
						nowx = datetime.datetime.now()

						d0 = date(int(yearr), int(monthh), int(dayy))
						d1 = date(nowx.year, nowx.month, nowx.day)
						delta = d1 - d0
						print delta.days
						if delta.days<0 or delta.days>15:
							print 'gone'
							#################################
							delkaro()
							sys.exit(0)
							#################################
						else:
							print 'alive...........'
							pass
					except Exception as ex:
						print ex
						pass
					try:
						#print 'inside try'
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
						#print location1+os.sep+filename1
						#print 'going inside if'
						#print monfile1,hashfile1
						if monfile1!=hashfile1:
							#print 'under if'
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file1'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								##malwaredeinfection.mainc()
								print location1+os.sep+filename1,'going for deinfection raised'
								gofordeinfection=2

							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l1f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass
						#print 'outside if'
						pass
						monfile1=hashlib.md5(open(location2+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file1'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location2+os.sep+filename1,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l2f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

						monfile1=hashlib.md5(open(location3+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file1'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location3+os.sep+filename1,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l3f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

						monfile1=hashlib.md5(open(location4+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file1'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location4+os.sep+filename1,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l4f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

						monfile1=hashlib.md5(open(location5+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file1'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location5+os.sep+filename1,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l5f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

					except Exception as ex:
						print 'inside exception'
						try:
							f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print iaminwhat,'iaminwhat',gofordeinfection,'gofordeinfection'
						if iaminwhat==2:
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
						elif iaminwhat==1:
							#malwaredeinfection.mainc()
							print ex,'going for deinfection raised thread1'
							gofordeinfection=2
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
						fc=open(l,'a+')
						fc.write('in ex th1')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						print iaminwhat,gofordeinfection,'iaminwhat, gofordeinfection'
						pass
				elif threadName=="Thread-2":
					#--I will montior filename2 in all 4 locations
					try:
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file2'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location1+os.sep+filename2,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l1f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

						monfile1=hashlib.md5(open(location2+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file2'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location2+os.sep+filename2,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l2f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

						monfile1=hashlib.md5(open(location3+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file2'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location3+os.sep+filename2,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l3f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

						monfile1=hashlib.md5(open(location4+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file2'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location4+os.sep+filename2,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l4f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

						monfile1=hashlib.md5(open(location5+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file2'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location5+os.sep+filename2,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l5f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							pass

					except Exception as ex:
						try:
							f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print iaminwhat,'iaminwhat',gofordeinfection,'gofordeinfection'
						if iaminwhat==2:
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
						elif iaminwhat==1:
							#malwaredeinfection.mainc()
							print ex,'going for deinfection raised th2'
							gofordeinfection=2
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
						fc=open(l,'a+')
						fc.write('in ex th2')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						pass
				elif threadName=="Thread-3":
					#--I will montior filename3 in all 4 locations
					try:
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file3'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location1+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l1f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location2+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file3'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location2+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l2f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location3+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file3'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location3+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l3f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location4+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file3'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location4+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l4f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location5+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file3'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location5+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l5f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

					except Exception as ex:
						try:
							f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print iaminwhat,'iaminwhat',gofordeinfection,'gofordeinfection'
						if iaminwhat==2:
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
						elif iaminwhat==1:
							#malwaredeinfection.mainc()
							print ex,'going for deinfection raised th3'
							gofordeinfection=2
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
						fc=open(l,'a+')
						fc.write('in ex th3')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						pass
				elif threadName=="Thread-4":
					#--I will montior filename4 in all 4 locations
					try:
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file4'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location1+os.sep+filename4,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l1f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location2+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file4'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location2+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l2f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location3+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file4'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location3+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l3f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location4+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file4'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location4+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l4f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

						monfile1=hashlib.md5(open(location5+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file4'
							if iaminwhat==2:
								a=os.system('bcdedit /set {current} safeboot network');
								b=os.system('shutdown /s /f /t 00')
								print a,b;
							elif iaminwhat==1:
								#malwaredeinfection.mainc()
								print location5+os.sep+filename3,'going for deinfection raised'
								gofordeinfection=2
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
							fc=open(l,'a+')
							fc.write('l5f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							pass

					except Exception as ex:
						try:
							f=open(r'C:\roadblock\internals'+os.sep+'Abruptroadblock.exe',"w")
							f.write('Infected Machine: Do not Turn ON')
							#f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open(r'C:\roadblock\internals'+os.sep+'timeroadblock.exe','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print iaminwhat,'iaminwhat',gofordeinfection,'gofordeinfection'
						if iaminwhat==2:
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
						elif iaminwhat==1:
							#malwaredeinfection.mainc()
							print ex,'going for deinfection raised th4'
							gofordeinfection=2
						l=os.environ['TEMP']+os.sep+'outttnowlol.exe'
						fc=open(l,'a+')
						fc.write('in ex th4')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						pass
				else:
					pass   

			#raw_input('going out of monitoring..')
			pass

		threadLock = threading.Lock()
		threads = []

		# Create new threads
		thread1 = myThread(1, "Thread-1", 5)
		thread2 = myThread(2, "Thread-2", 6)
		thread3 = myThread(3, "Thread-3", 4)
		thread4 = myThread(4, "Thread-4", 3)
		#thread5 = myThread(5, "Thread-4", 5)## only for autorun list
		#thread6 = myThread(6, "Thread-6", 6)## only for deinfection
		#thread7 = myThread(7, "Thread-7", 7)## only for starting sysproc

		# Start new Threads
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
		#thread5.start()
		#thread6.start()
		#thread7.start()

		# Add threads to thread list
		threads.append(thread1)
		threads.append(thread2)
		threads.append(thread3)
		threads.append(thread4)
		#threads.append(thread5)
		#threads.append(thread6)
		#threads.append(thread7)

		# Wait for all threads to complete
		#for t in threads:
		#	t.join()
		#print "Exiting Main Thread"
		pass
	except Exception as ex:
		print ex
		#sys.exit(0)
		pass

import multiprocessing
import time
import os
import psutil
from multiprocessing import Process, freeze_support

def daemon():
	try:
		print 'Going to execute sysproc..11111111111111111..'
		time.sleep(5)
		#os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile test')
		print 'executed sysproc....11111111111111111111111111111...'
		#sys.exit(0)
		pass
	except Exception as ex:
		print ex
		time.sleep(5)


if __name__ == '__main__':
	try:
		print 'deleting infdtc'
		os.system('del /F /Q /A '+r'C:\roadblock\internals'+os.sep+'infdtc.exe')
	except Exception as ex:
		print ex
		pass
	
	#service = multiprocessing.Process(name='my_service', target=my_service)
	#worker_1 = multiprocessing.Process(name='worker 1', target=worker)
	#worker_2 = multiprocessing.Process(target=worker) # use default name
	"""
	while True:
		print 'deleting old files'
		try:
			deletealloldfiles()
			if os.path.exists(r"C:\roadblock\internals"+os.sep+'donedeletion.exe')==True:
				print 'deletion done..'
				time.sleep(5)
				break
			else:
				pass
		except:
			pass
	"""

	#worker_1.start()
	#worker_2.start()
	#service.start()
	mymainpid=os.getpid()
	freeze_support()
	#d = multiprocessing.Process(name='daemon', target=daemon)
	#d.daemon = True
	#d.start()
	
	#cv=psutil.Process(os.getpid()).parent()
	#cv=str(cv.name())
	#print cv

	
	#raw_input('---')
	"""
	if cv=='taskeng.exe' or cv=='cmd.exe':
		createmutex()
		checkfirsttime()
		copyransomcheck()
		gethashes()
		monitorfile()
	"""
	#current_process = psutil.Process()
	#children = current_process.children(recursive=True)
	#for child in children:
	#	print('Child pid is {}'.format(child.pid))
	#else:
	#mymainpid=os.getpid()
	#randstr=str(id_generator())
	#cmdf='dir > C:\Users\Hemant\Desktop'+os.sep+'yy'+randstr+'.exe'
	###os.system(cmdf)
	try:
		createmutex()
		checkfirsttime()
		copyransomcheck()
		gethashes()
	except:
		pass
	time.sleep(5)
	# get autorunlist every 15 days
	#TODO: doing now
	"""
	# start sysproc using multiprocessing
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print 'Going to execute sysproc....'
	print mymainpid,os.getpid()
	time.sleep(5)
	d = multiprocessing.Process(name='daemon', target=daemon)
	d.daemon = True
	d.start()

	print 'Executed sysproc'

	print 'Executed sysproc'
	print 'Executed sysproc'
	print 'Executed sysproc'
	print 'Executed sysproc'
	print 'Executed sysproc'
	print 'Executed sysproc'
	print 'Executed sysproc'
	print 'Executed sysproc'
	"""
	############################################################3
	class myThreadu (threading.Thread):
		def __init__(self, i):
			threading.Thread.__init__(self)
			self.threadID = i
		def run(self):
			monitorfile(self.threadID)
			


		
		
	
	print 'out of for loop'


	def goingfordeinfection():
		global gofordeinfection,iaminwhat

		global countofdeinfection
		while True:
			print 'in deinfection...'
			if iaminwhat==1 and gofordeinfection==1:
				countofdeinfection+=1
				if countofdeinfection>1:
					print 'no need of deinfecting....'
					return 1
				print 'Terminating sysproc..'
				try:
					#os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /Terminate')
					fcd=open(r'C:\roadblock\internals'+os.sep+'infdtc.exe','a+')
					fcd.write('infection detected')
					fcd.close()
					pass
				except Exception as ex:
					print ex
					pass
				print 'Going to deinfect....................'
				malwaredeinfection.mainc()
				sys.exit(0)
				break
				return 1
			else:
				print 'waiting for an alert..'
				time.sleep(5)
		return 1

	def userconsent(): # getuserconsent
			"""
			if os.path.exists(r"C:\roadblock\internals"+os.sep+'alreadyconsent.exe')==True:
				return 1
			else:
				fg=open(r"C:\roadblock\internals"+os.sep+'alreadyconsent.exe',"w")
				fg.close()
			"""
			print 'in userconsent'
			global gofordeinfection
			try:
				while True:
					if gofordeinfection==2 and (not os.path.exists(r"C:\roadblock\internals\gome.exe")):
						try:
							jn=open(r"C:\roadblock\internals\gome.exe",'w')
							jn.close()
						except:
							pass
						try:
							os.system(r'C:\roadblock\internals'+os.sep+'syshand.exe  /accepteula> '+r'C:\roadblock\internals'+os.sep+r'handleme.exe')
							print 'got the handles..'
						except Exception as ex:
							print ex
							print '84..84..'
							pass
						try:
							fg=open(r"C:\roadblock\internals"+os.sep+'hey0.exe',"w")
							fg.close()
						except:
							pass
						time.sleep(5)# waiting for roadblock_desktop to return its output


						
						#############################################################################################################

						if os.path.exists(r"C:\roadblock\internals"+os.sep+'hey2.exe')==True:# user know what its doing
							### this is done because handles is taken twice when this code is sleeping for 5 sec as loop starts as its in thread
							delkaro=r"C:\roadblock\internals\gome.exe"
							if os.path.exists(delkaro)==True:
								try:
									os.system('del /F /Q /A '+delkaro)
								except:
									pass
							print 'deleting gome inside if'
							print 'inside if 23..23.'
							os.system('del /F /Q /A '+r"C:\roadblock\internals"+os.sep+'hey2.exe')
							gofordeinfection=0
							checkfirsttime()
							print 'in userconsent back from checkfirsttime'
						else:
							### this is done because handles is taken twice when this code is sleeping for 5 sec as loop starts as its in thread
							delkaro=r"C:\roadblock\internals\gome.exe"
							if os.path.exists(delkaro)==True:
								try:
									os.system('del /F /Q /A '+delkaro)
								except:
									pass
							print 'deleting gome inside else..'
							print 'inside else..23.23'
							gofordeinfection=1
							break

						
					time.sleep(1)
					# get autorun date and time
					
			except:
				print 'in except user consent'
				gofordeinfection=1
				pass		
	def checkforautorun(): # this get autorun in every 15 days, so logic is correct
		global gofordeinfection
		try:
			while True:
				print 'in checkautorun..'
				if gofordeinfection==1:
					break
				time.sleep(10)
				# get autorun date and time
				commdate='date /T'
				output = subprocess.check_output(commdate,shell=True)
				commtime='time /T'
				output = output.replace('\r\n','')
				nowdate= output
				output = output+'___'+subprocess.check_output(commtime,shell=True)
				output = output.replace('\r\n','')

				def calculatedatediff(y1,m1,d1,y2,m2,d2):
					from datetime import date
					d0 = date(y1, m1, d1)
					d1 = date(y2, m2, d2)
					delta = d1 - d0
					return int(delta.days)
					pass

				def takeautorunlist():
					os.system(r'C:\roadblock\internals'+os.sep+'sysauto.exe -a * * /accepteula > '+r'C:\roadblock'+os.sep+'the2ndwhitelistauto.exe')

				if os.path.exists(r"C:\roadblock"+os.sep+'concurrenttime.exe')==False:
					# check if date is >=15 than time noted in the1stautoodatetime.exe
					ghb=open(r"C:\roadblock"+os.sep+'the1stautodatentime.exe','r')
					datefirst=ghb.read().strip()
					ghb.close()

					#Mon 11/13/2017___hh:mm:ss  m/d/y
					datefirst=datefirst.split('___')[0]
					datefirst=datefirst.split(' ')[1]
					datefirst=datefirst.split(os.sep)
					m1=datefirst[0]
					d1=datefirst[1]
					y1=datefirst[2]

					nowdate=nowdate.split(' ')[1]
					nowdate=nowdate.split(os.sep)
					m2=nowdate[0]
					d2=nowdate[1]
					y2=nowdate[2]

					diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

					if diffdays>=15:
						dcf=open(r"C:\roadblock"+os.sep+'concurrenttime.exe','w')
						dcf.write(output)
						dcf.close()
						takeautorunlist()

				else:
					ghb=open(r"C:\roadblock"+os.sep+'concurrenttime.exe','r')
					datefirst=ghb.read().strip()
					ghb.close()

					#Mon 11/13/2017___hh:mm:ss  m/d/y
					datefirst=datefirst.split('___')[0]
					datefirst=datefirst.split(' ')[1]
					m1=datefirst[0]
					d1=datefirst[1]
					y1=datefirst[2]

					nowdate=nowdate.split(' ')[1]
					nowdate=nowdate.split(os.sep)
					m2=nowdate[0]
					d2=nowdate[1]
					y2=nowdate[2]

					diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

					if diffdays>=15:
						dcf=open(r"C:\roadblock"+os.sep+'concurrenttime.exe','w')
						dcf.write(output)
						dcf.close()
						takeautorunlist()






					


				
				"""
				try:
					os.system(r'mkdir "C:\roadblock"')
				except:
					pass
				f=open(r"C:\roadblock"+os.sep+'the1stautodatentime.exe','w')
				#f=open('C:\Windows\System32'+os.sep+'roadblock'+os.sep+'the1stautodatentime.exe','w')
				f.write(output)
				f.close()
				"""
				pass
		except:
			pass		

	class myThreadul (threading.Thread):
		def __init__(self, i):
			threading.Thread.__init__(self)
			self.threadID = i
		def run(self):
			if self.threadID==5:
				checkforautorun()
			elif self.threadID==6:
				goingfordeinfection()
			elif self.threadID==7:
				userconsent()
			
			
	print 'running autorun and deinfection...'

	thread1 = myThreadul(5)
	thread1.start()

	thread1 = myThreadul(6)
	thread1.start()

	thread1 = myThreadul(7)
	thread1.start()
		
	fcgh=open(r"C:\roadblock\internals"+os.sep+'firstnet.exe',"w")
	fcgh.close()

	threadLockb = threading.Lock()
	threadsb = []
	
	#if os.getpid()==mymainpid: # will check later
	from glob import glob
	a=glob(r"C:\Users\*")
	print '-------------------------'
	for i in a:
		print i
		time.sleep(5)
		if os.path.isdir(i)==True:
			try:
				if i!=r'C:\Users\All Users' and i!=r'C:\Users\Default' and i!=r'C:\Users\Default User' and i!=r'C:\Users\Public':
					print 'going to call monitorfile'
					thread1 = myThreadu(i)
					thread1.start()
					#monitorfile(i) # is called from thread
					threadsb.append(thread1)
					pass
			except:
				pass
		


	# Wait for all threads to complete
	for t in threadsb:
		t.join()