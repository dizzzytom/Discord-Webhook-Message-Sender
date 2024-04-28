import tkinter as tk
import requests

def send_message():
    message = entry.get()
    webhook_url = ""
    data = {"content": message}
    requests.post(webhook_url, json=data)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Discord Webhook Message Sender")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
