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
    column_width = 60  # Width of each column
    column = 0  # Initialize column count
    for question in questions:
        x_position = 10 + column * column_width
        pdf.set_xy(x_position, pdf.get_y())
        pdf.cell(column_width - 10, 10, question)  # Adjusted width to account for the line of separation
        if column < 2:
            pdf.line(x_position + column_width - 10, pdf.get_y() - 10, x_position + column_width - 10, pdf.get_y())  # Draw line of separation
        column = (column + 1) % 3  # Increment column count, and reset to 0 if it reaches 3
        if column == 0:
            pdf.ln(10)  # Move to the next line after every third column

    pdf.output('test.pdf')


questions = generate_questions()
create_pdf(questions)

