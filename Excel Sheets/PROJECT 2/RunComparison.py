import sys
from ExcelSheet import ExcelSheet

ag1 = sys.argv[1]
ag2 = sys.argv[2]

excel = ExcelSheet()
excel.dataSets(ag1,ag2)
excel.chooseData()







