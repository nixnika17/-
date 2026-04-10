# from pydoc import text
import tkinter as tk
import time

display = tk.Tk() #створення вікна або його определения

# назва вікна
display.state("normal") #що означає state? це стан вікна(в обсді написала детальніше)
display.title("підзарядись..будь ласка!") #хочу сюди шрифт і колір (походу неможливо)


#Встановлюємо колір фону вікна (чорний)
bg_color = "#000000"
display.configure(bg=bg_color) #конфігурація - зовнішні вигляд

# розмір іконки
display.geometry("600x300")


# текст в середині вікна і колір
label = tk.Label(display,text =  "вже час \nпідзарядитись...",
       font = ("Courier New", 20, "bold"),
       fg="#33FF00",  #колір тексту
       bg="#000000",  #Такий же фон тексту, як у вікна
       # pady=40        # Відступ зверху і знизу
) #Concul

label.pack(padx=10, pady=5) #відступи з усіх сторін


# текстове поле для введення даних
# text = tk.Text(display, height=5, width=15,
#                 font=("Courier New", 20, "bold"),
#                 fg="#33FF00",  #колір тексту
#                 bg="#000000"   #колір фону тексту
#                 )  
# text.pack()


# для малого кількостві даних
# entry = tk.Entry(display)
# entry.pack(padx=10)

button = tk.Button(display,text="немає світла",
 font = ("Courier New",20, "bold"),
   fg = "#000000", bg = "#00FF15")
button.pack(padx=0, pady=5)
 

# ну для калькудятора підійде
# butframe = tk.Frame(display)
# butframe.columnconfigure(0,weight=  1)
# butframe.columnconfigure(1,weight=  1)
# butframe.columnconfigure(2,weight=  1)

# btnl = tk.Button(butframe,text= "1", font= ("Courier New", 20, "bold"))
# btnl.grid(row=0, column= 0, sticky=tk.W+tk.E)

# btnl2 = tk.Button(butframe,text= "2", font= ("Courier New", 20, "bold"))
# btnl2.grid(row=0, column= 1, sticky=tk.W+tk.E)

# btnl3 = tk.Button(butframe,text= "3", font= ("Courier New", 20, "bold"))
# btnl3.grid(row=1, column= 2, sticky=tk.W+tk.E)

# butframe.pack()
 
#випригне поверх  програм
display.attributes("-topmost", True)#(що це -topmost?  )


#щоб вікно було по центру 
# label.pack(expand=True) #не працує,воно в рандомних точках

#Закрити вікно автоматично через 5000 мілісекунд (5 секунд)
display.after(5000, display.destroy)

display.mainloop()



