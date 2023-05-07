from openpyxl import Workbook

wb = Workbook("odds.xlsx")
ws = wb.active


new_row = ["2023-02-02", "Premier League", "ENG", "Arsenal", "Chelsea" , 2.5, 3.5, 4, 2, 2, 2, 2]

ws.append(new_row)

wb.save('odds.xlsx')
