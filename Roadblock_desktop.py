import threading, msvcrt
import sys
popup=''
ans=''
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
hide()

def readInput(caption, timeout = 5):
    default=2
    class KeyboardThread(threading.Thread):
        def run(self):
            self.timedout = False
            self.input = ''
            while True:
                if msvcrt.kbhit():
                    chr = msvcrt.getche()
                    if ord(chr) == 13:
                        break
                    elif ord(chr) >= 32:
                        self.input += chr
                if len(self.input) == 0 and self.timedout:
                    break    


    sys.stdout.write('%s:'%(caption));
    result = default
    it = KeyboardThread()
    it.start()
    it.join(timeout)
    it.timedout = True
    if len(it.input) > 0:
        # wait for rest of input
        it.join()
        result = it.input
    print ''  # needed to move to next line
    return result

import ctypes
import os
from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
import os
import sys
#from easygui import ynbox
import ctypes
import tkinter as tk
#from tkinter import ttk
msg='Press YES if you knowingly deleting the files.. in 3 seconds'
def placefiles(username):
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
    """# no need of hash calculation
    hashfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
    

    try:
      os.system(r'mkdir c:\roadblock\hashvalue')
    except:
      pass

    f=open(r'c:\roadblock\hashvalue'+os.sep+'Hashlist.exe',"w")
    f.write(hashfile1)
    f.close()
    """
    pass
  except Exception as ex:
    print ex
    ##sys.exit(0)

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

class myThread (threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        mypopup()
answ=5

def mypopup():
  global answ
  while True:
    if answ==2:
      answ=0
      print 'in popupraised mypopup'
      
      try:
        a=ctypes.windll.user32.MessageBoxA(0, "You have 3 seconds to answer..\nPress OK if you are knowingly deleting files.", "Ransomware Attack Detected", 1)
        answ=a
        print answ,'answwww'
        while True:
          if answ==8:
            break
          else:
            time.sleep(0.5)
      except Exception as ex:
        print ex
    else:
      time.sleep(0.5)
      pass




thread3 = myThread("popup")
thread3.start()
"""
def popupraised():
  global ans
  print 'in popupraised'
  #a=easygui.ynbox(r'Is the files deleted from you knowingly?\nYou have 3 seconds to answer..','Ransomware Attack Detected',('yes','no'))
  #return a
  
  print 'in popupraised'
  a=[]
  try:
    a.append(ctypes.windll.user32.MessageBoxA(0, "You have 3 seconds to answer..\nPress OK if you are knowingly deleting files.", "Ransomware Attack Detected", 1))

    print a[0],'a[0]'
    return a[0]
  except Exception as ex:
    print ex
  
  global msg
  popup = tk.Tk()
  popup.wm_title("Ransomware Attack Detected..")
  
  def callback1(p):
    print p,'pppp'
    ans=p
    pass
  def callback2(p):
    print p,'pppp'
    ans=p
    pass
  print 'in popupraised1'
  label = ttk.Label(popup, text=msg, font=NORM_FONT)
  label. pack(side="top", fill="x", pady=10)
  B1 = ttk.Button(popup, text="YES", command=lambda: callback1(1) and popup.destroy)
  B1.pack()
  B2 = ttk.Button(popup, text="NO", command=lambda: callback2(2) and popup.destroy)
  B2.pack()
  B3 = ttk.Button(popup, text="CLOSE", command=popup.destroy)
  B3.pack()
  popup.mainloop()
  print 'in popupraised1'
  pass
"""

def placemefiles(): # to restore files
  from glob import glob
  a=glob(r"C:\Users\*")
  for i in a:
    if os.path.isdir(i)==True:
      try:
        if i!=r'C:\Users\All Users':
          placefiles(i)
      except:
        pass

def raisenotify():
  # -- coding: utf-8 --
  try:
    class WindowsBalloonTip:
        def __init__(self, title, msg):
            message_map = {
                    win32con.WM_DESTROY: self.OnDestroy,
            }
            # Register the Window class.
            wc = WNDCLASS()
            hinst = wc.hInstance = GetModuleHandle(None)
            wc.lpszClassName = "PythonTaskbar"
            wc.lpfnWndProc = message_map # could also specify a wndproc.
            classAtom = RegisterClass(wc)
            # Create the Window.
            style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
            self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                    0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                    0, 0, hinst, None)
            UpdateWindow(self.hwnd)
            iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            try:
               hicon = LoadImage(hinst, iconPathName, \
                        win32con.IMAGE_ICON, 0, 0, icon_flags)
            except:
              hicon = LoadIcon(0, win32con.IDI_APPLICATION)
            flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
            nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
            Shell_NotifyIcon(NIM_ADD, nid)
            Shell_NotifyIcon(NIM_MODIFY, \
                             (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                              hicon, "Balloon  tooltip",title,200,msg))
            # self.show_balloon(title, msg)
            #print 'waiting for 10 sec'
            time.sleep(10)
            #print 'waiting over..'
            DestroyWindow(self.hwnd)
        def OnDestroy(self, hwnd, msg, wparam, lparam):
            nid = (self.hwnd, 0)
            Shell_NotifyIcon(NIM_DELETE, nid)
            PostQuitMessage(0) # Terminate the app.
    def balloon_tip(title, msg):
        w=WindowsBalloonTip(msg, title)


    balloon_tip('Your attention is required!','Ransomware attack has been detected on this system.')
    pass
  except:
    pass

def chngwallppr1():
  try:
    
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, r"C:\roadblock\internals\image1.exe" , 0)
  except Exception as ex:
    print ex,'112.12'
    pass


  pass

def chngwallppr():
  try:
    
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, r"C:\roadblock\internals\image.exe" , 0)
  except Exception as ex:
    print ex,'112.12'
    pass


  pass

import win32event, win32api, winerror
from _winreg import *
import time

time.sleep(3) # for ransometestingreal2.exe to delete pending files on restart
print 'Roadblock_desktop'
try:
  print 'deleting infdtc'
  os.system('del /F /Q /A '+r'C:\roadblock\internals'+os.sep+'infdtc.exe')
except Exception as ex:
  print ex
  pass

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

    #print 'checking...'
    time.sleep(1)
    #print 'checking..'
    #os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 2 /f')
    if os.path.exists(r"C:\roadblock\internals"+os.sep+'infdtc.exe')==True:
        #sys.exit(0)
        pass
    if os.path.exists(r"C:\roadblock\internals"+os.sep+'hey0.exe')==True:
        print 'hey0 exisit'
        #raw_input('..1 going to delete hey0')
        os.system('del /F /Q /A '+r"C:\roadblock\internals"+os.sep+'hey0.exe')
        print 'Infection detected'
        print "You have 5 seconds to answer!"
        answ=2
        #popupraised()
        #ans = readInput('Do you have knowingly done this..Press 1 to accept..')
        time.sleep(3)
        print answ,'answ....'
        if answ!=2 and answ!=0:
          
          f=open(r"C:\roadblock\internals"+os.sep+'hey2.exe',"w")
          f.close()
          print 'Setting Alarm as False..'
          answ=8
          #raw_input('..1 going to delete hey2')
          #placemefiles() # let it be done from privilleged ones running as service
          pass

        else:
          #answ=0
          answ=8
          f=open(r"C:\roadblock\internals"+os.sep+'hey1.exe',"w")
          f.close()
          #raw_input('..1 going to create hey1')
          try:
            chngwallppr()
          except Exception as ex:
            print ex
            print 'changing wallpaper..'
            pass
          try:
            print 'calling raisenotify'
            raisenotify()
            print 'back from raisenotify'
          except:
            print 'raising notification..'
            pass
          pass  
    else:
      pass
    if os.path.exists(r"C:\roadblock\internals"+os.sep+'completed.exe')==True:
      os.system('del /F /Q /A '+r"C:\roadblock\internals"+os.sep+'completed.exe')
      try:
        chngwallppr1()
      except:
        pass


