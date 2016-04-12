import sys
import subprocess

print("Inserisci codice di installazione:")
username=input()

                           
subprocess.call("git clone C:/inetpub/wwwroot/UnimiAssignments/students/"+username+"/bare.git Personali",shell=True)
