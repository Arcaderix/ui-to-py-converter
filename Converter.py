import tkinter as tk
from tkinter import ttk, filedialog
import subprocess

class UIConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UI to PY File Converter")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Select a .ui file")
        self.label.pack(pady=10)

        self.open_button = tk.Button(root, text="Open File", command=self.open_file)
        self.open_button.pack(pady=5)

        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        self.convert_button = tk.Button(root, text="Convert", state="disabled", command=self.convert_file)
        self.convert_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save", state="disabled", command=self.save_file)
        self.save_button.pack(pady=5)

        self.file_path = None
        self.save_path = None

        self.log_text = tk.Text(root, height=6, width=50)
        self.log_text.pack(pady=10)
        self.log_text.config(state=tk.DISABLED)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("UI Files", "*.ui")])
        if self.file_path:
            self.file_label.config(text=f"Selected file: {self.file_path}")
            self.convert_button.config(state="normal")
            self.log_message(f"Selected file: {self.file_path}")

    def convert_file(self):
        if not self.file_path:
            return

        self.progress.config(value=0)
        self.progress.start(10)

        self.log_message("Starting conversion...")

        try:
            output_file = self.file_path.replace(".ui", ".py")
            subprocess.run(["pyuic5", self.file_path, "-o", output_file], check=True)
            
            self.progress.stop()
            self.progress.config(value=100)
            
            self.log_message(f"Conversion completed: {output_file}")

            self.save_button.config(state="normal")
            self.save_path = output_file
        except subprocess.CalledProcessError:
            self.log_message("Error converting the file.")
            self.progress.stop()

    def save_file(self):
        if not self.save_path:
            return

        save_location = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if save_location:
            try:
                with open(self.save_path, "r") as f:
                    content = f.read()
                with open(save_location, "w") as f:
                    f.write(content)

                self.log_message(f"File saved as {save_location}")
            except Exception as e:
                self.log_message(f"Error saving the file: {str(e)}")

    def log_message(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.config(state=tk.DISABLED)
        self.log_text.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = UIConverterApp(root)
    root.mainloop()
