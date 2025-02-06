import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root):
        self.root = root
        root.title("Message Box")
        
        # Create main frame
        mainframe = ttk.Frame(root, padding="10")
        mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Entry with label
        self.name_var = tk.StringVar()
        ttk.Label(mainframe, text="Name:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(mainframe, textvariable=self.name_var).grid(row=0, column=1, padx=5, pady=5)
        
        # Dropdown menu
        self.choice_var = tk.StringVar()
        choices = ["Messi", "Ronaldo", "Other"]
        ttk.Label(mainframe, text="Choose:").grid(row=1, column=0, sticky=tk.W)
        ttk.Combobox(mainframe, textvariable=self.choice_var, values=choices).grid(row=1, column=1, padx=5, pady=5)
        
        # Checkbutton
        self.check_var = tk.BooleanVar()
        ttk.Checkbutton(mainframe, text="Agree", variable=self.check_var).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Button
        ttk.Button(mainframe, text="Submit", command=self.submit).grid(row=3, column=0, columnspan=2, pady=10)

    def submit(self):
        message = f"Name: {self.name_var.get()}\n"
        message += f"Choice: {self.choice_var.get()}\n"
        message += f"Feature enabled: {self.check_var.get()}"
        messagebox.showinfo("Submission", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()