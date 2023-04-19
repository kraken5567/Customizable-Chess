def Loader():
    with open("ChessSave.txt", "r") as file:
        Save = file.read()
        rows = Save.splitlines()
        All = []
        color = str(rows[-1])
        n = 0
    for a, row in enumerate(rows):
        singleRow = row.replace("|","")
        if a == len(rows) - 1:
            break
        for b, char in enumerate(singleRow):
            if n < len(color):
                c = color[n]
                if char.isalpha():
                    if char == char.upper():
                        listAdd=[a,b,char,c]
                        All.append(listAdd)
                        n += 1
    return All


def readSize():
    with open("ChessSave.txt", "r") as file:
        Save = file.read()
        #reads number of returns (GENIUS!)
        rows = Save.count("\n")
        first_line = Save.splitlines()[0]
        columns = len(first_line.split("|")) - 2
        Size = [rows, columns]
    return Size