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
def pr2csv_prcheck(filetimeandname):
    #Tue Nov 21 12:04:19 2017$#$test-1.PML
    filetimeandname=filetimeandname.split('$#$')
    filetimeandname=filetimeandname[1]
    filetimeandname=filetimeandname.split('.')
    filetimeandname=filetimeandname[0]
    # now convert pml to csv
    os.chdir(r'C:\roadblock\internals')
    os.system(r'C:\roadblock\internals'+os.sep+r'sysproc.exe /AcceptEula /Quiet /Minimized /OpenLog '+filetimeandname+'.pml /SaveAs '+r'C:\roadblock\internals'+os.sep+filetimeandname+'.csv')
    return filetimeandname



def prcheck():
    fxss=open(r'C:\roadblock\internals'+os.sep+'listofcsv.exe','w')
    try:
        # checking no of pml files sorted by date and time
        filelist=[]
        # path to the directory (relative or absolute)
        gotpmlinsystem32=0

        dirpath = r'C:\windows\system32'

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
        time.sleep(5)

        for i in reversed(filelist):
            #print i
            try:
                i.index('.PML')
                gotpmlinsystem32=1
                print i
                filenamee=pr2csv_prcheck(i)
                #raw_input('converted to csv')
                print filenamee # converted to csv at this stage
                # time to search for the malware
                fxss.write(i+'\n')
                #gff=open(r'C:\roadblock\internals'+os.sep+'pmlinsystem.exe','w') # as saved csv file is in internal s folder, so removing this check
                gff=open(r'C:\roadblock\internals'+os.sep+'pmlininternals.exe','w')
                gff.close()
                #prprocesscsv(filenamee) # this gives me all writefile,deleted and process create activity and saved to proc.txt
                #raw_input('got all req event from sysproc')


            except Exception as ex:
                #print ex
                pass

        if gotpmlinsystem32==0:
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

            for i in reversed(filelist):
                #print i
                try:
                    i.index('.PML')
                    print i
                    filenamee=pr2csv_prcheck(i)
                    #raw_input('converted to csv')
                    print filenamee # converted to csv at this stage
                    # time to search for the malware
                    fxss.write(i+'\n')
                    gff=open(r'C:\roadblock\internals'+os.sep+'pmlininternals.exe','w')
                    gff.close()
                    #prprocesscsv(filenamee) # this gives me all writefile,deleted and process create activity and saved to proc.txt
                    #raw_input('got all req event from sysproc')


                except Exception as ex:
                    #print ex
                    pass
    except:
        pass
    fxss.close()
    gff=open(r'C:\roadblock\internals'+os.sep+'processprocdone.exe','w')
    gff.close()

#prcheck()

import os

#os.system(r'C:\roadblock\internals\sysproc.exe /AcceptEula /Quiet /Minimized /BackingFile testhhhaaaiii')
from multiprocessing import Process, freeze_support

import multiprocessing
import time
import sys

def daemonproc():
    while True:
        # check if sysproc is terminated by roadblock_procstop
        if os.path.exists(r'C:\roadblock\internals\sysroadblock_procstopped.exe')==True:
            prcheck()
            break
        else:
            time.sleep(5)

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
    r'C:\roadblock\internals'+os.sep+'sysauto.exe',r'C:\roadblock\internals'+os.sep+'syssys.exe',\
    r'C:\roadblock\internals'+os.sep+'sysproc.exe',r'C:\roadblock\internals'+os.sep+'syshand.exe',\
    r'C:\roadblock\internals'+os.sep+'roadblockreal2.exe',r'C:\roadblock\internals\rbchingu.exe',\
    r'C:\roadblock\internals'+os.sep+'roadblock_procdelete.exe',r'C:\roadblock\internals'+os.sep+'procserv.exe',r'C:\roadblock\internals'+os.sep+'roadblock_procstop.exe',\
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
                #os.system('del /F /Q /A '+i), deactivated will check later
                pass
    """
    d = multiprocessing.Process(name='daemonproc', target=daemonproc)
    d.daemon = True

    

    d.start()
    time.sleep(1)
    """
    while True:
        # check if sysproc is terminated by roadblock_procstop
        if os.path.exists(r'C:\roadblock\internals\sysroadblock_procstopped.exe')==True:
            time.sleep(10)
            prcheck()
            break
        else:
            time.sleep(5)
    