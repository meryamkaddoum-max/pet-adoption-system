import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "http://localhost:8000"

def safe_get(obj, *keys):
    for key in keys:
        if key in obj:
            return obj[key]
    return "-"

# ======================
# MAIN WINDOW
# ======================
root = tk.Tk()
root.title("Pet Adoption Management System")
root.geometry("1000x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ======================
# PETS TAB
# ======================
frame_pets = ttk.Frame(notebook)
notebook.add(frame_pets, text="Pets")

cols = ("ID", "Name", "Species", "Breed", "Age", "Gender", "Status")
tree_pets = ttk.Treeview(frame_pets, columns=cols, show="headings")

for col in cols:
    tree_pets.heading(col, text=col)
    tree_pets.column(col, width=120)

tree_pets.pack(fill="both", expand=True, pady=10)

form_pets = tk.Frame(frame_pets)
form_pets.pack()

entry_name = tk.Entry(form_pets)
entry_species = tk.Entry(form_pets)
entry_breed = tk.Entry(form_pets)
entry_age = tk.Entry(form_pets)
entry_gender = tk.Entry(form_pets)
entry_status = tk.Entry(form_pets)

labels = [
    ("Name (z.B. Max)", entry_name),
    ("Species (z.B. Dog)", entry_species),
    ("Breed (z.B. Labrador)", entry_breed),
    ("Age (z.B. 2)", entry_age),
    ("Gender (Male/Female)", entry_gender),
    ("Status (available/adopted)", entry_status),
]

for i, (text, entry) in enumerate(labels):
    tk.Label(form_pets, text=text).grid(row=0, column=i)
    entry.grid(row=1, column=i)

def load_pets():
    tree_pets.delete(*tree_pets.get_children())

    try:
        res = requests.get(f"{API_URL}/pets")
        data = res.json()

        if not data:
            tree_pets.insert("", "end", values=("Keine Pets vorhanden", "", "", "", "", "", ""))
            return

        for p in data:
            tree_pets.insert("", "end", values=(
                safe_get(p, "id", "pet_id"),
                safe_get(p, "name", "pet_name"),
                safe_get(p, "species", "pet_species"),
                safe_get(p, "breed", "pet_breed"),
                safe_get(p, "age", "pet_age"),
                safe_get(p, "gender", "pet_gender"),
                p.get("status", "-")   # ✅ FIX
            ))

    except Exception as e:
        messagebox.showerror("Error", str(e))


def add_pet():
    try:
        data = {
            "name": entry_name.get(),
            "species": entry_species.get(),
            "breed": entry_breed.get(),
            "age": int(entry_age.get()),
            "gender": entry_gender.get(),
            "status": entry_status.get()   # ✅ FIX
        }

        requests.post(f"{API_URL}/pets", json=data)
        load_pets()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_pet():
    selected = tree_pets.selection()
    if not selected:
        return

    item = tree_pets.item(selected[0])
    pet_id = item["values"][0]

    try:
        requests.delete(f"{API_URL}/pets/{pet_id}")
        load_pets()
    except Exception as e:
        messagebox.showerror("Error", str(e))


btn_frame = tk.Frame(frame_pets)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Load", command=load_pets).pack(side="left", padx=5)
tk.Button(btn_frame, text="Add", command=add_pet).pack(side="left", padx=5)
tk.Button(btn_frame, text="Delete", command=delete_pet).pack(side="left", padx=5)


# ======================
# ADOPTERS TAB
# ======================
frame_adopters = ttk.Frame(notebook)
notebook.add(frame_adopters, text="Adopters")

cols2 = ("ID", "Name", "Email", "Phone")
tree_adopters = ttk.Treeview(frame_adopters, columns=cols2, show="headings")

for col in cols2:
    tree_adopters.heading(col, text=col)
    tree_adopters.column(col, width=150)

tree_adopters.pack(fill="both", expand=True, pady=10)

form_adopters = tk.Frame(frame_adopters)
form_adopters.pack()

entry_fn = tk.Entry(form_adopters)
entry_ln = tk.Entry(form_adopters)
entry_email = tk.Entry(form_adopters)
entry_phone = tk.Entry(form_adopters)

labels2 = [
    ("First Name", entry_fn),
    ("Last Name", entry_ln),
    ("Email", entry_email),
    ("Phone", entry_phone),
]

for i, (text, entry) in enumerate(labels2):
    tk.Label(form_adopters, text=text).grid(row=0, column=i)
    entry.grid(row=1, column=i)


def load_adopters():
    tree_adopters.delete(*tree_adopters.get_children())

    res = requests.get(f"{API_URL}/adopters")
    data = res.json()

    if not data:
        tree_adopters.insert("", "end", values=("Keine Adopters", "", "", ""))
        return

    for a in data:
        tree_adopters.insert("", "end", values=(
            a.get("id"),
            f"{a.get('first_name','')} {a.get('last_name','')}",
            a.get("email", "-"),
            a.get("phone", "-")
        ))


def delete_adopter():
    selected = tree_adopters.selection()
    if not selected:
        return

    item = tree_adopters.item(selected[0])
    adopter_id = item["values"][0]

    requests.delete(f"{API_URL}/adopters/{adopter_id}")
    load_adopters()


def add_adopter():
    data = {
        "first_name": entry_fn.get(),
        "last_name": entry_ln.get(),
        "email": entry_email.get(),
        "phone": entry_phone.get()
    }

    try:
        requests.post(f"{API_URL}/adopters", json=data)
        load_adopters()
    except Exception as e:
        messagebox.showerror("Error", str(e))


btn_frame2 = tk.Frame(frame_adopters)
btn_frame2.pack(pady=10)

tk.Button(btn_frame2, text="Load", command=load_adopters).pack(side="left", padx=5)
tk.Button(btn_frame2, text="Add", command=add_adopter).pack(side="left", padx=5)

btn_delete_adopter = ttk.Button(frame_adopters, text="Delete", command=delete_adopter)
btn_delete_adopter.pack()


# ======================
# ADOPTIONS TAB
# ======================
frame_adoptions = ttk.Frame(notebook)
notebook.add(frame_adoptions, text="Adoptions")

cols3 = ("ID", "Adopter ID", "Pet ID", "Date", "Status")
tree_adoptions = ttk.Treeview(frame_adoptions, columns=cols3, show="headings")

for col in cols3:
    tree_adoptions.heading(col, text=col)
    tree_adoptions.column(col, width=150)

tree_adoptions.pack(fill="both", expand=True, pady=10)

form_adopt = tk.Frame(frame_adoptions)
form_adopt.pack()

entry_adopter_id = tk.Entry(form_adopt)
entry_pet_id = tk.Entry(form_adopt)
entry_date = tk.Entry(form_adopt)
entry_status2 = tk.Entry(form_adopt)

labels3 = [
    ("Adopter ID", entry_adopter_id),
    ("Pet ID", entry_pet_id),
    ("Date YYYY-MM-DD", entry_date),
    ("Status", entry_status2),
]

for i, (text, entry) in enumerate(labels3):
    tk.Label(form_adopt, text=text).grid(row=0, column=i)
    entry.grid(row=1, column=i)


def load_adoptions():
    tree_adoptions.delete(*tree_adoptions.get_children())

    res = requests.get(f"{API_URL}/adoptions")
    data = res.json()

    if not data:
        tree_adoptions.insert("", "end", values=("Keine Adoptions", "", "", "", ""))
        return

    for a in data:
        tree_adoptions.insert("", "end", values=(
            a.get("id"),
            a.get("adopter_id"),
            a.get("pet_id"),
            safe_get(a, "date", "adoption_date", "created_at"),
            a.get("status", "-")
        ))


def add_adoption():
    data = {
        "adopter_id": int(entry_adopter_id.get()),
        "pet_id": int(entry_pet_id.get()),
        "adoption_date": entry_date.get(),
        "status": entry_status2.get()   # ✅ FIX
    }

    r = requests.post(f"{API_URL}/adoptions", json=data)

    if r.status_code in (200, 201):
        load_adoptions()
    else:
        messagebox.showerror("Error", r.text)


def delete_adoption():
    selected = tree_adoptions.selection()
    if not selected:
        return

    item = tree_adoptions.item(selected[0])
    adoption_id = item["values"][0]

    requests.delete(f"{API_URL}/adoptions/{adoption_id}")
    load_adoptions()


btn_frame3 = tk.Frame(frame_adoptions)
btn_frame3.pack(pady=10)

tk.Button(btn_frame3, text="Load", command=load_adoptions).pack(side="left", padx=5)
tk.Button(btn_frame3, text="Add", command=add_adoption).pack(side="left", padx=5)

btn_delete_adoption = ttk.Button(frame_adoptions, text="Delete", command=delete_adoption)
btn_delete_adoption.pack()


# ======================
# START
# ======================
root.mainloop()