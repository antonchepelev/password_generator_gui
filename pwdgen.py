import tkinter as tk
from tkinter import ttk
import random
import string


root = tk.Tk()

#root info
root.title('Password Generator')
root.geometry("400x200")
root.iconphoto(True, tk.PhotoImage(file='/home/achepelev/Pictures/Iron-Devil-Ids-3d-Icons-20-Dousojin.32.png'))
root.configure(background='#C3DCCC')
root.resizable(False,False)
root.tk.call('tk', 'scaling', 2)
#styles for widgets
style = ttk.Style()
style.theme_create('soft', parent='alt')           
style.theme_use('soft')
style.configure('soft.TButton', background = '#CBC3DC', foreground = '#73787D', font = ('Ubuntu',12,'bold',),relief = 'raised')
style.configure('soft.TMenubutton', background = '#CBC3DC',foreground = '#73787D', arrowcolor = '#73787D',font = ('Times New Roman',13,'bold'), 
relief = 'solid',bordercolor = '#73787D' )
style.configure('soft.TSpinbox',background = '#CBC3DC', bordercolor = '#73787D',arrowcolor = '#73787D',
                font = ('Arial',16,'bold'),selectbackground = '#CBC3DC',selectforeground = '#73787D',fieldbackground = '#CBC3DC',relief = 'flat',)


def click_value():
    global length
    number = int(length_spinbox.get())
    length = 0
    length += number

#pwd is made based on desired length info from spinbox widget and type from option menu
def on_select(value):
   
    global  output_text, length, style

    output_text.configure(state='disabled')
    output_text.delete('1.0','end')
    
    has_special = False
    has_number = False
    has_both = False
    letters = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation
    meets_criteria = False

    pwd=""

    characters = letters

    if value == 'Special':
        has_special = True
    if value == 'Numbers':
        has_number = True
    if value == 'Both':
        has_both = True
    
    if has_special:
        characters += special
        
    if has_number:
        characters += numbers
        
    if has_both:
        characters += numbers
        characters += special
       
    try:
        while not meets_criteria:
            new_char = random.choice(characters)
            pwd += new_char
            if new_char in characters and len(pwd) == length:
                meets_criteria = True
        style.configure('soft.TSpinbox',background = '#CBC3DC', foreground = 'black', bordercolor = '#73787D',arrowcolor = '#73787D',
                font = ('Arial',16,'bold'),selectbackground = '#CBC3DC',selectforeground = '#73787D',fieldbackground = '#CBC3DC',relief = 'flat',)
        
    except NameError:
        
        style.configure('soft.TSpinbox', bordercolor = 'red')
   

    output_text.insert("end",pwd)
    if meets_criteria == True:  
       output_text.configure(state='normal')
    return pwd
    
#grabs pwd type from option menu and returns to output text 
def c_button_call():
    global output_text
    output_text.configure(state='normal')
    output_text.delete('1.0', 'end')
    pwd = on_select(selected_value.get())
    output_text.insert("end", pwd)
    output_text.configure(state='disabled')


length_spinbox = ttk.Spinbox(root,wrap = True,  from_=1, to=15, increment=1, width=2,takefocus=0,
                             state = 'readonly',style = 'soft.TSpinbox',command= click_value)

length_spinbox.place(x=117)  


selected_value = tk.StringVar()


option_menu = ttk.OptionMenu(root,selected_value, 'SELECT','Special','Numbers','Both',command=on_select,style= 'soft.TMenubutton',direction='right')
option_menu.configure(width=10)
option_menu.place(x=185,y=0)


output_frame = ttk.Frame()
output_font = ("Arial", 12, "bold")
output_text =tk.Text(output_frame,height=1,width=20, background= '#CBC3DC',foreground='#73787D',
                     font = output_font,selectbackground='#C4C3DC',selectforeground='black',
                            relief='flat',state='disabled')

output_text.pack()
output_frame.place(x=115,y=70)



    


create_button = ttk.Button(text='CREATE',width=9,style ='soft.TButton',command = c_button_call)
create_button.place(x=160,y=100)


root.mainloop()