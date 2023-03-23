import json
from time import sleep
import onoff


def ProcessData(data):
    #Code pour alummer led ou ske tu veux selon data 
    # pour linstant il n'ya que Led1 et Led2 dans data
    # tu modifies api pour ajouter ou supprimer
    # et tu fais ske tu veux en les utilisant ici
    print(data)
    if data["Led"]==1:
        #allumer led
        Led.on()
        pass
    else:
        #éteindre led
        Led.off()
        pass

#initialize Gpio pins for Led
Led= onoff.Gpio(21,"out")

#read initial data from json file
with open("data.json",'r') as f: #si data.json est situé autre part écris le chemin complet
    old_data = json.loads(f.read())

#fs ske tu veux avec old_data
while True:
    try:
        #read new data from json file
        with open("data.json",'r') as f: #si data.json est situé autre part écris le chemin complet
            data = json.loads(f.read())

        #if data changed, process it
        if data != old_data:
            ProcessData(data)
            old_data = data
        #wait a bit before checking new data
        sleep(0.1)
    except:
        pass
Led.close()