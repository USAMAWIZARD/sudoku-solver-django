
import numpy as np
import pandas as pd

def chkifzeroindataframe(sudokobord):
    for i in range(8):
        if 0 in sudokobord[i][:].values.tolist():
            return True
    return False
def getslicerepetations(x,y,i,sudokobord):
    list=getslice(x,y,sudokobord)
    #print(list)
    list=list.values.tolist()
    for  innerlist in list:
        if i in innerlist:
            return True
    return False
def getslice(x,y,sudokobord):
    if x>=0 and  x<=2 and y>=0 and  y<=2:
        return sudokobord.loc[[0,1,2],[0,1,2]]
    if x>=3 and x<=5 and y>=0 and  y<=2:
        return sudokobord.loc[[3, 4, 5], [0, 1, 2]]
    if x>=6 and x<=8 and y>=0 and  y<=2:
        return sudokobord.loc[[6, 7, 8], [0, 1, 2]]
    if x>=0 and x<=2 and y>=3 and  y<=5:
        return sudokobord.loc[[0, 1, 2], [3, 4, 5]]  #xy
    if x>=3 and x<=5 and y>=3 and  y<=5:
        return sudokobord.loc[[3, 4, 5], [3, 4, 5]]  #xy
    if x>=6 and x<=8 and y>=3 and  y<=5:
        return sudokobord.loc[[6, 7, 8], [3, 4, 5]]  #xy
    if x>=0 and x<=2 and y>=6 and  y<=8:
        return sudokobord.loc[[0, 1, 2], [6, 8, 7]]  #xy
    if x>=3 and x<=5 and y>=6 and  y<=8:
        return sudokobord.loc[[3, 4, 5], [6, 8, 7]]  #xy
    if x>=6 and x<=8 and y>=6 and  y<=8:
        return sudokobord.loc[[6, 7, 8], [6, 8, 7]]  #xy
def filldefaultvalues(sudokobord,values):
    for i in range(9):
        for j  in range(9):
            if values[str(i+1)+str(j+1)] !="":
                sudokobord[j][i]=values[str(i+1)+str(j+1)]
    print(sudokobord)
def whatCanIInsert(x,y,sudokobord,caninsert):
    if sudokobord[x][y]:
        return False
    for i in range(1,10):
        if ((not(i in sudokobord.loc[y][:].values.tolist())) and (not(i in sudokobord.loc[:][x].values.tolist()) and (not(getslicerepetations(y,x,i,sudokobord))))):
            caninsert.append(i)
    return caninsert



