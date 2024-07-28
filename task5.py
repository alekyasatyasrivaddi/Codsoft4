import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
     
        self.contacts = []

        self.bg_color = '#f0f0f0'  
        self.btn_color = '#4CAF50'  
        self.text_color = '#000000'  

        
        self.root.configure(bg=self.bg_color)

        
        self.large_font = ('Arial', 14)

       
        self.create_contact_form()

      
        self.create_contact_list()

    def create_contact_form(self):
        self.label_name = tk.Label(self.root, text="Name:", font=self.large_font, bg=self.bg_color, fg=self.text_color)
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(self.root, font=self.large_font, width=30)
        self.entry_name.pack(pady=5)

        self.label_phone = tk.Label(self.root, text="Phone Number:", font=self.large_font, bg=self.bg_color, fg=self.text_color)
        self.label_phone.pack(pady=5)
        self.entry_phone = tk.Entry(self.root, font=self.large_font, width=30)
        self.entry_phone.pack(pady=5)

        self.label_email = tk.Label(self.root, text="Email:", font=self.large_font, bg=self.bg_color, fg=self.text_color)
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.root, font=self.large_font, width=30)
        self.entry_email.pack(pady=5)

        self.label_address = tk.Label(self.root, text="Address:", font=self.large_font, bg=self.bg_color, fg=self.text_color)
        self.label_address.pack(pady=5)
        self.entry_address = tk.Entry(self.root, font=self.large_font, width=30)
        self.entry_address.pack(pady=5)

        self.button_add = tk.Button(self.root, text="Add Contact", command=self.add_contact, font=self.large_font, width=20, bg=self.btn_color, fg='white')
        self.button_add.pack(pady=10)

        self.button_update = tk.Button(self.root, text="Update Contact", command=self.update_contact, font=self.large_font, width=20, bg=self.btn_color, fg='white')
        self.button_update.pack(pady=10)

        self.button_delete = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, font=self.large_font, width=20, bg=self.btn_color, fg='white')
        self.button_delete.pack(pady=10)

        self.button_search = tk.Button(self.root, text="Search Contact", command=self.search_contact, font=self.large_font, width=20, bg=self.btn_color, fg='white')
        self.button_search.pack(pady=10)

        self.button_view_all = tk.Button(self.root, text="View All Contacts", command=self.view_contacts, font=self.large_font, width=20, bg=self.btn_color, fg='white')
        self.button_view_all.pack(pady=10)

    def create_contact_list(self):
        self.label_contact_list = tk.Label(self.root, text="Contact List:", font=self.large_font, bg=self.bg_color, fg=self.text_color)
        self.label_contact_list.pack(pady=5)

        self.listbox_contacts = tk.Listbox(self.root, font=self.large_font, width=50, height=10)
        self.listbox_contacts.pack(pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone and email and address:
            self.contacts.append(Contact(name, phone, email, address))
            self.view_contacts()
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "All fields are required to add a contact.")

    def view_contacts(self):
        self.listbox_contacts.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox_contacts.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
            if results:
                self.listbox_contacts.delete(0, tk.END)
                for contact in results:
                    self.listbox_contacts.insert(tk.END, f"{contact.name} - {contact.phone}")
            else:
                messagebox.showinfo("No Results", "No contacts found with that search term.")

    def update_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            contact.name = self.entry_name.get()
            contact.phone = self.entry_phone.get()
            contact.email = self.entry_email.get()
            contact.address = self.entry_address.get()
            self.view_contacts()
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
        else:
            messagebox.showwarning("Selection Error", "No contact selected for update.")

    def delete_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.view_contacts()
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
        else:
            messagebox.showwarning("Selection Error", "No contact selected for deletion.")

root = tk.Tk()
app = ContactManagerApp(root)
root.mainloop()
