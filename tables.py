import random
from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)  # Set position 1.5 cm from the bottom
        self.set_font('Helvetica', 'I', 8)  # Choose Arial italic 8
        page_number_text = 'Page ' + str(self.page_no())
        self.set_x((210 - self.get_string_width(page_number_text)) / 2)  # Center the page number text
        self.cell(0, 10, page_number_text)  # Page number
        

def addition():
    a = random.randint(0, 10)
    b = random.randint(0, 10 - a)
    op = '+'
    return f'{a} {op} {b} = _____'

def subtraction():
    a = random.randint(1, 10)
    b = random.randint(0, a)
    
    op = '-'
    return f'{a} {op} {b} = _____'

def multiplication():
    a, b = random.randint(1, 8), random.randint(1, 8)
    op = 'x'
    return f'{a} {op} {b} = _____'

def generate_question():
    types = [addition, subtraction, multiplication]

    choice = types[random.randint(0, len(types)-1)]
    
    return choice()

       
def generate_questions(num_questions=500):
    questions = []

    for i in range(num_questions):
        questions.append(generate_question())
        
    return questions

def create_pdf(questions):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)
    column = 0
    for question in questions:
        pdf.set_xy(10 + column * 90, pdf.get_y())
        pdf.cell(0, 10, question)
        if column == 1:
            pdf.ln(10)
        column = 1 - column  # toggle between 0 and 1
    pdf.output('test.pdf')

questions = generate_questions()
create_pdf(questions)

