def uaac():

	import sys, os, traceback, types

	def isUserAdmin():

		if os.name == 'nt':
			import ctypes
			# WARNING: requires Windows XP SP2 or higher!
			try:
				return ctypes.windll.shell32.IsUserAnAdmin()
			except:
				traceback.print_exc()
				print "Admin check failed, assuming not an admin."
				print
				return False
		elif os.name == 'posix':
			# Check for root on Posix
			return os.getuid() == 0
		else:
			raise RuntimeError, "Unsupported operating system for this module: %s" % (os.name,)

	def runAsAdmin(cmdLine=None, wait=True):

		if os.name != 'nt':
			raise RuntimeError, "This function is only implemented on Windows."

		import win32api, win32con, win32event, win32process
		from win32com.shell.shell import ShellExecuteEx
		from win32com.shell import shellcon

		python_exe = sys.executable

		if cmdLine is None:
			cmdLine = [python_exe] + sys.argv
		elif type(cmdLine) not in (types.TupleType,types.ListType):
			raise ValueError, "cmdLine is not a sequence."
		cmd = '"%s"' % (cmdLine[0],)
		# XXX TODO: isn't there a function or something we can call to massage command line params?
		params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
		cmdDir = ''
		showCmd = win32con.SW_SHOWNORMAL
		#showCmd = win32con.SW_HIDE
		lpVerb = 'runas'  # causes UAC elevation prompt.

		# print "Running", cmd, params

		# ShellExecute() doesn't seem to allow us to fetch the PID or handle
		# of the process, so we can't get anything useful from it. Therefore
		# the more complex ShellExecuteEx() must be used.

		# procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

		procInfo = ShellExecuteEx(nShow=showCmd,
								  fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
								  lpVerb=lpVerb,
								  lpFile=cmd,
								  lpParameters=params)

		if wait:
			procHandle = procInfo['hProcess']	
			obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
			rc = win32process.GetExitCodeProcess(procHandle)
			#print "Process handle %s returned code %s" % (procHandle, rc)
		else:
			rc = None

		return rc

	def test():
		try:
			runuacpy = r'C:\roadblock\internals'+os.sep+'roadblockreal.exe'
			rc = runAsAdmin([runuacpy])
		except:
			raw_input('Admin privillege was not provided.. exiting...')
			pass



	test()

def hide():
	import win32console,win32gui
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
	return True
hide()

try:
	os.system(r'mkdir "C:\roadblock"')
except:
	pass

try:
	os.system(r'mkdir "C:\roadblock\internals"')
except:
	pass

try:
 
	rded=str(sys.argv[1]) #get the ip address with port
	rded=rded.strip()
	vgb=open(r'C:\roadblock\internals'+os.sep+'conne.exe',"w") # record the ip address
	vgb.write(rded)
	vgb.close()
except:
	pass 



############### extract roadblockreal in internals folder... startsysauto.exe ,sysauto.exe, sysproc,sysmon,syshand in same folder too..
import pefile
pe = pefile.PE('roadblock.exe')

rsrdetails=pe.DIRECTORY_ENTRY_RESOURCE

rsrdetails1=rsrdetails.entries

rsrdetails2=rsrdetails1[1]

entrytoresource=rsrdetails2.directory.entries
noofresource=len(entrytoresource)
print 'No. of resource: ',noofresource



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

for ik in range(0,noofresource):
	resourceinquestion=entrytoresource[ik]
	resourceinquestion1=resourceinquestion.directory.entries
	resourceinquestion2=resourceinquestion1[0]
	resourceinquestion2offset=resourceinquestion2.data.struct.OffsetToData
	
	resourceinquestion2offset=pe.get_offset_from_rva(resourceinquestion2offset)
	
	resourceinquestion2size=resourceinquestion2.data.struct.Size
	
	print 'Extracting ',listofresource[ik]
	
	fg11=open("roadblock.exe","rb")
	fg11.seek(resourceinquestion2offset)
	f111=open(listofresource[ik],"wb")
	f111.write(fg11.read(resourceinquestion2size))
	f111.close()
	fg11.close()

#raw_input('going to execute..')
try:
	print 'deleting infdtc'
	os.system('del /F /Q /A '+r'C:\roadblock\internals'+os.sep+'infdtc.exe')
except Exception as ex:
	print ex
	pass
uaac()
