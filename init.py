import sys
import subprocess

print("Inserisci codice di installazione:")
username=input()

subprocess.call("git clone C:\\Users\\Davide\\Desktop\\unimi\\students\\"+username+"\\bare.git Personali",shell=True)
subprocess.call("git clone C:\\Users\\Davide\\Desktop\\unimi\\public_notebooks Esercitazioni",shell=True)
