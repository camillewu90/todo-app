import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label, input_box, add_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todo = values["todo"] + '\n'
            todos = functions.read_todos()
            todos.append(todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

