import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.root, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.button_view = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.button_search = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.button_search.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.button_update = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.button_update.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.button_delete = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

    def add_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def search_contact(self):
        name = self.entry_name.get().strip()
        if name in self.contacts:
            messagebox.showinfo("Contact", f"{name}: {self.contacts[name]}")
        else:
            messagebox.showinfo("Contact", "Contact not found.")

    def update_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        if name in self.contacts:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact updated successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.entry_name.get().strip()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
