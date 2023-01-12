import pyttsx3
from tkinter import *
import os
window = Tk()
window.geometry('450x300')
window.resizable(0,0)
window.title('Text to speech python project')
window.configure(bg='AliceBlue')


eng = pyttsx3.init() # object

# title label
Label(window,text='Text to Speech',font='Calibri 18 bold',bg='Red',fg='blue2').pack()
# bottom label


# text box label and text box
msg = StringVar()
Label(window,text= 'Enter Text',font='Calibri 18 bold',bg='AliceBlue').place(x=40,y=60)
entry_field = Entry(window, textvariable=msg, width=60)
entry_field.place(x=40,y=100,height=25)


voices = eng.getProperty('voices')
_voice = True
# functions for converting text to speech
def toggle_voice():
    global _voice
    if _voice:
        eng.setProperty('voice', voices[1].id)  # female
        _voice = False
    else:
        eng.setProperty('voice', voices[0].id)
        _voice = True



def text_to_speech():

    message = entry_field.get()
    eng.say(message)  # covert text to speech

    # engine.save_to_file(message, 't2s.mp3')  # we can also save into audio
    eng.runAndWait()   # play the speech

    eng.stop()

def exit():
    window.destroy()

def reset():
    msg.set('')

# buttons
Button(window,text='Play',font='Calibri 13 bold', command=text_to_speech,bg='Cyan').place(x=60,y=150)
Button(window,text='Reset',font='Calibri 13 bold', command=reset,bg='red').place(x=180,y=150)
Button(window,text='Exit',font='Calibri  13 bold', command=exit,bg='cyan').place(x=310,y=150)
Button(window,text='ChangeVoice',font='Calibri 15 bold', command=toggle_voice,bg='Red').place(x=130,y=220)

window.mainloop()
