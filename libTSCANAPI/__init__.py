import os
import shutil
import sys
from .TSCommon import _os,_curr_path
from .TSCommon import *
from .TSMasterDevice import *
from .TSDB import *
from .TSUDS import*
from .config import *
from .TSPrase_Fibex import *
import atexit
try :
    
    def updateFile(file,old_str,new_str):
        file_data = ""
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if old_str in line and (not Python_CAN_Config in line):
                    line = line.replace(old_str,new_str)
                file_data += line
        with open(file,"w",encoding="utf-8") as f:
            f.write(file_data)
    
    if IS_ADD_PYTHON_CAN:
        import can
        libtosun_path = os.path.join(_curr_path, 'libtosun.py')
        if os.path.isfile(libtosun_path) :
            can_path = os.path.dirname(can.__file__) #for pyinstaller to find the compiled module
            old_str = '"socketcand": ("can.interfaces.socketcand", "SocketCanDaemonBus"),'
            new_str = old_str + '\n"libtosun":("can.interfaces.libtosun","libtosunBus"),'
            updateFile(os.path.join(can_path, 'interfaces/__init__.py'),old_str,new_str)
            shutil.move(libtosun_path,os.path.join(can_path, 'interfaces'))
    
    current_dbc_path = os.path.join(_curr_path, 'dbc.py')
    if os.path.isfile(current_dbc_path):
        import cantools
        cantools_path = os.path.dirname(cantools.__file__)
        dbc_path = os.path.join(cantools_path, 'database/can/formats')
        shutil.move(libtosun_path,dbc_path)
except:
    pass
initialize_lib_tscan(True,True,False)

def close():
    tsapp_disconnect_all()
    finalize_lib_tscan()
    if os.path.exists('./libTSH.so'):
        os.remove("./libTSH.so")
    elif os.path.exists('./libTSH.dll'):
        os.remove("./libTSH.dll")

atexit.register(close)