import subprocess
import glob
import sys


def exists(directory,corso):
    public =glob.glob(directory+'/*/')
    for directory in public:
        if corso==directory.split("\\")[1]:
            return True
    return False

for corso in sys.argv[1:]:
    if exists("Esercitazioni",corso):
        print("Upgrading "+corso)
        subprocess.call("cd Esercitazioni/"+corso+" && git reset --hard && git pull",shell=True)
    else:
        print("Downloading "+corso)
        subprocess.call("cd Esercitazioni && git clone C:/inetpub/wwwroot/UnimiAssignments/public_notebooks/"+corso,shell=True)

subprocess.call("cd Personali && git reset --hard && git pull",shell=True)

input("")
