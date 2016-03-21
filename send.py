import json
import glob
import ntpath
import subprocess

def mancanti(name):
    with open(name) as input_file:
        json_data = json.load(input_file)
        
    cont=0
    for cell in json_data["cells"]:
        if cell["source"][0]=="Inserire qui la risposta":
            cont=cont+1
        
    return cont

def copia(name):
    with open(name) as input_file:
        json_data = json.load(input_file)
    with open("Personali/"+ntpath.split(file)[1].split(".")[0]+"_compilato.ipynb", 'w') as output_file:
        json.dump(json_data, output_file)

print("########## Nb Selector")
lista=glob.glob('Esercitazioni/*.ipynb')

for file in lista:
    print(ntpath.split(file)[1]," Risposte mancanti:",mancanti(file))
    if mancanti(file)==0:
        print(ntpath.split(file)[1].split(".")[0]+"_compilato.ipynb"," >>> Personali")
        copia(file)

subprocess.call("cd Esercitazioni && git reset --hard",shell=True)
subprocess.call("cd Personali && git add * && git commit -m davalutare && git push",shell=True)
subprocess.call("cd Personali && git reset --hard && git pull",shell=True)
