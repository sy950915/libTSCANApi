'''
Author: seven 865762826@qq.com
Date: 2023-04-21 11:21:33
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-06-10 07:22:33
'''
from ctypes import cdll


import os
import platform
import sys
import shutil

_curr_path = os.path.dirname(__file__)
_arch, _os = platform.architecture()
_os = platform.system()
_is_windows, _is_linux = False, False
if 'windows' in _os.lower():
    from ctypes import WinDLL,windll
    _is_windows = True
    if _arch == '32bit':
        if sys.version_info < (3,9):
            shutil.copy(os.path.join(_curr_path, 'windows/x86/libTSH.dll'),'./')
        _lib_path = os.path.join(_curr_path, 'windows/x86/libTSCAN.dll')
    else:
        if sys.version_info < (3,9):
            shutil.copy(os.path.join(_curr_path, 'windows/x64/libTSH.dll'),'./')
        _lib_path = os.path.join(_curr_path, 'windows/x64/libTSCAN.dll')
    # if not os.path.exists(_lib_path):
    #     _lib_path = r"D:\demo\libtosun\libtosun\windows\X64\libTSCAN.dll"
    dll = windll.LoadLibrary(_lib_path)
elif 'linux' in _os.lower():
    _is_linux = True
    if _arch == '64bit':
        shutil.copy(os.path.join(_curr_path, 'linux/libTSH.so'),'./')
        _lib_path = os.path.join(_curr_path, 'linux/libTSCANApiOnLinux.so')
    else:
        _lib_path = None
    if _lib_path:
        dll = cdll.LoadLibrary(_lib_path)
else:
    _library = None
