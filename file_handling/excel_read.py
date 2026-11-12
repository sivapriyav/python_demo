#openpyxl is a python library used to work with excel spreadsheets
#1.create new excel files,
#2.Read existing excel files,
#3.Write data into cells,
#4. Delete rows and coloumns,
#5. Work with multiple sheets


#How to install: python -m pip install openpyxl
import openpyxl

#Reading an existing excel file

workbook = openpyxl.load_workbook("C:\\Users\\Dell\\Downloads\\student_data.xlsx")
sheet = workbook["data"]
print(sheet["A2"].value)
print(sheet["D2"].value)

#Reading all rows from an excel file

for row in sheet.iter_rows(values_only=True):
    print(row)
print(sheet.max_row)
print(sheet.max_column)




