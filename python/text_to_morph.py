from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth

categories = {}
text_size = 12
main_font = 'Courier'

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
        current_width = stringWidth(names, main_font, text_size)
        if current_width > max_title_width:
            max_title_width = current_width
    return max_title_width

text_to_dict()
# print(categories)
c = canvas.Canvas("output.pdf", bottomup=0, pagesize=landscape(A4))
height, width = A4

cell_height = height / len(categories)
title_cell_width = calculate_max_title_width() + 5
index_y = 0
for category in categories:
    cell_width = (width - title_cell_width) / len(categories[category])
    c.rect(0, index_y*cell_height, title_cell_width, cell_height)
    c.drawString(5, (index_y*cell_height)+cell_height/2, category)
    list_of_values = categories[category]
    for i in range(len(list_of_values)):
        c.rect(title_cell_width+i*cell_width, index_y*cell_height, cell_width, cell_height)
        label = list_of_values[i]
        text_width = stringWidth(label, main_font, text_size)
        c.drawString(title_cell_width+i*cell_width+cell_width/2.0 - text_width/2.0, index_y*cell_height+cell_height/2.0+5, label)
    index_y = index_y + 1

c.save()

