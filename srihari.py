import random
from fpdf import FPDF

DIVISION = "\u00F7"  # Division symbol

class PDF(FPDF):
    def footer(self):
        self.set_y(-10)  # Set position 1.5 cm from the bottom
        self.set_font('Helvetica', 'I', 8)  # Choose Helvetica italic 8
        page_number_text = 'Page ' + str(self.page_no())
        self.set_x((210 - self.get_string_width(page_number_text)) / 2)  # Center the page number text
        self.cell(0, 10, page_number_text)  # Page number

# Various arithmetic question functions (e.g., addition, subtraction, multiplication, division, fractions, etc.)
def addition_4():
    a = random.randint(5, 30)
    b = random.randint(5, 30)
    op = '+'
    return f'{a} {op} {b} = ____'

# add three numbers
def addition_5():
    a = random.randint(5, 40)
    b = random.randint(5, 40)
    c = random.randint(5, 40)
    op = '+'
    return f'{a} {op} {b} {op} {c} = ____'


def sub_1():
    a = random.randint(11, 99)
    b = random.randint(1, a)
    op = '-'
    return f'{a} {op} {b} = ____'
    

def subtraction_2_x():
    a = random.randint(1, 25)
    b = random.randint(1, a)
    op = '-'
    r = a - b
    return f'A {op} {b} = {r} ; A =___'

def multiplication_x():
    a, b = random.randint(2, 10), random.randint(2, 10)
    op = 'x'
    r = a * b
    return f'A {op} {b} = {r} ; A = ___'

def division():
    a, b = random.randint(2, 10), random.randint(2, 10)
    c = a * b
    op = DIVISION
    return f'{c} {op} {b} = ____'

def fraction_2():
    a = random.randint(2, 5)
    b = random.randint(1, 6)
    n = a * b
    toss = random.randint(0, 1)
    s = 0
    op = ""
    if toss == 0:
        # addition
        op = "+"
        s = random.randint(1, 5)
    else:
        # subtraction
        op = "-"
        s = random.randint(1, min(random.randint(1, 5), b))
    return f'(1/{a} x {n}) {op} {s} = ___'

def addition_3_x():
    a = random.randint(1, 11)
    y = random.randint(1, 11)
    b = random.randint(1, 11)
    s = a + y + b
    op = '+'
    return f'{a} + Y + {b} = {s}; Y = ___'


# 5 < __ < 8; 
def satisfy_ineq_0():
    z = random.randint(7, 10)
    x = random.randint(1, z-2)

    op = '+'
    return f'{x}  <  __  <  {z}'
    
# 5 x __ < 8; 
def satisfy_ineq_1():
    z = random.randint(10, 50)
    x = random.randint(2, 10)

    op = '+'
    return f'({x} x  __  ) <  {z}'


# 5 < 8 x __ ; 
def satisfy_ineq_2():
    z = random.randint(10, 30)
    x = random.randint(2, 10)

    op = '+'
    return f'{z} < ({x} x  __ )'
    

# 5 < __ + 2 < 8
def satisfy_ineq_10():
    z = random.randint(7, 10)
    y = random.randint(3, z-3)
    x = random.randint(y+1, z-2)

    op = '+'
    return f'{x}  < ( __ + {y} ) <  {z}'


def satisfy_ineq_group():
    subtypes = [
        satisfy_ineq_0,
        satisfy_ineq_1,
        satisfy_ineq_2
    ]

    choice = subtypes[random.randint(0, len(subtypes) - 1)]
    return choice()

def generate_question():
    types = [
        addition_5,
        sub_1,
        subtraction_2_x,
        division,
        fraction_2,
        addition_3_x,
        satisfy_ineq_group
    ]
    choice = types[random.randint(0, len(types) - 1)]
    return choice()

def generate_questions(num_questions):
    questions = []
    for i in range(num_questions):
        questions.append(generate_question())
    return questions

def create_pdf(questions, questions_per_page, num_columns):
    # Calculate font size and line spacing based on questions per page
    if questions_per_page <= 10:
        font_size = 24
        line_spacing = 32
    elif questions_per_page <= 20:
        font_size = 20
        line_spacing = 25
    else:
        font_size = 16
        line_spacing = 20

    column_width = 210 / num_columns - 10  # Width of each column, adjusted for margins
    column = 0  # Initialize column count

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=font_size)
    pdf.set_auto_page_break(auto=True, margin=15)
    question_count = 0

    for question in questions:
        if question_count > 0 and question_count % questions_per_page == 0:
            pdf.add_page()
            pdf.set_font("Helvetica", size=font_size)
            column = 0  # Reset column count on new page
        
        x_position = 10 + column * column_width
        pdf.set_xy(x_position, pdf.get_y())
        pdf.cell(column_width - 10, 10, question)  # Adjusted width to account for the line of separation
        if column == num_columns - 1:
            pdf.ln(line_spacing)  # Move to the next line after the last column
        column = (column + 1) % num_columns  # Increment column count, and reset to 0 if it reaches num_columns
        question_count += 1

    pdf.output('test.pdf')

questions = generate_questions(num_questions=280)  # Specify the total number of questions
create_pdf(questions, questions_per_page=20, num_columns=2)  # Specify the number of questions per page and columns
