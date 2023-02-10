#!/usr/bin/python
#coding: utf-8

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def create_pdf(filename):
	doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
	elements = []

	name = Paragraph("your_name")
	elements.append(name)
	elements.append(Spacer(1, 20))

	data = [["About me", "lore ipsum"],
	       ["Contact", "(41)9 8525-1434"],
	       ["References", "lore ipsum"],
	       ["Hobbies", "lore ipsum"],
	       ["Education", "lore ipsum"],
	       ["Experiences", "lore ipsum"],
	       ["Certifications", "lore ipsum"],
	       ["Skills", "lore ipsum"]]
	table = Table(data)
	table.setStyle(TableStyle([('BACKGROUND',(0, 0), (-1, 0), colors.olive),
		                        ('TEXTCOLOR', (0,0), (-1, 0), colors.whitesmoke),
		                        ('ALIGN', (0,0), (-1, 0), 'LEFT'),
		                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
		                        ('BOTTOMPADDING', (0,0), (-1, 0), 12),
		                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
		                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
		                        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica')]))
	elements.append(table)

	doc.build(elements)

create_pdf("Curriculum.pdf")
