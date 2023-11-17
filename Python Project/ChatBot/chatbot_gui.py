import tkinter as tk
from chatbot_logic import get_response  # Replace this with your chatbot logic function

def send_message():
    user_message = user_input.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_message + "\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)

    bot_response = get_response(user_message)  # Replace this with your chatbot logic function call

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)
    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x500")

chat_log = tk.Text(root, wrap="word", state=tk.DISABLED)
chat_log.pack(expand=True, fill=tk.BOTH)

user_input = tk.Entry(root, width=60)
user_input.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
