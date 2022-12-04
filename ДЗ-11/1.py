import requests
import json
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("180x80")
root.resizable(width=False, height=False)

entry = ttk.Entry()
entry.pack(padx=8, pady=8, anchor=N)


def btn_func():
    username = entry.get()
    url = f"https://api.github.com/users/{username}"

    user_data = requests.get(url).json()
    new_user_data = {
        "company": user_data["company"],
        "created_at": user_data["created_at"],
        "email": user_data["email"],
        "id": user_data["id"],
        "name": user_data["name"],
        "url": user_data["url"],
    }

    with open('file.txt', 'w') as outfile:
        json.dump(new_user_data, outfile)


btn = ttk.Button(text="Get JSON", command=btn_func)
btn.pack(anchor=N, padx=6, pady=6)

root.mainloop()
