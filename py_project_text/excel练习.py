from openpyxl import Workbook, load_workbook

wb = Workbook()      # 创建一个excel文件
sheet = wb.active    # 获取积极的Excel文件的sheet
print(sheet.title)

sheet.title = "hello word"
print(sheet.title)

sheet["B9"] = "hello"
sheet["C9"] = "word"

sheet.append(["陈文宇", "20", "10200115"])
print(sheet["B5:B10"])
sheet["b5:B8"] = [1]

print(sheet["B5:B10"])




