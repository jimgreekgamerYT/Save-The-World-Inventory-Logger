import tkinter as tk

def add_item():
    item = entry.get()
    if item:
        items.append(item)  # Add the item to the list
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        save_to_file(item)  # Save the item to the file

def search_item():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)
    found = False

    for item in items:
        if query in item.lower():
            listbox.insert(tk.END, item)
            found = True

    if found:
        search_result.config(text="This item is in the list", bg="yellow")
    else:
        search_result.config(text="The item doesn't exist in the list", bg="red")

def clear_search():
    search_entry.delete(0, tk.END)
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)
    search_result.config(text="", bg="white")

def save_to_file(item):
    with open("/Desktop/STW_Logger/dist/stuff.txt", "a") as file:
        file.write(item + "\n")

def load_from_file():
    try:
        with open("/Desktop/STW_Logger/dist/stuff.txt", "r") as file:
            for line in file:
                item = line.strip()
                items.append(item)
                listbox.insert(tk.END, item)
    except FileNotFoundError:
        pass

# Create the main window
root = tk.Tk()
root.title("Save The World Inverntory Logger")
root.geometry("400x400")

# Create a listbox to display items
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

# Create an entry widget for adding items
entry = tk.Entry(root)
entry.pack(fill=tk.X)

# Create a button to add items to the list
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

# Create an entry widget for searching items
search_entry = tk.Entry(root)
search_entry.pack(fill=tk.X)

# Create a button to search items in the list
search_button = tk.Button(root, text="Search", command=search_item)
search_button.pack()

# Create a button to clear the search
clear_button = tk.Button(root, text="Clear Search", command=clear_search)
clear_button.pack()

# Create a label to display search results
search_result = tk.Label(root, text="", bg="white")
search_result.pack(fill=tk.X)

# Initialize a list of items
items = []

# Load items from the file
load_from_file()

# Start the GUI main loop
root.mainloop()
