import tkinter as tk





def sub():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 - num2
    unswer_entry.delete(0, 'end')
    unswer_entry.insert(0, res)


def div():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 / num2
    unswer_entry.delete(0, 'end')
    unswer_entry.insert(0, res)


def mul():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 * num2
    unswer_entry.delete(0, 'end')
    unswer_entry.insert(0, res)


def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    unswer_entry.delete(0, 'end')
    unswer_entry.insert(0, res)





window = tk.Tk()


window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False,False)

button_add = tk.Button(window, text= '+', width= 5, height= 2,command=add)
button_add.place(x = 100 , y = 70)

button_sub = tk.Button(window,text= '-',width= 5, height=2,command=sub)
button_sub.place(x = 150, y = 70)

button_mul = tk.Button(window, text= '*', width= 5, height= 2,command=mul)
button_mul.place(x = 200 , y = 70)

button_dif = tk.Button(window,text= '/',width= 5, height=2,command=div)
button_dif.place(x = 250, y = 70)

number1_entry = tk.Entry(window,width= 32)
number1_entry.place(x = 100, y =10)
number1 = tk.Label(window, text = 'Enter 1st number')
number1.place(x = 1, y = 10)


number2_entry = tk.Entry(window, width= 32)
number2_entry.place(x = 100, y =40)
number2 = tk.Label(window, text = 'Enter 2nd number')
number2.place(x = 1, y = 40)

unswer_entry = tk.Entry(window, width= 32)
unswer_entry.place(x = 100, y =120)
unswer = tk.Label(window, text = 'Сonclusion')
unswer.place(x = 1, y = 120)
window.mainloop()