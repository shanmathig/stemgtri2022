import pandas as pd
import math 
import re
from MST import MST
def parser():
    df=pd.read_csv('TestText.txt', sep=":", header=None, names = ["Name","Location"]) #import values from the file
    #convert DataFrame pandas gives the df into nested lists
    positions = df['Location'].values.tolist()
    positions2 = []
    for i in range(len(positions)):
        positions[i] = re.sub("[(]","[",positions[i])
        positions[i] = re.sub("[)]","]",positions[i])
        positions2.append(positions[i])
    positionlist = [i.strip("[]").split(",") for i in positions2]
    vertecies=len(positionlist) #saving this for later
    position3 = []
    positionsub = []
    for i in range(len(positionlist)):
        for l in range(len(positionlist[i])):
            positionsub.append(int(positionlist[i][l]))
        position3.append(positionsub)
        positionsub = []
    return MST(position3)