import subprocess

subprocess.call("cd Esercitazioni && git reset --hard && git pull",shell=True)
subprocess.call("cd Personali",shell=True)
