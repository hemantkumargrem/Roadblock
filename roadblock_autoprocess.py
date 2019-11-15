import os
import subprocess
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
import mmap

import contextlib

import argparse

from Evtx.Evtx import FileHeader

from Evtx.Views import evtx_file_xml_view
import time
treestore=[]
searchfor='' # nouse
strr=''

searchitem='' # stores the actual suspicious pid

processidtodelete=[]
processname=[]

getparentname=''
count=1

treefromsysmonready=0

deletedbysysproc=0
deletedbyhandles=0


susphandleprocess=[]
import psutil

from shutil import copyfile
import datetime
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
hide()
def killme(pid):
    try:
        os.system('Taskkill /PID '+str(pid)+' /F')
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
        lp[len(lp)-1]='j'
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

def quarantinebyname(nameofp):
    gth=open(r"C:\roadblock\internals\quarantine\quarantinelog.exe",'a+')
    try:
        nameofprocecss=nameofp
        print nameofprocecss,'--quarantinebyname'
        try:
            try:
                nameofprocecss.index('roadblock')# just to hinder deleting any roadblock file, but will remove and make it random in future
                return 1
            except:
                pass
            if nameofprocecss.startswith(r'C:\Windows\System32\svchost.exe'): # only to deal with svchost
                pass
            elif nameofprocecss.startswith(r'System'): # only to deal with svchost
                pass
            elif nameofprocecss.startswith(r'C:\Windows\System32'): # don't delete any process resiiidng in system32 folder
                pass
            elif nameofprocecss.startswith(r'C:\roadblock'): # don't delete any process resiiidng in system32 folder
                pass
            elif nameofprocecss.startswith(r'C:\Windows\explorer.exe'): # don't delete any process resiiidng in system32 folder
                pass
            else:
                # saving in quartine fodler
                try:
                    klj=nameofprocecss
                    klj=klj.split(os.sep)
                    klj=klj[len(klj)-1]# get the process name without path
                    klj=klj.split('.')
                    klj=klj[0]
                    klj=str(klj)
                    sxs=datetime.datetime.now()
                    sxs=str(sxs)
                    sxs=sxs.replace('-','_')
                    sxs=sxs.replace(':','_')
                    sxs=sxs.replace(' ','$$')
                    sxs=sxs.split('.')
                    sxs=str(sxs[0])
                    klj=klj+'#$'+sxs#new processnamewithdate
                    copyfile(nameofprocecss,r"C:\roadblock\internals\quarantine"+os.sep+klj)
                    print r"C:\roadblock\internals\quarantine"+os.sep+klj,'copied'
                    gth.write(klj+'#$#@'+str(nameofprocecss)+'\n')
                    try:
                        print 'trying to delete by name..',nameofprocecss
                        try:
                            deleteme(nameofprocecss)
                        except Exception as ex:
                            print ex,'fecc..cd'
                            pass
                        os.system('del /F /Q /A '+nameofprocecss)
                    except Exception as ex:
                        print ex
                        pass
                except:
                    pass
        except:
            pass

    except:
        pass
    gth.close()

def quarantine(pid):
    """
    try:
        os.system(r'mkdir "C:\roadblock\internals\quarantine"')
    except:
        pass
    """
    try:
        p=psutil.Process(pid)
    except Exception as ex:
        return

    gth=open(r"C:\roadblock\internals\quarantine\quarantinelog.exe",'a+')
    
    try:
        nameofprocecss=p.exe()
        print nameofprocecss,'--'
        try:
            try:
                nameofprocecss.index('roadblock')# just to hinder deleting any roadblock file, but will remove and make it random in future
                return 1
            except:
                pass
            if nameofprocecss.startswith(r'C:\Windows\System32\svchost.exe'): # only to deal with svchost
                parentid=p.ppid()
                parentid=psutil.Process(parentid)
                nameofparentprocess=parentid.exe()
                if nameofparentprocess.startswith(r'C:\Windows\System32\services.exe'):
                    pass
                else:
                    # saving in quartine fodler
                        
                    try:
                        klj=nameofprocecss
                        klj=klj.split(os.sep)
                        klj=klj[len(klj)-1]# get the process name without path
                        klj=klj.split('.')
                        klj=klj[0]
                        klj=str(klj)
                        sxs=datetime.datetime.now()
                        sxs=str(sxs)
                        sxs=sxs.replace('-','_')
                        sxs=sxs.replace(':','_')
                        sxs=sxs.replace(' ','$$')
                        sxs=sxs.split('.')
                        sxs=str(sxs[0])
                        klj=klj+'#$'+sxs#new processnamewithdate
                        copyfile(nameofprocecss,r"C:\roadblock\internals\quarantine"+os.sep+klj)
                        gth.write(klj+'#$#@'+str(nameofprocecss)+'\n')
                    except:
                        pass
                    killme(pid)
            elif nameofprocecss.startswith(r'C:\Windows\System32'): # don't delete any process resiiidng in system32 folder
                pass
            elif nameofprocecss.startswith(r'C:\roadblock'): # don't delete any process resiiidng in system32 folder
                pass
            elif nameofprocecss.startswith(r'C:\Windows\explorer.exe'): # don't delete any process resiiidng in system32 folder
                pass
            elif nameofprocecss.startswith(r'System'): # don't delete any process resiiidng in system32 folder
                pass
            else:
                # saving in quartine fodler
                try:
                    klj=nameofprocecss
                    klj=klj.split(os.sep)
                    klj=klj[len(klj)-1]# get the process name without path
                    klj=klj.split('.')
                    klj=klj[0]
                    klj=str(klj)
                    sxs=datetime.datetime.now()
                    sxs=str(sxs)
                    sxs=sxs.replace('-','_')
                    sxs=sxs.replace(':','_')
                    sxs=sxs.replace(' ','$$')
                    sxs=sxs.split('.')
                    sxs=str(sxs[0])
                    klj=klj+'#$'+sxs#new processnamewithdate
                    copyfile(nameofprocecss,r"C:\roadblock\internals\quarantine"+os.sep+klj)
                    gth.write(klj+'#$#@'+str(nameofprocecss)+'\n')
                except:
                    pass

                killme(pid)
                try:
                    print 'trying to delete',nameofprocecss
                    try:
                        deleteme(nameofprocecss)
                    except Exception as ex:
                        print ex,'fecc..cd'
                        pass
                    os.system('del /F /Q /A '+nameofprocecss)
                except Exception as ex:
                    print ex
                    pass
        except:
            pass

    except:
        pass
    gth.close()
    pass

import ctypes

def takeautorunlist():
    os.system(r'C:\roadblock\internals'+os.sep+'sysauto.exe -a * * /accepteula > '+r'C:\roadblock'+os.sep+'infectedauto.exe')
    

def deinfectautoruns():
    global gofordeinfection
    time.sleep(10)
    takeautorunlist()
    try:
        #os.system(r'C:\roadblock\internals'+os.sep+'sysauto.exe -a /accepteula > '+r'C:\roadblock'+os.sep+'infectedauto.exe')

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

        # check if 2ndwhitelist date is around 10 dat\ys before than today, then deinfect using that

        if os.path.exists(r"C:\roadblock"+os.sep+'concurrenttime.exe')==False: # this means only first whitelist is available
            # 
            #takeautorunlist()

            fv1=open(r"C:\roadblock"+os.sep+'infectedauto.exe','r')
            fv1s=fv1.read()
            fv1.close()


            fv2=open(r"C:\roadblock"+os.sep+'the1stwhitelistauto.exe','r')
            fv2s=fv2.read()
            fv2.close()



            import string
            printable = set(string.printable)
            fv1s=filter(lambda x: x in printable,fv1s)
            fv2s=filter(lambda x: x in printable,fv2s)
            #fv1s=fv1s.split('\r\n')# infected one
            #fv2s=fv1s.split('\r\n')

            listofsofttodel=[]

            fv1s=fv1s.split('\r\n')
            fv2s=fv2s.split('\r\n')

            fv1snospace=[]
            fv2snospace=[]

            for sw1 in fv1s:
                fv1snospace.append(sw1.lstrip())

            for sw1 in fv2s:
                fv2snospace.append(sw1.lstrip())


            for sw1 in fv1snospace:
                if sw1.startswith('c:'+os.sep) and sw1 not in fv2snospace:
                    sw1=sw1.replace('\r\n','')
                    sw1=sw1.strip()
                    listofsofttodel.append(sw1)


            print listofsofttodel

            for jk in listofsofttodel:
                try:
                    jk.index('.exe')
                    quarantinebyname(jk)
                except Exception as ex:
                    print ex

        else: # need to check 2nd whitelist creation time
            #takeautorunlist()

            fv1=open(r"C:\roadblock"+os.sep+'the2ndwhitelistauto.exe','r')
            fv1s=fv1.read()
            fv1.close()


            fv2=open(r"C:\roadblock"+os.sep+'the1stwhitelistauto.exe','r')
            fv2s=fv2.read()
            fv2.close()



            import string
            printable = set(string.printable)
            fv1s=filter(lambda x: x in printable,fv1s)
            fv2s=filter(lambda x: x in printable,fv2s)
            #fv1s=fv1s.split('\r\n')# infected one
            #fv2s=fv1s.split('\r\n')

            listofsofttodel=[]

            fv1s=fv1s.split('\r\n')
            fv2s=fv2s.split('\r\n')

            fv1snospace=[]
            fv2snospace=[]

            for sw1 in fv1s:
                fv1snospace.append(sw1.lstrip())

            for sw1 in fv2s:
                fv2snospace.append(sw1.lstrip())


            for sw1 in fv1snospace:
                if sw1.startswith('c:'+os.sep) and sw1 not in fv2snospace:
                    sw1=sw1.replace('\r\n','')
                    sw1=sw1.strip()
                    listofsofttodel.append(sw1)


            print listofsofttodel

            
            for jk in listofsofttodel:
                try:
                    jk.index('.exe')
                    quarantinebyname(jk)
                except Exception as ex:
                    print ex
    except Exception as ex:
        print ex
        raw_input('---------------------')
        pass
    pass
### code will come here that will hint malware detected
#TODO or call mainc(), i guess mainc will be better
######################################################
            
import os

#os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile testhhhaaaiii')
from multiprocessing import Process, freeze_support

import multiprocessing
import time
import sys

def daemonauto():
    while True:
        if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==True:
            deinfectautoruns()
            break
        else:
            time.sleep(5)
    sys.exit(0)
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
        try:
            os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 2 /f')
        except:
            pass
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
    r'C:\roadblock\internals'+os.sep+'sysauto.exe',r'C:\roadblock\internals'+os.sep+'syssys.exe',\
    r'C:\roadblock\internals'+os.sep+'sysproc.exe',r'C:\roadblock\internals'+os.sep+'syshand.exe',r'C:\roadblock\internals\rbchingu.exe',\
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
                #os.system('del /F /Q /A '+i), deactivated, will check later
                pass

    """
    d = multiprocessing.Process(name='daemonauto', target=daemonauto)
    d.daemon = True

    

    d.start()
    time.sleep(1)
    """

    while True:
        if os.path.exists(r'C:\roadblock\internals\infdtc.exe')==True:
            deinfectautoruns()
            break
        else:
            time.sleep(1)
    #raw_input('..')
    time.sleep(10)
    sys.exit(0)
    
