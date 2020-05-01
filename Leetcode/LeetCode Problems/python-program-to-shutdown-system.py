import os
import platform
if platform.system() == "Windows":
    os.system("shutdown -s -t 0")
else:
    os.system("shutdown -h now")