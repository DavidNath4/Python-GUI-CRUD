import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    keluhan = keluhan_text.get("1.0", "end-1c")  # Get text from the Text widget

    if not name or not age or not email or not phone or not keluhan:
        messagebox.showerror("Error", "All fields are required!")
    else:
        selected_item = data_tree.selection()
        if selected_item:
            # Get the existing patient ID from the selected row
            patient_id = data_tree.item(selected_item, 'values')[4]
            data_tree.item(selected_item, values=(name, age, email, phone, keluhan, patient_id))
            clear_entries()
            messagebox.showinfo("Success", "Data updated successfully!")
        else:
            # Generate a new patient ID for new data
            patient_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            data_tree.insert('', 'end', values=(name, age, email, phone, keluhan, patient_id))
            clear_entries()
            # messagebox.showinfo("Success", "Data submitted successfully!")

def edit_data(event):
    selected_item = data_tree.selection()
    if selected_item:
        values = data_tree.item(selected_item, 'values')
        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        keluhan_text.delete("1.0", "end")  # Clear the Text widget
        name_entry.insert(0, values[0])
        age_entry.insert(0, values[1])
        email_entry.insert(0, values[2])
        phone_entry.insert(0, values[3])
        keluhan_text.insert("1.0", values[4])  # Populate the Text widget

def delete_data():
    selected_item = data_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select a row to delete.")
    else:
        data_tree.delete(selected_item)
        messagebox.showinfo("Success", "Data deleted successfully!")

def clear_entries():
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    keluhan_text.delete("1.0", "end")  # Clear the Text widget

app = tk.Tk()
app.title("Data Input Form")

name_label = tk.Label(app, text="Nama Pasien:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(app, justify="left")
name_entry.grid(row=0, column=1)

age_label = tk.Label(app, text="Umur Pasien:")
age_label.grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(app, justify="left")
age_entry.grid(row=1, column=1)

email_label = tk.Label(app, text="Email:")
email_label.grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(app, justify="left")
email_entry.grid(row=2, column=1)

phone_label = tk.Label(app, text="No. Tlp:")
phone_label.grid(row=3, column=0, sticky="w")
phone_entry = tk.Entry(app, justify="left")
phone_entry.grid(row=3, column=1)

keluhan_label = tk.Label(app, text="Keluhan:")
keluhan_label.grid(row=4, column=0, sticky="w")

# Create a Text widget for the Keluhan field
keluhan_text = tk.Text(app, height=5, width=30)
keluhan_text.grid(row=4, column=1, padx=5, pady=5)

submit_button = tk.Button(app, text="Submit", command=submit_data)
submit_button.grid(row=5, columnspan=2)

data_tree = tk.ttk.Treeview(app, columns=("Nama Pasien", "Umur Pasien", "Email", "No. Tlp", "Keluhan", "Patient ID"), show="headings")
data_tree.heading("Nama Pasien", text="Nama Pasien")
data_tree.heading("Umur Pasien", text="Umur Pasien")
data_tree.heading("Email", text="Email")
data_tree.heading("No. Tlp", text="No. Tlp")
data_tree.heading("Keluhan", text="Keluhan")
data_tree.heading("Patient ID", text="Patient ID")
data_tree.grid(row=0, column=2, rowspan=5, padx=10)

delete_button = tk.Button(app, text="Hapus", command=delete_data)
delete_button.grid(row=5, column=2, sticky="w")

app.mainloop()
