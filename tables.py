import random
from fpdf import FPDF

def generate_questions(num_questions=50):
    questions = []
    operations = ['+', '-', 'x']
    for i in range(num_questions):
        a, b = random.randint(1, 12), random.randint(1, 12)
        op = random.choice(operations)
        questions.append(f'{a} {op} {b} = _____')
    return questions

def create_pdf(questions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)  # Set font and size
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

