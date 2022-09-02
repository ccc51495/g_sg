import xlrd

wb = xlrd.open_workbook("soldier.xlsx")

sheet1 = wb.sheet_by_index(0)

col1 = sheet1.col_values(0)
line1 = sheet1.row_values(2)
if "农夫" in col1:
    print(col1.index("农夫"))
    print(col1[3])
    print(line1)