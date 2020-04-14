from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

font_title = Font(name='Fira', size=14, bold=True, color='FFFFFFFF')
font_body = Font(name='Fira', size=12, bold=False, color='404040')
font_import = Font(name='Fira', size=12, bold=True, color='FFFFFFFF')
fill_title = PatternFill(fill_type='solid', fgColor='8064A2')
fill_import = PatternFill(fill_type='solid', fgColor='0070C0')
border = Border(outline=Side(border_style=None, color='FF000000'))
alignment = Alignment(horizontal='left', vertical='center', wrap_text=False, shrink_to_fit=False)

wb = load_workbook('./excel_files/report_fixed.xlsx')

ws_list = wb.sheetnames
ws_list = ws_list[:-2]
for ws_name in ws_list:
    ws = wb[ws_name]
    ws.column_dimensions.group('A', 'B', hidden=True)

    # not worked
    row1 = ws.row_dimensions[1]
    row1.font = font_title

    for row in ws.rows:
        for cell in row:
            cell.font = font_body
            cell.alignment = alignment
            cell.border = border

    # worked
    for cell in ws[1]:
        cell.font = font_title
        cell.alignment = alignment
        cell.fill = fill_title
        cell.border = border

    for name in 'CEFG':
        ws.column_dimensions[name].width = 20.0
    ws.column_dimensions['D'].width = 30.0
    ws.row_dimensions[1].height = 30
    for row_num in range(2, ws.max_row + 1):
        ws.row_dimensions[row_num].height = 25
        cell_confirm = ws['E{}'.format(row_num)]
        cell_confirm.font = font_import
        cell_confirm.fill = fill_import

wb.save('./excel_files/report_formatted.xlsx')
