import openpyxl

wb = openpyxl.load_workbook(
    r"C:\Users\Dell\Downloads\student_data.xlsx"
)

print("Available sheets:", wb.sheetnames)

for sheet in wb.worksheets:

    print("\nSheet name:", sheet.title)
    print("Max rows:", sheet.max_row)
    print("Max columns:", sheet.max_column)

    for row in sheet.iter_rows(values_only=True):
        print(row)