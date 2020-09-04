from tkinter import *

fart = int(input('Hvor fort kjører du?'))
fartsgrense = 60


def hva_fartsgrense():
    if fart > fartsgrense:
        print('Du kjører for fort')
    elif fart < fartsgrense:
        print('Du kjører for sakte')
    else:
        print('Du kjører i grensa')
        


window = Tk()
window.title('Kjører du for fort rotte')
window.geometry('700x300')

frm_entry = Frame(master=window)



windows.mainloop()
