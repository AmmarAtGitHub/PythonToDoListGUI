import tkinter as tk

def add_task():
    global task_entry, todo_listbox
    # besorge task_name vom Entry field(in main()) durch get() Methode
    task_name = task_entry.get()
    if not task_name.strip(): # strip() wird die Eingabe vom leeren Tasten beseitigen
        return  # wenn empty, tur nichts
    todo_listbox.insert(tk.END, "( ) " + task_name.strip()) # Eingabe zur Liste hinzufügen + strip => leeren beseitigen
    # entry field entleeren (für nächste Eingabe, von index 0 bis zum 'END'
    task_entry.delete(0, tk.END)


def complete_task():
    global todo_listbox
    selected_task = todo_listbox.curselection() #Listbox-Widget Methode, die ein Tuple von 'cur'rently ausgewählten Indexes retourniert
    if selected_task:
        index = selected_task[0] # Index vom ausgewählten Task
        task_text = todo_listbox.get(index)
        # ist die Task bereits erledigt:
        if task_text.startswith("(x)"):
            return  # wenn ja, tue nichts, weil wir suchen nur die noch zu erledigen

        # als erledigt markieren
        todo_listbox.delete(index)
        #markiere den Task with (x) als Zeichen 'erledigt'
        todo_listbox.insert(index, "(x) " + task_text[4:])
def delete_task():
    global todo_listbox

    # besorge den ausgewählten Task Listbox
    selected_task = todo_listbox.curselection()
    if selected_task:
        index = selected_task[0]

        # den ausgewählten task vom Listbox löschen
        todo_listbox.delete(index)


def main():
    global task_entry, todo_listbox
    # hier wird main window durch Tkinter module erstellt
    myWindow = tk.Tk()  # Tk() contructor initializier neues main window (zugewiesen zu myWIndow)
    myWindow.geometry("500x500") # Methode vom Objekt (erstellt vom Tk() constructor), um die Dimentionen(widthXheight) zu etablieren
    myWindow.title("TO-DO LIST APP") #title() Methode, um das main widow ein Titel zu geben

    # Label() ist eine constructor Methode, um Label Widget zu erstellen
    title_label = tk.Label(myWindow, text="Enter Task: ")
    title_label.pack()# geometry Methde, dadurch wird das Widget automatisch zum Main Window angepasst

    # Entry field durch Entry() Methode
    task_entry = tk.Entry(myWindow, width=30)
    task_entry.pack()

    # Button für 'Add Task' funktion, wird heir durch command= add_task mit der Funktion verbunden
    add_button = tk.Button(myWindow, text="Add Task", command=add_task, bg="green", fg="white", font=("Arial", 12))
    add_button.pack()

    # Label für To-Do List
    todo_list_label = tk.Label(myWindow, text="My To-Do List")
    todo_list_label.pack()

    #Listbox() ist eine constructor Methode, um einen list box zu erstellen
    todo_listbox = tk.Listbox(myWindow, width=30, height=10)
    todo_listbox.pack()

    # Buttons für 'Complete Task' and 'Delete Task'
    complete_button = tk.Button(myWindow, text="Complete Task", command=complete_task)
    complete_button.pack(side=tk.LEFT, padx=10)
    delete_button = tk.Button(myWindow, text="Delete Task", command=delete_task)
    delete_button.pack(side=tk.RIGHT, padx=10)

    # Event-Loop starten # mailloop() ist die Event-Contriller, die Aufgaben zu Event-Handlers(bzw. Funktionen) weiterleitet.
    myWindow.mainloop()

if __name__ == "__main__":
    main()