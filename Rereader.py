import re
import tkinter as tk
from tkinter import filedialog

#get file Dialog to save files to a chosen or forced location (export/localsave)

def LineFormatConverter():
    with open("ChessSave.txt", "r") as file:
        n = 0
        Save = file.read()
        rows = Save.splitlines()
        indexer = []
        for a, row in enumerate(rows):
            singleRow = row.replace("|","")
            singleRow = list(singleRow)
            for b, letter in enumerate(singleRow):
                if re.match("[A-Z]", letter) != None:
                    Section = rows[len(rows)-1]
                    Section = Section.replace("[',]","")
                    color = Section[n]
                    indexer.append([a+1, b+1, letter, color])
                    n += 1

def BoxConverter():
    with open("ChessSave.txt", "r") as Lined:
        Lists = Lined.read()
        print(Lists)