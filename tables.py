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
    a = random.randint(1, 9)
    b = random.randint(1, 10 - a)
    op = '+'
    return f'{a} {op} {b} = _____'

def subtraction():
    a = random.randint(1, 10)
    b = random.randint(1, a)
    
    op = '-'
    return f'{a} {op} {b} = _____'

def multiplication():
    a, b = random.randint(1, 8), random.randint(1, 8)
    op = 'x'
    return f'{a} {op} {b} = _____'

# 4 + 4 + 4 + 4 + 4 = _______
def mult_1():
    a, b = random.randint(1, 8), random.randint(2, 8)
    op = '+'
    
    return f'{a} {op} '*(b-1) + f'{a} = _____'

# 
# 4 + 6 + 2 + 8 + 1 + 9 (for range = 3)
def tens_1():
    ntens = random.randint(2,5)

    s = list()
    for _ in range(ntens):
        n = random.randint(1,9)
        m = 10 - n
        s.append(f'{m}')
        s.append(f'{n}')

    return '+'.join(s) + "= _____"

# 
# 4 + 6 + 2 + 8 + 1 + 9 + 4 (for range = 3)
def tens_and_number_1():
    ntens = random.randint(2,5)

    s = list()
    for _ in range(ntens):
        n = random.randint(1,9)
        m = 10 - n
        s.append(f'{m}')
        s.append(f'{n}')

    n = random.randint(1,9)
    s.append(f'{n}')

    return '+'.join(s) + "= _____"


# 
# 4 + 2 + 6 + 8 + 9 + 1 (for range = 3)
def tens_2():
    
    ntens = random.randint(2,5)

    s = list()
    for _ in range(ntens):
        n = random.randint(1,9)
        m = 10 - n
        s.append(f'{m}')
        s.append(f'{n}')

    # make it bit harder
    random.shuffle(s)

    return '+'.join(s) + "= _____"

# 
# 4 + 2 + 6 + 8 + 9 + 1 + 2 (for range = 3)
def tens_and_number_2():
    
    ntens = random.randint(2,5)

    s = list()
    for _ in range(ntens):
        n = random.randint(1,9)
        m = 10 - n
        s.append(f'{m}')
        s.append(f'{n}')

    n = random.randint(1,9)
    s.append(f'{n}')
    
    # make it bit harder
    random.shuffle(s)

    return '+'.join(s) + "= _____"


# 4 + 3 - 3
def cancellation_1():
    a = random.randint(1, 9)
    b = random.randint(1, 10 - a)
    return f'{a} + {b} - {b} = _____'
        
     
def generate_question():
    types = [addition, subtraction, multiplication, mult_1, tens_1, tens_2,
             tens_and_number_1, tens_and_number_2, cancellation_1]

    choice = types[random.randint(0, len(types)-1)]
    
    return choice()

       
def generate_questions(num_questions=756):
    questions = []

    for i in range(num_questions):
        questions.append(generate_question())
        
    return questions

def create_pdf(questions):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)
    column_width = 90  # Width of each column
    column = 0  # Initialize column count
    for question in questions:
        x_position = 10 + column * column_width
        pdf.set_xy(x_position, pdf.get_y())
        pdf.cell(column_width - 10, 10, question)  # Adjusted width to account for the line of separation
        if column < 3:
            pdf.line(x_position + column_width - 10, pdf.get_y() - 10, x_position + column_width - 10, pdf.get_y())  # Draw line of separation
        column = (column + 1) % 2  # Increment column count, and reset to 0 if it reaches 3
        if column == 0:
            pdf.ln(10)  # Move to the next line after every third column

    pdf.output('test.pdf')


questions = generate_questions()
create_pdf(questions)

