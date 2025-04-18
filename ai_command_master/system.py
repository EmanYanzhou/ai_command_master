import os
import platform
import getpass

class SystemInfo:
    def __init__(self):
        self.system_info: dict = {
            '系统': platform.system(),
            '系统版本': platform.version(),
            '用户名': getpass.getuser(),
            '用户家目录': os.path.expanduser('~'),
            '当前工作目录': os.getcwd()
        }
    
    def get_system_info(self) -> dict:
        return self.system_info
