# Reading an excel file using Python xlrd
# https://www.geeksforgeeks.org/reading-excel-file-using-python/
# http://www.blog.pythonlibrary.org/2014/04/30/reading-excel-spreadsheets-with-python-and-xlrd/

import xlrd

# Give the location of the file
path = "/home/cliffjstx/Excel/PythonTest.xlsx"

# Open workbook
book = xlrd.open_workbook(path)

# print number of sheets
print("Number of sheets:", book.nsheets)

# print sheet names
print("Sheet names:", book.sheet_names())

# get the first worksheet
sheet1 = book.sheet_by_index(0)

# read the row A (row 0)
row = sheet1.row_values(0)
print("Row A", row)

# read the column A - cells A1,A2,A3
cell_A1 = sheet1.cell(0, 0)
cell_A2 = sheet1.cell(1, 0)
cell_A3 = sheet1.cell(2, 0)
print("Cell A1", cell_A1)
print("Cell A2", cell_A2)
print("Cell A3", cell_A3)

# print cell B2
print("Cell B2", sheet1.cell(1, 1))

