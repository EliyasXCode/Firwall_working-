import tkinter as tk
from tkinter import messagebox, ttk
import requests
import validators

# Function to check if the site is harmful (simulating)
def is_harmful(url):
    # List of known harmful keywords or domains
    harmful_keywords = ['malware', 'phishing', 'badsite', 'dangerous', 'harmful']
    
    for keyword in harmful_keywords:
        if keyword in url:
            return True
    return False

# Function to handle URL checking
def check_url():
    url = url_entry.get()
    if not validators.url(url):
        messagebox.showerror("Invalid URL", "Please enter a valid URL")
        return

    if is_harmful(url):
        messagebox.showwarning("Blocked", f"The site '{url}' is harmful and has been blocked.")
        add_to_blocked(url)
    else:
        messagebox.showinfo("Allowed", f"The site '{url}' is safe to access.")
        add_to_allowed(url)

# Function to add site to blocked list
def add_to_blocked(url):
    blocked_list.insert(tk.END, url)
    with open("blocked_sites.txt", "a") as f:
        f.write(url + "\n")

# Function to add site to allowed list
def add_to_allowed(url):
    allowed_list.insert(tk.END, url)
    with open("allowed_sites.txt", "a") as f:
        f.write(url + "\n")

# Creating the Tkinter window
root = tk.Tk()
root.title("Firewall Simulation")
root.geometry("600x400")
root.configure(bg='#f5f5f5')

# Title
title_label = tk.Label(root, text="Firewall URL Checker", font=("Arial", 20, 'bold'), bg='#f5f5f5')
title_label.pack(pady=10)

# URL Entry Section
url_frame = tk.Frame(root, bg='#f5f5f5')
url_frame.pack(pady=10)

url_label = tk.Label(url_frame, text="Enter URL:", font=("Arial", 14), bg='#f5f5f5')
url_label.grid(row=0, column=0, padx=10)

url_entry = tk.Entry(url_frame, width=40)
url_entry.grid(row=0, column=1, padx=10)

check_button = tk.Button(url_frame, text="Check URL", command=check_url, width=15, bg='#4CAF50', fg='white')
check_button.grid(row=0, column=2, padx=10)

# Site Lists Section
list_frame = tk.Frame(root, bg='#f5f5f5')
list_frame.pack(pady=20)

# Blocked Sites Column
blocked_label = tk.Label(list_frame, text="Blocked Sites", font=("Arial", 14), bg='#f5f5f5')
blocked_label.grid(row=0, column=0, padx=20)

blocked_list = tk.Listbox(list_frame, height=10, width=30, bg='#FFCDD2', fg='#000', font=("Arial", 12))
blocked_list.grid(row=1, column=0, padx=20, pady=10)

# Allowed Sites Column
allowed_label = tk.Label(list_frame, text="Allowed Sites", font=("Arial", 14), bg='#f5f5f5')
allowed_label.grid(row=0, column=1, padx=20)

allowed_list = tk.Listbox(list_frame, height=10, width=30, bg='#C8E6C9', fg='#000', font=("Arial", 12))
allowed_list.grid(row=1, column=1, padx=20, pady=10)

# Run the main event loop
root.mainloop()
