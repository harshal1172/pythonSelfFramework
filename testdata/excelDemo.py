import openpyxl

book = openpyxl.load_workbook("/home/harshal/PycharmProjects/PythonSelfFramework/excelfiles/exceldemo1.xlsx")

sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)

