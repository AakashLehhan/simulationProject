def sud():
    from sudoku import sudoku
    sudoku()
def mn():
    from mnc import mc
    mc()
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
    
    infoPane.create_window(100, 250,
                           window = sudokuBtn)
    infoPane.create_window(300, 250,
                           window = mncBtn)
    mainloop()

if __name__ == "__main__":
    main()
    
