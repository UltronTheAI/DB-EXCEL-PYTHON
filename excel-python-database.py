from tkinter import *
import os

try:
    import pyperclip
except EXCEPTION as ex:
    os.system('pip install pyperclip')
try:
    import openpyxl
except EXCEPTION as ex:
    os.system('pip install openpyxl')
try:
    import pynput
except EXCEPTION as ex:
    os.system('pip install pynput')
import time

mouse = pynput.mouse.Controller()
key_bord = pynput.keyboard.Controller()
key_code = pynput.keyboard.KeyCode
button = pynput.mouse.Button


def set_mouse_position(x=0, y=0):
    mouse.position = (x, y)


# try:
#     image = PhotoImage(file = 'logo.png')
#     Border = Label(border = 0, image = image)
#     Border.place(x = 0, y = 0)
# except:
#     os.system('cd.> logo.png')
#     # with open('logo.png', 'bw') as file:
#     #     file.write('')
#     #     file.close()
#     image = PhotoImage(file = 'logo.png')
#     Border = Label(border = 0, image = image)
#     Border.place(x = 0, y = 0)
db_excel_python = Tk()
db_excel_python.wm_attributes('-transparentcolor', 'black')
db_excel_python.attributes('-alpha', 0.50)
db_excel_python.overrideredirect(1)
db_excel_python.resizable(0, 0)
db_excel_python.title('db-excel-python')

db_excel_python.geometry('952x519+600+300')
image = PhotoImage(file='git.png')
image_p = PhotoImage(file='git-fs-2.png')
Border = Label(border=0, image=image)
Border_p1 = Label(border=0, image=image_p)
Border.place(x=0, y=0)
i = 0
lp = Label(bg='black', padx=i)

for i in range(0, 480):
    time.sleep(0.01)
    db_excel_python.update()
    db_excel_python.update_idletasks()
    lp['padx'] = i
    lp.place(x=0, y=350)
lp.place(x=9000)
db_excel_python.update_idletasks()
db_excel_python.update()
db_excel_python.overrideredirect(0)
db_excel_python.attributes('-fullscreen', True)
# db_excel_python.overrideredirect(1)


# code
# new_button = Label(text = 'FILE', fg = 'white', padx = 20)
# new_button.place(x = 0, y = 0)
image = PhotoImage(file='git-fs.png')
Border['image'] = image
db_excel_python.wm_attributes('-transparentcolor', 'black')
db_excel_python.attributes('-alpha', 0.60)
db_excel_python.update()
db_excel_python.update_idletasks()


# set_mouse_position(90, 80)
# z = Label(bg='white', padx=200, pady=550)
# z.place(x=1000, y=3000)
#

# page = 1


def cl_p(e_P=''):
    # global page
    print(e_P)
    print('mouse')
    x = mouse.position[0]
    y = mouse.position[1]
    print(x)
    print(y)
    if x < 170 and x > 0 and y > 0 and y < 76:
        Border_p1 = Label(border=0, image=image_p)
        Border_p1.place(x=0, y=0)
        Border_p1.bind('<Button-1>', cl_p_1)
        # Border.place(x = 9000, y = 9000)
        # page = 2
        # print('page = ' + page)
    # page = 2
    # db_excel_python.wm_attributes('-transparentcolor', 'black')
    # db_excel_python.attributes('-alpha', 0.60)
    # db_excel_python.update_idletasks()
    # db_excel_python.update() 396 495


def cl_p_1(e_p=''):
    print(e_p)
    print('mouse')
    x = mouse.position[0]
    y = mouse.position[1]
    print(x)
    print(y)
    if x < 600 and x > 0 and y > 400 and y < 506:
        Border = Label(border=0, image=image)
        Border.bind('<Button-1>', cl_p)
        Border.place(x=0, y=0)
        # Border_p1.place(x = 9000, y = 9000)
        # page = 1
        # print('page = ' + str(page))
    if x < 600 and x > 0 and y > 550 and y < 656:
        exit()


# cl_p('')
Border.bind('<Button-1>', cl_p)
Border_p1.bind('<Button-1>', cl_p_1)
db_excel_python.mainloop()
