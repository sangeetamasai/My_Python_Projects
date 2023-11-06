from tkinter import *
import random
import randomcolor
color=randomcolor.RandomColor().generate()
win = Tk()
win.title('My Notes')
win.geometry('400x600')
win.resizable(False,False)
win.configure(bg=color)

tasks = []

def create_task():
    task_text = input.get()
    if task_text:
        Tasks.insert(END, task_text)
        tasks.append(task_text)
        input.delete(0, END)  

def delete_all_task():
    Tasks.delete(0, END)
    tasks.clear()

def delete_1_task():
    selected_task = Tasks.curselection()
    if selected_task:
        index = selected_task[0]
        Tasks.delete(index)
        tasks.pop(index)

def sort_task_asd():
    tasks.sort()
    update_listbox()

def sort_task_des():
    tasks.sort(reverse=True)
    update_listbox()

def update_listbox():
    Tasks.delete(0, END)
    for task in tasks:
        Tasks.insert(END, task)

label1 = Label(win, text='To Do List',fg='blue', bg='Yellow', bd=2, font=('Arial', 20, 'bold'))
label1.pack(pady=5)  

Tasks = Listbox(win,border=2,font=('Arial',10,'bold'),fg='red')
Tasks.pack(pady=5) 

input = Entry(win, text='write here',fg='Red',font=('Arial',15,'bold'))
input.pack(pady=5)  

Create_task = Button(win, text='Add Task', fg='green', bg='white',font=('Arial',15,'bold'), command=create_task)
Create_task.pack(pady=5) 

Delete_all_task = Button(win, text='Delete all tasks',fg='green', bg='white',font=('Arial',15,'bold'),command=delete_all_task)
Delete_all_task.pack(pady=5)

Delete_a_task = Button(win, text='Delete a Task', fg='green', bg='white', font=('Arial',15,'bold'),command=delete_1_task)
Delete_a_task.pack(pady=5)  

Sort_task_asd = Button(win, text='Sort Ascending', fg='green', bg='white',font=('Arial',15,'bold'), command=sort_task_asd)
Sort_task_asd.pack(pady=5)  

Sort_task_des = Button(win, text='Sort Descending', fg='green', bg='white',font=('Arial',15,'bold'),command=sort_task_des)
Sort_task_des.pack(pady=5)  

win.mainloop()
