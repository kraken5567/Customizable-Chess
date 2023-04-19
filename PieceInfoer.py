import os 
import json

def pieceInQuestion(All,x):
    LegalSqrs = []
    P = All[x]
    library = "Pieces/"+P[3]+P[2]
    extJson = '.json'
    
    Name = str(P[3])+str(P[2])
    for files in os.listdir(library):
        if files.endswith(extJson):
            with open("Pieces/"+str(Name)+"/"+str(files),"r") as properites:
                info = json.load(properites)
                print(info)
                LegalSqrs = [info["Dist"], info["Movement"]]
        return LegalSqrs
