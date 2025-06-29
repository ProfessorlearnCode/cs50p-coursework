from fpdf import FPDF

pdf = FPDF()

class PDF():
    def __init__(self, name):
        self.shirt_pdf = FPDF()
        self.shirt_pdf.add_page()
        self.shirt_pdf.set_font('Times', 'B', 50)
        self.shirt_pdf.cell(0, 60,"CS50 Shirtificate", new_x ="LMARGIN", new_y ="NEXT", align ="C")
        self.shirt_pdf.image("shirtificate.png", w=self.shirt_pdf.epw)
        self.shirt_pdf.set_font_size(30)
        self.shirt_pdf.set_text_color(255, 255, 255)
        self.shirt_pdf.text(x = 58.5, y= 140, txt= f"{name} took CS50")

    def saving(self, name):
        self.shirt_pdf.output(name)



user_name = input("Name: ")
pdf = PDF(user_name)
pdf.saving("shirtificate.pdf")
