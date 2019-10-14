import xlrd
import numpy as np
from openpyxl import Workbook, load_workbook
from tqdm import tqdm
import time

class ExcelSheet: 
    book = Workbook()
    arrSheet=[]
    s1 = []
    s2 = []
    
    
    def __init__(self):

        fileName = None
        currentRow =0
        currentColumn = 0
    
    def dataSets(file1,file2):
        loc1 = (file1)
        loc2 = (file2)

        fileToLink = xlrd.open_workbook(loc1) 
        confirmID = xlrd.open_workbook(loc2)

        sheet1 = fileToLink.sheet_by_index(0)
        sheet2 = confirmID.sheet_by_index(0) 
 
        j=1
        i=1
        
        for i in range(sheet2.nrows):
            self.s2.append([str((sheet2.cell(i,1).value).lower()),str((sheet2.cell(i,0).value))])
            
        print(self.s2[1][1])

        for j in range(sheet1.nrows):
            self.s1.append(str((sheet1.cell(j,1).value).lower()))
        self.s1.sort
        
        
    def setFileName(self,fileName):
        if ".xlsx" not in fileName:
            self.fileName = str(fileName)+".xlsx"
            
        self.fileName = str(self.fileName)
        print(self.fileName)
    
    def createSheet(self,name):
        sheet = self.book.active
        
        self.arrSheet.append(sheet)

    def save(self):
        self.book.save(self.fileName)


    def createBase(self,r=None,sheet_num=None):
        index = 0
        data = self.s1
        
        
        
        if r == None:
            r = len(data)-1

        if sheet_num != None:
            index = sheet_num

        sheet = self.arrSheet[index]
        sheet.title = "Test"


        
        for i in range(1,r):
            cellref = sheet.cell(row=i,column=2)
            cellref.value = data[i].upper()
    
        # Print iterations progress
         

    def compare(self,s):
        percent = 0
        sheet = self.arrSheet[0]
        l = len(self.s2)-1
        for i in tqdm(range(s,l)):
            temp = self.s2[i][0]
            for j in range(1,len(self.s1)):
                temp2 = self.s1[j]
                if temp[0] != temp2[0]:
                    continue
                else:
                    ratio = self.levenshtein(temp,temp2)
                    if ratio <= 2:
                        percent += 1
                        cellref = sheet.cell(row=j,column=1)
                        cellref.value= self.s2[i][1]
        print(str((percent/l)*100))
             
    def levenshtein(self,str1,str2):
        size_x = len(str1) + 1
        size_y = len(str2) + 1
        matrix = np.zeros((size_x,size_y))
        for x in range(size_x):
            matrix [x,0] = x
        for y in range(size_y):
            matrix [0,y] = y
        
        for x in range(1,size_x):
            for y in range(1,size_y):
                if str1[x-1] == str2[y-1]:
                    matrix[x,y] = min(
                        matrix[x-1,y]+1,
                        matrix[x-1,y-1],
                        matrix[x,y-1]+1
                    )

                else:
                    matrix [x,y]=min(
                        matrix[x-1,y]+1,
                        matrix[x-1,y-1]+1,
                        matrix[x,y-1]+1
                    )
        return(matrix[size_x - 1, size_y - 1])

    