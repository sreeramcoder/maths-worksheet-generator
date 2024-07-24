import random
from fpdf import FPDF

DIVISION = "\u00F7"

class PDF(FPDF):
    def footer(self):
        self.set_y(-10)  # Set position 1.5 cm from the bottom
        self.set_font('Helvetica', 'I', 8)  # Choose Arial italic 8
        page_number_text = 'Page ' + str(self.page_no())
        self.set_x((210 - self.get_string_width(page_number_text)) / 2)  # Center the page number text
        self.cell(0, 10, page_number_text)  # Page number
        
# 2 + 7 = ______
def addition():
    a = random.randint(1, 9)
    b = random.randint(1, 10 - a)
    op = '+'
    return f'{a} {op} {b} = _____'

# 6 + 8 = ______
def addition_2():
    a = random.randint(1, 9)
    b = random.randint(1, 14 - a)
    op = '+'
    return f'{a} {op} {b} = _____'

# 1 + Y + 8 = 10
def addition_3_x():
    
    a = random.randint(1, 5)
    y = random.randint(1, 5)
    b = random.randint(1, 5)
    s = a + y + b
    op = '+'
    return f'{a} + Y + {b} = {s}; Y = ___'


# Y + 8 = 14
def addition_2_x():
    a = random.randint(1, 10)
    b = random.randint(1, 20 - a)
    op = '+'
    r = a + b
    return f'Y {op} {b} = {r} ; Y = ___'

# 30 + 80 = ______
def addition_3():
    a = random.randint(1, 10)
    b = random.randint(1, 18 - a)

    a *= 10
    b *= 10
    
    op = '+'
    
    return f'{a} {op} {b} = ____'

# 12 + 15 = ______
def addition_4():
    a = random.randint(5, 20)
    b = random.randint(5, 20)

    op = '+'
    
    return f'{a} {op} {b} = ____'

# 1/2 of 4 = 
def fraction_1():

    a = random.randint(2,6)
    b = min(random.randint(1, 2), a-1)
    n = a*random.randint(1,7)

    return f'({b}/{a}) x {n} = ___'

# (1/2 x 4) +- 2 = 
def fraction_2():
    a = random.randint(2,4)
    b = random.randint(1,5)
    n = a*b

    toss = random.randint(0,1)
    s = 0
    op = ""
    if toss==0:
        #addition
        op = "+"
        s = random.randint(1,5)
    else:
        #sub
        op = "-"
        s = random.randint(1,min(random.randint(1,5),b))

    return f'(1/{a} x {n}) {op} {s} = ___'


# 5 - 2 = _____
def subtraction():
    a = random.randint(1, 10)
    b = random.randint(1, a)
    
    op = '-'
    return f'{a} {op} {b} = _____'

# 12 - 2 = _____
def subtraction_2():
    a = random.randint(1, 15)
    b = min(10, random.randint(1, a))
    
    op = '-'
    return f'{a} {op} {b} = _____'

# 12 - 2 = _____
def subtraction_2_x():
    a = random.randint(1, 25)
    b = random.randint(1, a)
    
    op = '-'
    r = a - b
    return f'A {op} {b} = {r} ; A =___'


def multiplication():
    a, b = random.randint(2, 10), random.randint(2, 10)
    op = 'x'
    return f'{a} {op} {b} = ___'

# A x 4 = 20; A = 
def multiplication_x():
    a, b = random.randint(2, 10), random.randint(2, 10)
    op = 'x'
    r = a * b
    return f'A {op} {b} = {r} ; A = ___'

# 4 + 4 + 4 + 4 + 4 = _______
def mult_1():
    a, b = random.randint(1, 9), random.randint(2, 6)
    op = '+'
    
    return f'{a} {op} '*(b-1) + f'{a} = ___'

# 24 / 4 = _____
def division():
    a, b = random.randint(2, 10), random.randint(2, 10)
    c = a * b
    op = DIVISION
    return f'{c} {op} {b} = ____'


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

    return '+'.join(s) + "= ___"

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

    return '+'.join(s) + "= ___"


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

    return '+'.join(s) + "= ___"

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

    return '+'.join(s) + "= ___"


# 4 + 3 - 3
def cancellation_1():
    a = random.randint(1, 9)
    b = random.randint(1, 15 - a)
    return f'{a} + {b} - {b} = ___'

# 3 + 4 - 3
def cancellation_2():
    a = random.randint(1, 9)
    b = random.randint(1, 15 - a)
    return f'{b} + {a} - {b} = ___'


# (5 x 4) +- 1 = ___
def paren():
    a, b = random.randint(2, 10), random.randint(2, 10)
    op = 'x'


    toss = random.randint(0, 1)
    if toss == 0:
        # addition
        op = "+"
        c = random.randint(1, 10)
    else:
        op = "-"
        c = min(random.randint(1, 10), a*b)
        
    return f'({a} x {b}) {op} {c} = ___'


# 1 + (5 x 4) = ___
def paren_3():
    a, b = random.randint(2, 10), random.randint(2, 10)
    op = 'x'
    c = random.randint(1, 6)    
    return f'{c} + ({a} {op} {b}) = ___'


def generate_question():
    #types = [addition, subtraction, multiplication, mult_1, tens_1, tens_2,
    #         tens_and_number_1, tens_and_number_2, cancellation_1]

    types = [
             addition_4,
             subtraction_2_x,
             multiplication_x,
             division,
             fraction_2,
             addition_3_x
    ]


    choice = types[random.randint(0, len(types)-1)]
    
    return choice()

       
def generate_questions(num_questions=28*14):
    # per page 54 questions
    questions = []

    for i in range(num_questions):
        questions.append(generate_question())
        
    return questions

def create_pdf(questions):
    column_width = 110  # Width of each column
    column = 0  # Initialize column count
    line_spacing = 20
    font_size = 18
    
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=font_size)
    pdf.set_auto_page_break(auto=True, margin=15)
    for question in questions:
        x_position = 10 + column * column_width
        pdf.set_xy(x_position, pdf.get_y())
        pdf.cell(column_width - 10, 10, question)  # Adjusted width to account for the line of separation
        if column == 0:
            pdf.line(x_position + column_width - 10, pdf.get_y() , x_position + column_width - 10, pdf.get_y()+line_spacing)  #raw line of separation
        column = (column + 1) % 2  # Increment column count, and reset to 0 if it reaches 3
        if column == 0:
            pdf.ln(line_spacing)  # Move to the next line after every third column

    pdf.output('test.pdf')


questions = generate_questions()
create_pdf(questions)

