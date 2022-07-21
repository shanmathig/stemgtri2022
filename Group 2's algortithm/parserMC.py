import pandas as pd
import re
def parserMC():
    df=pd.read_csv('InputTextMC.txt', sep=":", header=None, names = ["Name","Location"]) #import values from the file
    #convert DataFrame pandas gives the df into nested lists
    List_Nums = df['Name'].values.tolist()
    String_Positions = df['Location'].values.tolist()
    List_Positions = []
    for i in range(len(String_Positions)):
        String_Positions[i] = re.sub("[(]","[",String_Positions[i])
        String_Positions[i] = re.sub("[)]","]",String_Positions[i])
        List_Positions.append(String_Positions[i])
    Stripped_Positions = [i.strip("[]").split(",") for i in List_Positions]
    Final_List_Positions = []
    Temp_Positions = []
    for i in range(len(Stripped_Positions)):
        for l in range(len(Stripped_Positions[i])):
            Temp_Positions.append(int(Stripped_Positions[i][l]))
        Final_List_Positions.append(Temp_Positions)
        Temp_Positions = []
    Loop_Positions = []
    #for i in range(len(Final_List_Positions)):
    #    Final_List_Positions[i].append(i)
    return Final_List_Positions