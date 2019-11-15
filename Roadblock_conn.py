import os

#os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile testhhhaaaiii')
from multiprocessing import Process, freeze_support

import multiprocessing
import time
import sys
import threading




def daemonserv():
    os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile C:\roadblock\internals\test')

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
hide()
import time
import urllib2
import socket


hostu=socket.gethostname()

try:
    f=open(r'C:\roadblock\internals'+os.sep+'conne.exe',"r")
    edfr=f.read().strip()
    edfr=str(edfr)
    iptoconnect=edfr
    f.close()
except:
    iptoconnect="http://www.cyberintel.in/"
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




if __name__ == '__main__':
    freeze_support()
    try:
      print 'deleting infdtc'
      os.system('del /F /Q /A '+r'C:\roadblock\internals'+os.sep+'infdtc.exe')
    except Exception as ex:
      print ex
      pass
    time.sleep(20) # wait before starting roadblockreal2 or roadblock

    def checkfirstnet():
        while True:
            if os.path.exists(r"C:\roadblock\internals"+os.sep+'firstnet.exe')==True:# to check if its running for first time
                # firstnet.exe is created in roadblockreral2
                hostu=socket.gethostname()
                page=urllib2.urlopen(iptoconnect+"roadblock/register.php?hostname="+hostu).read()

                if page=='success':
                    print 'successfuly contacted domain..'
                    print 'creating firstnet.exe'
                    os.system('del /F /Q /A '+r"C:\roadblock\internals"+os.sep+'firstnet.exe') # just to check, this ping is done only once
                    fgv=open(r"C:\roadblock\internals"+os.sep+'firstnetdone.exe',"w") # this tell checkfirstnet function was completed successfully
                    fgv.close()
                    return 1
                    pass
                else:
                    time.sleep(60)
                    continue
            elif os.path.exists(r"C:\roadblock\internals"+os.sep+'firstnetdone.exe')==True:
                return 1
            time.sleep(60)
            pass
    
    def deleteschtask():
        try:
            os.system(r'C:\windows\System32\schtasks.exe /delete /tn roadblock_starter /f')
        except:
            pass
        pass

    def deleteme(namer):
        e=r'C:\Windows\explorer.exe'
        uj=r'C:\Windows\explorer.exe'
        if namer==e or namer==uj:
            return 1
        try:
            os.system(r'C:\Windows\System32\takeown.exe /F '+namer)
        except Exception as ex:
            pass
        try: 
            os.system(r'C:\Windows\System32\icacls.exe '+namer+r' /grant %username%:F')
        except Exception as ex:
            pass
        try:
            os.system('del /F /Q /A '+namer)
        except Exception as ex:
            pass
        try:
            os.system('ren '+namer+' rb_detect')
        except Exception as ex:
            pass
        ed=''
        try:
            lp=namer
            lp=lp.split(os.sep)
            lp[len(lp)-1]='rb_detect'
            ed=''
            for i in lp:
                ed=ed+i+os.sep
            ed=ed[0:-1]
        except Exception as ex:
            pass
        try:
            os.system('del /F /Q /A '+ed)
        except Exception as ex:
            pass

    def deletesoftwares():
        try:
            
            listofresource=[r'C:\roadblock\internals'+os.sep+'roadblockreal.exe',\
            r'C:\roadblock\internals'+os.sep+'roadblock_sysauto.exe',\
            r'C:\roadblock\internals'+os.sep+'sysauto.exe',r'C:\roadblock\internals'+os.sep+'syssys.exe',\
            r'C:\roadblock\internals'+os.sep+'sysproc.exe',r'C:\roadblock\internals'+os.sep+'syshand.exe',\
            r'C:\roadblock\internals'+os.sep+'roadblockreal2.exe',r'C:\roadblock\internals\rbchingu.exe',\
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

    def uninstallme():
        while True:
            if os.path.exists(r"C:\roadblock\internals"+os.sep+'firstnetdone.exe')==True:# to check if its running for first time
                page=urllib2.urlopen(iptoconnect+"roadblock/uninstall.php?hostname="+hostu).read()

                if page=='1':
                    uninstallmenow()
                    return 1
                else:
                    pass
            else:
                time.sleep(30)
            time.sleep(60)
            pass

    def pingme():
        while True:
            if os.path.exists(r"C:\roadblock\internals"+os.sep+'firstnetdone.exe')==True:# to check if its running for first time
                page=urllib2.urlopen(iptoconnect+"roadblock/ping.php?hostname="+hostu).read()

                if page=='success':
                    print 'Pinged successful..'
                    pass
                else:
                    pass
            else:
                time.sleep(30)
            time.sleep(60)
            pass

    def infectedping():
        while True:
            if os.path.exists(r"C:\roadblock\internals"+os.sep+'firstnetdone.exe')==True:# to check if its running for first time
                if os.path.exists(r"C:\roadblock\internals"+os.sep+'infdtc.exe')==True:
                    page=urllib2.urlopen(iptoconnect+"roadblock/infected.php?hostname="+hostu).read()

                    if page=='success':
                        print 'Infection reported..'
                        try:
                            dfcx=str(os.getpid())
                            os.system('taskkill.exe /pid '+dfcx+' /F')
                            sys.exit(0)

                        except:
                            sys.exit(0)
                            pass
                        sys.exit(0)
                        return 1
                        pass
                    else:
                        pass
            else:
                time.sleep(30)
                pass
            time.sleep(30)
            pass

    class myThreadul (threading.Thread):
        def __init__(self, i):
            threading.Thread.__init__(self)
            self.threadID = i
        def run(self):
            if self.threadID==5:
                checkfirstnet()
            elif self.threadID==6:
                uninstallme()
            elif self.threadID==7:
                pingme()
            elif self.threadID==8:
                infectedping()
            
    threadLock = threading.Lock()
    threads = []

    thread1 = myThreadul(5)
    threads.append(thread1)
    thread1.start()

    thread1 = myThreadul(6)
    threads.append(thread1)
    thread1.start()

    thread1 = myThreadul(7)
    threads.append(thread1)
    thread1.start()

    thread1 = myThreadul(8)
    threads.append(thread1)
    thread1.start()

    

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print "Exiting Main Thread"
    
    

        

