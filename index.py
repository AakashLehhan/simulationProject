import os
def sud():
    os.system('ttt.py')
def mn():
    os.system('mnc.py')
def tt():
    from ttt import ttt
    ttt()
def main():
    from tkinter import Tk, Label, Button, Canvas, mainloop, PhotoImage
    master = Tk()

    master.geometry('400x500+484+100')
    master.configure(bg = '#e6caca')
    master.title("Homepage")

    blank_label = Label(text = '',
                        bg = '#e6caca')
    blank_label.pack()
    
    infoPane = Canvas(master,
                      height = '400',
                      width = '400',
                      bg = '#f7ebeb')
    infoPane.pack()

    infoPane.create_text(200, 25,
                         text = "WELCOME",
                         font = 'calibri 20 bold')
    infoPane.create_rectangle(10, 50, 390, 150,
                              fill = '#e04a31',
                              outline = '#e04a31')
    infoPane.create_text(200, 100,
                         text = "\tThis page has navigations to problems \nwhich basically checks the correction status of your solution \n\t        with background processing.",
                         font = 'calibri 11 bold')

    sudokuImg = PhotoImage(file = 'icons/sudoku.png')
    mncImg = PhotoImage(file = 'icons/mnc.png')
    tttImg = PhotoImage(file = 'icons/ttt.png')

    sudokuBtn = Button(master,
                       image = sudokuImg,
                       bd = '0',
                       bg = '#f7ebeb',
                       activebackground = '#f7ebeb',
                       command = sud)
    mncBtn = Button(master,
                    image = mncImg,
                    bd = '0',
                    bg = '#f7ebeb',
                    activebackground = '#f7ebeb',
                    text = 'mnc',
                    command = mn)
    tttBtn = Button(master,
                    image = tttImg,
                    bd = '0',
                    bg = '#f7ebeb',
                    activebackground = '#f7ebeb',
                    text = 'mnc',
                    command = tt)
    
    infoPane.create_window(150, 250,
                           window = sudokuBtn)
    infoPane.create_window(250, 250,
                           window = mncBtn)
    infoPane.create_window(200, 350,
                           window = tttBtn)
    mainloop()

if __name__ == "__main__":
    main()
    
