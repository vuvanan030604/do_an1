import tkinter as tk
from tkinter import font

def switch_to_programmer():
    win.withdraw()  # Ẩn cửa sổ chính
    win2.deiconify()  # Hiển thị cửa sổ thứ hai

def switch_to_standard():
    win2.withdraw()  # Ẩn cửa sổ thứ hai
    win.deiconify()  # Hiển thị lại cửa sổ chính

# Cửa sổ chính
win = tk.Tk()
win.title('Calculations')
win.geometry('300x500')
win.attributes('-topmost', True)

fontTitle = font.Font(family='Trajan Pro', size=14)
fontText = font.Font(family='Arabic Transparent', size=10)
fontResult = font.Font(font=('Eccentric Std', 12, 'bold'))

a_label = tk.Label(win, text="Standard")
a_label.grid(column=0, row=0)

menu_bar = tk.Menu(win)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Programmer", command=switch_to_programmer)
file_menu.add_separator()
file_menu.add_command(label="Standard", command=switch_to_standard)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="|||", menu=file_menu)
win.config(menu=menu_bar)

def click_number(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Hàm xử lý khi nhấn nút phép tính
def click_operator(operator):
    global first_number
    global math_operator
    first_number = float(entry.get())
    math_operator = operator
    entry.delete(0, tk.END)

def square():
    number = float(entry.get())
    squared_number = number**2
    entry.delete(0, tk.END)
    entry.insert(0, str(squared_number))
    
def chiax():
    number = float(entry.get())
    chiax_number = 1 / number
    entry.delete(0, tk.END)
    entry.insert(0, str(chiax_number))

# Hàm xử lý khi nhấn nút bằng
def click_equal():
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if math_operator == "+":
        entry.insert(0, first_number + second_number)
    elif math_operator == "-":
        entry.insert(0, first_number - second_number)
    elif math_operator == "*":
        entry.insert(0, first_number * second_number)
    elif math_operator == "/":
        entry.insert(0, first_number / second_number)

# Hàm xử lý khi nhấn nút xóa
def click_clear():
    entry.delete(0, tk.END)

# Tạo entry để hiển thị kết quả
entry = tk.Entry(win, width=16, font=('Arial', 20), borderwidth=2, relief='solid')
entry.grid(row=2, column=0, columnspan=4)

# Tạo các nút bấm số
numbers = [
    (1, 6, 0), (2, 6, 1), (3, 6, 2),
    (4, 5, 0), (5, 5, 1), (6, 5, 2),
    (7, 4, 0), (8, 4, 1), (9, 4, 2),
    (0, 7, 1)
]

for (num, row, col) in numbers:
    button = tk.Button(win, text=str(num), padx=20, pady=20, font=('Arial', 12),
                       command=lambda num=num: click_number(num))
    button.grid(row=row, column=col)

# Tạo các nút bấm phép tính
operators = [
    ('+', 4, 3), ('-', 5, 3), ('*', 6, 3), ('/', 7, 3)
]

for (op, row, col) in operators:
    button = tk.Button(win, text=op, padx=20, pady=20, font=('Arial', 12),
                       command=lambda op=op: click_operator(op))
    button.grid(row=row, column=col)

# Tạo nút bằng
button_equal = tk.Button(win, text='=', padx=20, pady=20, font=('Arial', 12), command=click_equal)
button_equal.grid(row=7, column=2)
button_equal = tk.Button(win, text="x^2", padx=20, pady=20, font=('Arial', 10),command=square)
button_equal.grid(row=3, column=0)
button_equal = tk.Button(win, text="1/x", padx=20, pady=20, font=('Arial',10), command=chiax)
button_equal.grid(row=3, column=1)
# Tạo nút xóa
button_clear = tk.Button(win, text='C', padx=20, pady=20, font=('Arial', 12), command=click_clear)
button_clear.grid(row=7, column=0)




# Cửa sổ thứ hai
win2 = tk.Toplevel(win)
win2.title('Programmmer')
win2.geometry('300x500')
win2.attributes('-topmost', True)
win2.withdraw()  # Ẩn cửa sổ thứ hai khi khởi động

fontTitle = font.Font(family='Trajan Pro', size=14)
fontText = font.Font(family='Arabic Transparent', size=10)
fontResult = font.Font(font=('Eccentric Std', 12, 'bold'))

a_label = tk.Label(win2, text="Programmer")
a_label.grid(column=0, row=0)

menu_bar = tk.Menu(win2)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Programmer", command=switch_to_programmer)
file_menu.add_separator()
file_menu.add_command(label="Standard", command=switch_to_standard)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="|||", menu=file_menu)
win2.config(menu=menu_bar)

def click_number(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Hàm xử lý khi nhấn nút phép tính
def click_operator(operator):
    global first_number
    global math_operator
    first_number = float(entry.get())
    math_operator = operator
    entry.delete(0, tk.END)

def square():
    number = float(entry.get())
    squared_number = number**2
    entry.delete(0, tk.END)
    entry.insert(0, str(squared_number))
    
def chiax():
    number = float(entry.get())
    chiax_number = 1 / number
    entry.delete(0, tk.END)
    entry.insert(0, str(chiax_number))

# Hàm xử lý khi nhấn nút bằng
def click_equal():
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if math_operator == "+":
        entry.insert(0, first_number + second_number)
    elif math_operator == "-":
        entry.insert(0, first_number - second_number)
    elif math_operator == "*":
        entry.insert(0, first_number * second_number)
    elif math_operator == "/":
        entry.insert(0, first_number / second_number)

# Hàm xử lý khi nhấn nút xóa
def click_clear():
    entry.delete(0, tk.END)

# Tạo entry để hiển thị kết quả
entry = tk.Entry(win2, width=16, font=('Arial', 20), borderwidth=2, relief='solid')
entry.grid(row=2, column=0, columnspan=4)

# Tạo các nút bấm số
numbers = [
    (1, 6, 1), (2, 6, 2), (3, 6, 3),
    (4, 5, 1), (5, 5, 2), (6, 5, 3),
    (7, 4, 1), (8, 4, 2), (9, 4, 3),
    (0, 7, 2)
]

for (num, row, col) in numbers:
    button = tk.Button(win2, text=str(num), padx=20, pady=20, font=('Arial', 12),
                       command=lambda num=num: click_number(num))
    button.grid(row=row, column=col)

# Tạo các nút bấm phép tính
operators = [
    ('+', 4, 4), ('-', 5, 4), ('*', 6, 4), ('/', 7, 4)
]

for (op, row, col) in operators:
    button = tk.Button(win2, text=op, padx=20, pady=20, font=('Arial', 12),
                       command=lambda op=op: click_operator(op))
    button.grid(row=row, column=col)

# Tạo nút bằng
button_equal = tk.Button(win2, text='=', padx=20, pady=20, font=('Arial', 12), command=click_equal)
button_equal.grid(row=7, column=3)
button_equal = tk.Button(win2, text="x^2", padx=20, pady=20, font=('Arial', 10),command=square)
button_equal.grid(row=4, column=0)
button_equal = tk.Button(win2, text="1/x", padx=20, pady=20, font=('Arial',10), command=chiax)
button_equal.grid(row=5, column=0)
# Tạo nút xóa
button_clear = tk.Button(win2, text='C', padx=20, pady=20, font=('Arial', 12), command=click_clear)
button_clear.grid(row=7, column=1)


win.mainloop()
win2.mainloop()
