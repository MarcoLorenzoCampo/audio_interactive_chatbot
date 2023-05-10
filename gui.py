import tkinter as tk
from chatbot_logic import set_key, chat, set_speak_mode, set_record_mode, send_to_open_ai, get_messages


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.chat_box = None
        self.bottom_panel = None
        self.input_box = None
        self.send_button = None
        self.talk_button = None
        self.record_button = None

    def create_main_window(self):
        # create the main window
        self.root.geometry("1000x700")
        self.root.configure(bg="#717171")
        self.root.title("ChatBot")

    def create_chat_box(self):
        # create chat box
        self.chat_box = tk.Text(self.root, bg="#959595", fg="#333", font=("Helvetica", 12))
        self.chat_box.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)

    def create_bottom_panel(self):
        # create bottom panel
        self.bottom_panel = tk.Frame(self.root, bg="#cccccc")
        self.bottom_panel.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

    def create_input_box(self):
        # create input box
        self.input_box = tk.Entry(self.bottom_panel, bg="#e6e6e6", fg="#333", font=("Helvetica", 12))
        self.input_box.place(relx=0.05, rely=0.2, relwidth=0.7, relheight=0.3)

    def create_send_button(self):
        # create send button
        def send_question():
            question = self.input_box.get()
            self.chat_box.insert(tk.END, "\n")
            self.chat_box.insert(tk.END, ">> ", "bold")
            self.chat_box.insert(tk.END, question + '\n')
            self.input_box.delete(0, tk.END)
            self.chat_box.insert(tk.END, '\n' + 'ChatGpt: ' + send_to_open_ai(question) + '\n')

        self.send_button = tk.Button(self.bottom_panel, text="Send", command=send_question,
                                     bg="#999999", fg="#ffffff", font=("Helvetica", 12))
        self.send_button.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.3)

    def create_talk_button(self):
        def on_talk_button_pressed():
            output = set_speak_mode()
            self.chat_box.insert(tk.END, '\n' + output)

        # create talk button
        self.talk_button = tk.Button(self.root, text="Talk", command=on_talk_button_pressed,
                                     bg="#999999", fg="#ffffff", font=("Helvetica", 12))
        self.talk_button.place(relx=0.10, rely=0.9, relwidth=0.1, relheight=0.04)

    def create_record_button(self):
        def on_record_button_pressed():
            output = set_record_mode()
            self.chat_box.insert(tk.END, '\n' + output)

        # create record button
        self.record_button = tk.Button(self.root, text="Record", command=on_record_button_pressed,
                                       bg="#999999", fg="#ffffff", font=("Helvetica", 12))
        self.record_button.place(relx=0.25, rely=0.9, relwidth=0.1, relheight=0.04)

    def run_gui(self):
        self.create_main_window()
        self.create_chat_box()
        self.create_bottom_panel()
        self.create_input_box()
        self.create_send_button()
        self.create_talk_button()
        self.create_record_button()

        self.root.mainloop()
    
    def get_chat_box(self):
        return self.chat_box

    def get_bottom_panel(self):
        return self.bottom_panel

    def get_input_box(self):
        return self.input_box

    def get_send_button(self):
        return self.send_button

    def get_talk_button(self):
        return self.talk_button

    def get_record_button(self):
        return self.record_button


if __name__ == '__main__':
    set_key()
    gui = GUI()
    gui.run_gui()
