import sys
import subprocess

print("Inserisci codice di installazione:")
username=input()

                           
subprocess.call("git clone http://localhost/UnimiAssignments/students/"+username+"/bare.git Personali",shell=True)
