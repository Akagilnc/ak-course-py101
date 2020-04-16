from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font

font_body = Font(name='黑体', size=12, bold=False, color='404040')
# 先调整一个cell对比一下

alignment = Alignment(horizontal='left', vertical='bottom', wrap_text=False, shrink_to_fit=False)
alignment_right = Alignment(horizontal='right', vertical='bottom', wrap_text=False, shrink_to_fit=False)
bd1 = Side(border_style='mediumDashDot', color='000000')
bd2 = Side(border_style='thin', color='000000')
border = Border(left=bd1, right=bd1, top=bd1, bottom=bd1, start=bd2, end=bd2)

# 定义标题相关的style
font_title = Font(name='黑体', size=18, bold=True, color='FFFFFF')
alignment_title = Alignment(horizontal='center', vertical='center', wrap_text=False, shrink_to_fit=False)
fill_title = PatternFill(fill_type='solid', fgColor='0F4C81')

# 设置确诊人数的font fill
font_imp = Font(name='fira', size=16, bold=True, color='000000')
fill_imp = PatternFill(fill_type='solid', fgColor='F3D5AD')

# 读取现有文件
wb = load_workbook('./excel_files/report_fixed.xlsx')
for sheet in wb.worksheets[:-2]:
    # sheet = wb[name] # 根据名字取出sheet
    sheet.sheet_view.zoomScale = 200
    # 设置字体到所有的cell
    for row in sheet.rows:
        for index, cell in enumerate(row):
            cell.font = font_body
            cell.alignment = alignment if index == 0 else alignment_right
            cell.border = border

    # 设置第一行的title font alignment, fill
    for title_cell in sheet[1]:
        title_cell.font = font_title
        title_cell.alignment = alignment_title
        title_cell.fill = fill_title

    # 设置列宽和行高
    sheet.column_dimensions['C'].width = 25.0
    for column_name in 'ABDE':
        sheet.column_dimensions[column_name].width = 15
    sheet.row_dimensions[1].height = 30

    # 设置确诊人数style
    # 从第二行开始，拿到所有的行号
    for row_num in range(2, sheet.max_row + 1):
        # 设置正文的行高
        sheet.row_dimensions[row_num].height = 20
        # 设置确诊人数font fill
        cell_confirmed = sheet['C{}'.format(row_num)]
        cell_confirmed.font = font_imp
        cell_confirmed.fill = fill_imp
        cell_confirmed.number_format = '#,##0'

# 保存到一个新的excel
wb.save('./excel_files/report_formatted.xlsx')
