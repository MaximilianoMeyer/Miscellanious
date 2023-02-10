#!/usr/bin/python
#coding: utf-8

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style="B", size=15)
        self.cell(190, 10, "Currículo", align="C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", style="I", size=8)
        self.cell(0, 10, "Página %s" % self.page_no(), align="C")

def get_info():
    info = {}
    info["name"] = input("Digite seu nome: ")
    info["email"] = input("Digite seu email: ")
    info["phone"] = input("Digite seu telefone: ")
    info["education"] = input("Digite sua formação: ")
    info["experience"] = input("Digite sua experiência: ")
    return info

def create_pdf(info):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(190, 10, "Nome: %s" % info["name"], ln=1)
    pdf.cell(190, 10, "Email: %s" % info["email"], ln=1)
    pdf.cell(190, 10, "Telefone: %s" % info["phone"], ln=1)
    pdf.ln(10)
    pdf.cell(190, 10, "Formação:", ln=1)
    pdf.cell(190, 10, info["education"], ln=1)
    pdf.ln(10)
    pdf.cell(190, 10, "Experiência:", ln=1)
    pdf.cell(190, 10, info["experience"], ln=1)
    pdf.output("curriculo1.pdf", "F")

if __name__ == "__main__":
    info = get_info()
    create_pdf(info)
