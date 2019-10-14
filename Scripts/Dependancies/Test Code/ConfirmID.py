#!/usr/bin/env python3

from ExcelSheet import ExcelSheet


e1 = ExcelSheet()
e1.dataSets("/Users/johnnyperez/Desktop/SQL JOB/File to Link Bloomberg IDs to USPTO IDs.xlsm","/Users/johnnyperez/Desktop/SQL JOB/Confirmed Firm IDs in USPTO Data.xlsx")
e1.setFileName("test")
e1.createSheet("TEST")
e1.createBase()
e1.compare(1)   
e1.save()





