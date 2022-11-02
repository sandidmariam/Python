#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter.ttk import *
from langdetect import detect
from iso639 import languages

# Creation d'objet
root = Tk()

style = Style()



# position de titre et button
root.geometry("500x520")
root.title('Detection Language App')
style.configure('TButton', font =
               ('calibri', 10, 'bold','underline'),
                    borderwidth = '3')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])
#fonction pour la detection de language 

def language_detection():
    
    
    text = inputText.get("1.0", END)

# avoir la language
    language_code = languages.get(alpha2=detect(text))
    l_d.config(text="Language Detected:- "+language_code.name)


# input text
inputText = Text(root)
inputText.pack()

# label
l_d = Label(root, text="Language Detected:- ")
l_d.pack(pady=10)

# Button
Button(root, text='Detect Language', command=language_detection).pack(side=LEFT,padx=2,pady=0)
btn1 = Button(root, text = 'Quit !', command = root.destroy).pack(pady=0, padx=2 , side=RIGHT)





# Execute Mainloop
root.mainloop()


# In[ ]:





# In[ ]:




