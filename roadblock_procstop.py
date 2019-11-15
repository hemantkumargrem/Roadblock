import os

#os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile testhhhaaaiii')
from multiprocessing import Process, freeze_support

import multiprocessing
import time
import sys

def daemonstop():
    while True:
        if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==True:
            os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /Terminate')
            os.system(r'taskkill /IM procserv.exe /T /F')
            gff=open(r'C:\roadblock\internals'+os.sep+'sysroadblock_procstopped.exe','w')
            gff.close()
            break
        else:
            time.sleep(5)

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
hide()
import time
if __name__ == '__main__':
    freeze_support()
    try:
        print 'deleting infdtc'
        os.system('del /F /Q /A '+r'C:\roadblock\internals'+os.sep+'infdtc.exe')
    except Exception as ex:
        print ex
        pass
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



    
    from glob import glob
    a=glob(r"C:\roadblock\internals\*")
    listofresource=[r'C:\roadblock\internals'+os.sep+'roadblockreal.exe',r'C:\roadblock\internals'+os.sep+'roadblock_sysauto.exe',\
    r'C:\roadblock\internals'+os.sep+'sysauto.exe',r'C:\roadblock\internals\rbchingu.exe',r'C:\roadblock\internals'+os.sep+'syssys.exe',\
    r'C:\roadblock\internals'+os.sep+'sysproc.exe',r'C:\roadblock\internals'+os.sep+'syshand.exe',\
    r'C:\roadblock\internals'+os.sep+'checkcrypto.exe',r'C:\roadblock\internals'+os.sep+'roadblockreal2.exe',\
    r'C:\roadblock\internals'+os.sep+'nssm.exe',r'C:\roadblock\internals'+os.sep+'procserv.exe',r'C:\roadblock\internals'+os.sep+'roadblock_procstop.exe',\
    r'C:\roadblock\internals'+os.sep+'roadblock_procprocess.exe',r'C:\roadblock\internals'+os.sep+'roadblock_autoprocess.exe']
    for i in a:
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
                #os.system('del /F /Q /A '+i), deactivated , will activate later
                pass
    """
    d = multiprocessing.Process(name='daemonstop', target=daemonstop)
    d.daemon = True

    

    d.start()
    time.sleep(1)
    """

    while True:
        if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==True:
            time.sleep(5)
            os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /Terminate')
            gff=open(r'C:\roadblock\internals'+os.sep+'sysroadblock_procstopped.exe','w')
            gff.close()
            break
        else:
            time.sleep(5)
    