#import win32console,win32gui
#window = win32console.GetConsoleWindow()
#win32gui.ShowWindow(window,0)

import os
def hide():
	try:
		import win32console,win32gui
		window = win32console.GetConsoleWindow()
		win32gui.ShowWindow(window,0)
		return True
	except:
		pass
hide()
try:
    os.system(r'mkdir "C:\roadblock"')
except:
    pass






print os.system(r'C:\roadblock\internals'+os.sep+'sysauto.exe -a * * /accepteula > '+r'C:\roadblock'+os.sep+'the1stwhitelistauto.exe')
#raw_input('...')
pass