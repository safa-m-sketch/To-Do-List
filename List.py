import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root=tk.Tk()
#Background color of "screen"
root.configure(bg = "#A3DAFF")
root.geometry("400x400")
#list that holds the goals
goals = []
#presents the tasks on output Listbox
def presentTasks():
    taskoutput.delete(0, tk.END)
    #use importance,g since list holds 2
    for importance,g in goals:
        taskoutput.insert(tk.END, f"[{importance}], {g}")

def add_goal():
    #gets the goal from input area
    goal = input.get()
    #gets how important the task is from dropdown
    importance  = important.get()
    #makes sure the goal isn't blank and if it is error pops up
    if goal != "":
        #add the goal to the list
        goals.append((importance, goal))
        #output the tasks on the listbox
        presentTasks()
        input.delete(0, tk.END)
        #reset the dropdown
        important_box.set("Medium")
    else:
        messagebox.showwarning("Error", "Try Again!")

def complete_goal():
    try:
        #find the index of the selected goal
        selected_goal = taskoutput.curselection()[0]
        #using the index found delete that goal from the list
        del goals[selected_goal]
        #output the tasks again
        presentTasks()
    except IndexError:
        messagebox.showwarning("Error", "Try Again!")

#What will you achieve today displayed
label = tk.Label(root, text="WHAT WILL YOU ACHIEVE TODAY?", font = ("Courier", 16, "bold underline"), fg = "#0E0A4E", bg = "#A3DAFF")
label.pack(pady=5)
#the input area to enter goals
input = tk.Entry(root, font = ("Calibri", 16), width = 30, justify = "right") #creates text entry, root parent window, how wide panel is in character, get text typed in with entry.get
input.pack(pady=3) #pack displays it on window and pady is for spacing
important = tk.StringVar()
#style of the dropdown (background and font don't work on Windows)
style = ttk.Style()
style.configure("TCombobox", foreground = "#0A4E0D", background = "#D2FCD7", font = "Courier")
important_box = ttk.Combobox(root, textvariable = important, values = ["High", "Medium", "Low"], state = "readonly")
important_box.set("Medium")
important_box.pack(pady=(2,2))
#taskoutput and scrollbar together
goal_frame = tk.Frame(root, bg = "#A3DAFF")
goal_frame.pack(pady=10)
taskoutput = tk.Listbox(goal_frame, width = 30, height = 10, bg = "#C1F6FA", font = ("Calibri", 15))
taskoutput.pack(side = tk.LEFT, fill = tk.BOTH)
#command equals (scrollbar controls listbox)
scrollbar = tk.Scrollbar(goal_frame, orient= tk.VERTICAL, command = taskoutput.yview)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
#Listbox updates scrollbar (without this no updates)
taskoutput.config(yscrollcommand = scrollbar.set)
style.configure("effect.TButton", foreground = "#0A4E0D", background = "#D2FCD7")
#effects for hovering
style.map("effect.TButton", background = [("active", "#606060"), ("pressed", "#202020")], foreground = [("active", "#0A4E0D"), ("pressed", "#0A4E0D")])
#add and complete button
add_button = ttk.Button(root, text = "Add Goal", style = "effect.TButton", command = add_goal)
add_button.place(x=90, y=370)
complete_button = ttk.Button(root, text = "Mark as Complete", style = "effect.TButton", command = complete_goal)
complete_button.place(x=190, y=370)
root.resizable(False, False)
#connect keys
root.bind("<Return>", lambda event: add_goal())
root.bind("<Delete>", lambda event: complete_goal())
root.mainloop()