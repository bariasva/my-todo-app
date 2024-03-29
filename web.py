import streamlit as st
import functions as fn

todos = fn.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My To-do App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

task_input = st.text_input(label="",placeholder="Add new task...",
                           on_change=add_todo, key='new_todo',)
