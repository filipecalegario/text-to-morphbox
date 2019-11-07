from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import mm

categories = {}
font_size = 10
main_font = 'Helvetica'
main_font_bold = main_font + '-Bold'

def text_to_dict():
    f = open('input.txt')
    for line in f:
        line = line.rstrip().split(':')
        category = line[0].strip()
        values = line[1].split(',')
        values = list(filter(None, values))
        values = [x.strip() for x in values]
        categories[category] = values

def calculate_max_title_width():
    max_title_width = 0;
    for names in categories:
        current_width = stringWidth(names, main_font_bold, font_size)
        if current_width > max_title_width:
            max_title_width = current_width
    return max_title_width

text_to_dict()
# print(categories)
c = canvas.Canvas("output.pdf", bottomup=0, pagesize=landscape(A4))
c.setFont(main_font, font_size)
# c.setDash(1,2)
height, width = A4
margin_horizontal = 10*mm
margin_vertical = 10*mm
width = width - margin_horizontal*2
height = height - margin_vertical*2

cell_height = height / len(categories)
title_cell_width = calculate_max_title_width() + 10
index_y = 0
for category in categories:
    cell_width = (width - title_cell_width) / len(categories[category])
    c.rect(margin_horizontal, margin_vertical + index_y*cell_height, title_cell_width, cell_height)
    c.setFont(main_font_bold, font_size)
    c.drawString(margin_horizontal + 5, margin_vertical + (index_y*cell_height)+cell_height/2+5, category)
    c.setFont(main_font, font_size)
    list_of_values = categories[category]
    for i in range(len(list_of_values)):
        c.rect(margin_horizontal + title_cell_width+i*cell_width, margin_vertical + index_y*cell_height, cell_width, cell_height)
        label = list_of_values[i]
        text_width = stringWidth(label, main_font, font_size)
        c.drawString(margin_horizontal + title_cell_width+i*cell_width+cell_width/2.0 - text_width/2.0, margin_vertical + index_y*cell_height+cell_height/2.0+5, label)
        # c.drawCentredString(title_cell_width+i*cell_width+cell_width/2.0, index_y*cell_height+cell_height/2.0, label)
    index_y = index_y + 1

c.save()

