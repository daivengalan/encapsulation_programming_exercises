import tkinter as tk
from tkinter import messagebox
from pet_class import Pet

class PetApp:
    def __init__(self, root):
        self.root = root
        root.title("Veterinary Clinic Registration")
        root.geometry("400x420")
        root.resizable(False, False)

        tk.Label(root, text="Veterinary Clinic",
                 font=("Arial", 15, "bold")).pack(pady=(20, 2))
        tk.Label(root, text="Pet Registration System",
                 font=("Arial", 10), fg="#555").pack(pady=(0, 16))

        form = tk.Frame(root)
        form.pack(padx=30, fill="x")

        tk.Label(form, text="Pet Name:", font=("Arial", 10)).grid(
            row=0, column=0, sticky="w", pady=6)
        self.name_entry = tk.Entry(form, width=24, font=("Arial", 10))
        self.name_entry.grid(row=0, column=1, pady=6)

        tk.Label(form, text="Species:", font=("Arial", 10)).grid(
            row=1, column=0, sticky="w", pady=6)
        self.type_entry = tk.Entry(form, width=24, font=("Arial", 10))
        self.type_entry.grid(row=1, column=1, pady=6)

        tk.Label(form, text="Age (years):", font=("Arial", 10)).grid(
            row=2, column=0, sticky="w", pady=6)
        self.age_entry = tk.Entry(form, width=24, font=("Arial", 10))
        self.age_entry.grid(row=2, column=1, pady=6)

        tk.Button(root, text="Register Pet", width=16, height=2,
                  bg="#D71920", fg="white", font=("Arial", 10, "bold"),
                  command=self.register).pack(pady=(14, 10))

        self.result = tk.Label(root, text="", font=("Courier", 9),
                               justify="left", bg="#f5f5f5", relief="sunken",
                               width=38, anchor="w", padx=8, pady=6)
        self.result.pack(padx=30, pady=(0, 10))

        tk.Button(root, text="Reset", width=10,
                  command=self.reset).pack()

    def register(self):
        name = self.name_entry.get().strip()
        animal_type = self.type_entry.get().strip()
        age_str = self.age_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Please enter the pet's name.")
            return
        if not animal_type:
            messagebox.showerror("Error", "Please enter the species.")
            return
        try:
            age = int(age_str)
            if age < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Age must be a non-negative whole number.")
            return

        pet = Pet()
        pet.set_name(name)
        pet.set_animal_type(animal_type)
        pet.set_age(age)

        self.result.config(text=(
            f" Registered Name : {pet.get_name()}\n"
            f" Species         : {pet.get_animal_type()}\n"
            f" Age             : {pet.get_age()} years old"
        ))

    def reset(self):
        self.name_entry.delete(0, "end")
        self.type_entry.delete(0, "end")
        self.age_entry.delete(0, "end")
        self.result.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = PetApp(root)
    root.mainloop()