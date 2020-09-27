from django.shortcuts import render,redirect

from solverapp.solver import *
# Create your views here.
def displaysudoku(request):
    return  render(request,'sudoku.html')
 
def convertdftoarray(df):
    arr=[]
    for i in df:
        for j in i:
            arr.append(j)
  
    return arr


def solvesudoku(request):
    sudokobord= pd.DataFrame(index=[0,1,2,3,4,5,6,7,8], columns=[0,1,2,3,4,5,6,7,8])
    canplaceonbord= pd.DataFrame(index=[0,1,2,3,4,5,6,7,8], columns=[0,1,2,3,4,5,6,7,8])
    sudokobord=sudokobord.fillna(0)
    caninsert=[]
    arr=convertdftoarray(sudokobord.to_numpy())

    filldefaultvalues(sudokobord,request.POST)

    while chkifzeroindataframe(sudokobord):
        for horizontal in range(0,9):
            for virtical in range(0,9):
                canplaceonbord[horizontal][virtical]=whatCanIInsert(horizontal,virtical,sudokobord,caninsert)#xy
                caninsert=[]
        canplaceonbord=canplaceonbord.values.tolist()

        for horizontal in range(0,9):
            for virtical in range(0,9):
                try:
                    if len(canplaceonbord[horizontal][virtical])==1:
                        sudokobord[virtical][horizontal]=canplaceonbord[horizontal][virtical][0]#xy
                except:
                    pass
        print(canplaceonbord)
        canplaceonbord= pd.DataFrame(index=[0,1,2,3,4,5,6,7,8], columns=[0,1,2,3,4,5,6,7,8])
    print(sudokobord)
    return render(request,'sudoku.html',{'sudo':arr})


