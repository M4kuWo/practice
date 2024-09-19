import tkinter as tk
from tkinter import messagebox
import requests

# Set the base URL for the Flask API
BASE_URL = "http://127.0.0.1:5000"

def get_videogames():
    """Fetch and display all video games from the API."""
    response = requests.get(f"{BASE_URL}/videogames")
    
    if response.status_code == 200:
        videogames = response.json()
        display_videogames(videogames)
    else:
        messagebox.showerror("Error", "Failed to fetch video games")

def display_videogames(videogames):
    """Clear and display video games in the text box."""
    text_box.delete(1.0, tk.END)  # Clear the text box
    for game in videogames:
        text_box.insert(tk.END, f"ID: {game['Id']} | Title: {game['Title']} | Year: {game['ReleaseYear']} | Category: {game['Category']}\n")

def add_videogame():
    """Add a new video game to the database via the API."""
    title = title_entry.get()
    year = year_entry.get()
    category_id = category_entry.get()

    if title and year and category_id:
        try:
            data = {
                "Title": title,
                "ReleaseYear": int(year),
                "CategoryId": int(category_id)
            }
            response = requests.post(f"{BASE_URL}/videogames", json=data)

            if response.status_code == 201:
                messagebox.showinfo("Success", "Video game added successfully")
                title_entry.delete(0, tk.END)
                year_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)
                get_videogames()
            else:
                messagebox.showerror("Error", "Failed to add video game")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid data")
    else:
        messagebox.showwarning("Input Error", "All fields are required")

# Create the main window
root = tk.Tk()
root.title("Video Game Wishlist")

# Title Label and Entry
title_label = tk.Label(root, text="Title:")
title_label.grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

# Release Year Label and Entry
year_label = tk.Label(root, text="Release Year:")
year_label.grid(row=1, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=1, column=1)

# Category ID Label and Entry
category_label = tk.Label(root, text="Category ID:")
category_label.grid(row=2, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=2, column=1)

# Add Video Game Button
add_button = tk.Button(root, text="Add Video Game", command=add_videogame)
add_button.grid(row=3, column=0, columnspan=2)

# Text Box to Display Video Games
text_box = tk.Text(root, height=10, width=50)
text_box.grid(row=4, column=0, columnspan=2)

# Refresh Button to Load Video Games
refresh_button = tk.Button(root, text="Load Video Games", command=get_videogames)
refresh_button.grid(row=5, column=0, columnspan=2)

# Start the Tkinter loop
root.mainloop()
