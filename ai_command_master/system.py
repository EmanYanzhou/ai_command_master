import os
import platform
import getpass

class SystemInfo:
    def __init__(self):
        self.system_info = {
            '系统': platform.system(),
            '系统版本': platform.version(),
            '用户名': getpass.getuser(),
            '当前工作目录': os.getcwd(),
            '用户家目录': os.path.expanduser('~'),
        }
    
    def get_system_info(self) -> dict:
        return self.system_info
    
    def update_working_dir(self):
        self.system_info['working_dir'] = os.getcwd()