import tkinter as tk
from chatbot_logic import set_key, chat, set_speak_mode, set_record_mode

def create_main_window():
    # create the main window
    root = tk.Tk()
    root.geometry("1000x700")
    root.configure(bg="#717171")
    root.title("ChatBot")
    return root

def create_chat_box(root):
    # create chat box
    chat_box = tk.Text(root, bg="#959595", fg="#333", font=("Helvetica", 12))
    chat_box.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)
    return chat_box

def create_bottom_panel(root):
    # create bottom panel
    bottom_panel = tk.Frame(root, bg="#cccccc")
    bottom_panel.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)
    return bottom_panel

def create_input_box(bottom_panel):
    # create input box
    input_box = tk.Entry(bottom_panel, bg="#e6e6e6", fg="#333", font=("Helvetica", 12))
    input_box.place(relx=0.05, rely=0.2, relwidth=0.7, relheight=0.3)
    return input_box

def create_send_button(bottom_panel, input_box, chat_box):
    # create send button
    def send_message():
        message = input_box.get()
        chat_box.insert(tk.END, "\n")
        chat_box.insert(tk.END, ">> ", "bold")
        chat_box.insert(tk.END, message)
        input_box.delete(0, tk.END)

    send_button = tk.Button(bottom_panel, text="Send", command=send_message, bg="#999999", fg="#ffffff", font=("Helvetica", 12))
    send_button.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.3)
    return send_button

def create_talk_button(root, chat_box):

    def on_talk_button_pressed():
        set_speak_mode()
        chat_box.insert(tk.END, '\n' + "Talking mode active")

    # create talk button
    talk_button = tk.Button(root, text="Talk", command=on_talk_button_pressed , bg="#999999", fg="#ffffff", font=("Helvetica", 12))
    talk_button.place(relx=0.10, rely=0.9, relwidth=0.1, relheight=0.04)
    return talk_button

def create_record_button(root, chat_box):

    def on_record_button_pressed():
        set_record_mode()
        chat_box.insert(tk.END, '\n' + "Recording mode active")

    # create record button
    record_button = tk.Button(root, text="Record", command=on_record_button_pressed, bg="#999999", fg="#ffffff", font=("Helvetica", 12))
    record_button.place(relx=0.25, rely=0.9, relwidth=0.1, relheight=0.04)
    return record_button

def run_gui():
    root = create_main_window()
    chat_box = create_chat_box(root)
    bottom_panel = create_bottom_panel(root)
    input_box = create_input_box(bottom_panel)
    send_button = create_send_button(bottom_panel, input_box, chat_box)
    talk_button = create_talk_button(root, chat_box)
    record_button = create_record_button(root, chat_box)
    root.mainloop()

if __name__ == '__main__':
    run_gui()
