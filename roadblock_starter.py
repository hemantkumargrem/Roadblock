# I do monitoring.. that's my job.. don't disturb me..
# todo: add autorun taking functionality every 10 days
import os
import sys
import hashlib
import win32event, win32api, winerror
import string 
import random

import time

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
        r'C:\roadblock\internals'+os.sep+'roadblockreal2.exe',r'C:\roadblock\internals'+os.sep+'rbchingu.exe',\
        r'C:\roadblock\internals'+os.sep+'roadblock_procdelete.exe',r'C:\roadblock\internals'+os.sep+'procserv.exe',r'C:\roadblock\internals'+os.sep+'roadblock_procstop.exe',\
        r'C:\roadblock\internals'+os.sep+'roadblock_procprocess.exe',r'C:\roadblock\internals'+os.sep+'roadblock_autoprocess.exe',\
        r'C:\roadblock\internals'+os.sep+'firstnet.exe',r'C:\roadblock\internals'+os.sep+'conne.exe',\
        r'C:\roadblock\internals'+os.sep+'firstnetdone.exe',r'C:\roadblock\internals'+os.sep+'Roadblock_desktop.exe',\
        r'C:\roadblock\internals'+os.sep+'Roadblock_conn.exe',r'C:\roadblock\internals'+os.sep+'roadblock_starter.exe',\
        r'C:\roadblock\internals\syspsex.exe',r'C:\roadblock\internals\aq.exe',\
        r'C:\roadblock\internals\image.exe',r'C:\roadblock\internals\syssig.exe',r'C:\roadblock\internals'+os.sep+'image1.exe']
        
        for i in a:
            print i
            time.sleep(1)
            if os.path.isdir(i)==False:
                deletei=0
                for ku in listofresource:
                    try:
                        i.index(ku)
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
                        time.sleep(1)
                        pass
                    time.sleep(1)
                    pass

        dsdd=open(r"C:\roadblock\internals"+os.sep+'donedeletion.exe',"w")
        dsdd.close()
    except Exception as ex:
        print ex
        print 'outside deletion exception'
        pass



    pass


def heydeleting(locc):

    a=glob(locc+r"\*")
    
    for i in a:
        print i
        #time.sleep(0.5)
        if os.path.isdir(i)==False:
            try:
                i.index('1aaa')
                #os.system("del /F /Q /A '"+locc+os.sep+i+"'")
                os.remove(i)
            except:
                pass
            try:
                i.index('eee')
                #os.system("del /F /Q /A '"+locc+os.sep+i+"'")
                os.remove(i)
            except:
                pass
            try:
                i.index('zzz')
                #os.system("del /F /Q /A '"+locc+os.sep+i+"'")
                os.remove(i)
            except:
                pass
            try:
                i.index('99hh')
                #os.system("del /F /Q /A '"+locc+os.sep+i+"'")
                os.remove(i)
            except:
                pass

def deletefiled(username):

    #--- List of users Locations ---#
    try:
        #gettheusername=os.environ.get("USERNAME")
        location1=username+os.sep+'Desktop'
        location2=username+os.sep+'Documents'
        location3=username
        location4=username+os.sep+'Downloads'
        location5='C:'
    except Exception as ex:
        print ex
        sys.exit(0)

    
    heydeleting(location1)
    heydeleting(location2)
    heydeleting(location3)
    heydeleting(location4)
    heydeleting(location5)

    
    #############################################################


    pass

def deletemonitoredfiles():

    from glob import glob
    a=glob(r"C:\Users\*")
    for i in a:
        if os.path.isdir(i)==True:
            try:
                print i
                #raw_input('---')
                if i!=r'C:\Users\All Users' and i!=r'C:\Users\Default' and i!=r'C:\Users\Default User' and i!=r'C:\Users\Public':
                    deletefiled(i)
                    print i
                    #raw_input('going again..')
                    pass
            except:
                pass





def executeall():
    

    try:
        
        #os.system(commd)
        #subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\roadblock_desktop.exe', shell=True)
        #subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\roadblockreal2.exe', shell=True)
        pass
        
    except Exception as ex:
        print ex

    
    time.sleep(5)
    
    try:
        
        subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\Roadblock_conn.exe', shell=True)
    except Exception as ex:
        print ex
    time.sleep(5)
    


    try:
        
        #subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\procserv.exe', shell=True)
        pass
    except Exception as ex:
        print ex
    time.sleep(5)
    


    try:
        
        subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\roadblock_procdelete.exe', shell=True)
    except Exception as ex:
        print ex
    time.sleep(5)
    



    try:
        
        subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\roadblock_procstop.exe', shell=True)
    except Exception as ex:
        print ex
    time.sleep(5)
    

    try:
        
        subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\roadblock_procprocess.exe', shell=True)
    except Exception as ex:
        print ex
    time.sleep(5)
    


    try:
        
        subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\roadblock_autoprocess.exe', shell=True)
    except Exception as ex:
        print ex
    time.sleep(5)
    
    pass

    try:
        
        subprocess.Popen(r'C:\roadblock\internals\syspsex.exe -i -d -s -accepteula  C:\roadblock\internals\roadblockreal2.exe', shell=True)
        pass
    except Exception as ex:
        print ex
    time.sleep(5)
    
    pass



import psutil
import time


if __name__ == '__main__':
    
    while True:
        

        """
        try:
            print 'deleting infdtc'
            os.system('del /F /Q /A '+r'C:\roadblock\internals'+os.sep+'infdtc.exe')
        except Exception as ex:
            print ex
            pass
        """

        #######################################################################################



        """
        process_name = ['roadblockreal.exe',\
        'roadblock_sysauto.exe',\
        'sysauto.exe',\
        'sysproc.exe','syshand.exe',\
        'roadblockreal2.exe',\
        'roadblock_procdelete.exe','procserv.exe',\
        'roadblock_procstop.exe',\
        'roadblock_autoprocess.exe',\
        'Roadblock_conn.exe']
        """ 
        process_name = ['roadblockreal2.exe']


        gotransomrr2=0
        def findifprocessrunning():
            global gotransomrr2
            gotransomrr2=0
            for proc in psutil.process_iter(): 
                process = psutil.Process(proc.pid)# Get the process info using PID
                pname = process.name()# Here is the process name
                #print pname
                #print pname,proc.pid
                #time.sleep(1)
                for juy in process_name:
                    if pname == juy: 
                        print pname,'found'
                        gotransomrr2=1
                    else:
                        #print ("Dont have")
                        pass
                

        while True:
            print 'checking if old process exits'
            findifprocessrunning()
            print gotransomrr2,'gotransomrr2'
            if gotransomrr2==1:
                time.sleep(5)
                continue
            else:
                break
                pass

        time.sleep(20)
        #############################################################################################

        #PROCNAMEb = "roadblock_procprocess.exe" # no need, sometime it just hang

        PROCNAMEb = ['roadblockreal.exe',\
        'roadblock_sysauto.exe',\
        'sysauto.exe',\
        'sysproc.exe','syshand.exe',\
        'roadblockreal2.exe',\
        'roadblock_procdelete.exe','procserv.exe',\
        'roadblock_procstop.exe',\
        'roadblock_autoprocess.exe',\
        'Roadblock_conn.exe']

        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() in PROCNAMEb:
                proc.kill()
        
        #service = multiprocessing.Process(name='my_service', target=my_service)
        #worker_1 = multiprocessing.Process(name='worker 1', target=worker)
        #worker_2 = multiprocessing.Process(target=worker) # use default name
        while True:
            print 'deleting old files'
            try:
                deletealloldfiles()

                if os.path.exists(r"C:\roadblock\internals"+os.sep+'donedeletion.exe')==True:
                    print 'deletion done..'
                    time.sleep(1)
                    break
                else:
                    pass
            except:
                pass

        print 'starting all programs..'
        try:
        	deletemonitoredfiles() # including encrypted ones...
        except Exception as ex:
        	print ex

        

        executeall()

        time.sleep(4)





