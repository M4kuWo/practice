import tkinter as tk

# Create the main application window
class SimpleTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter App")

        # Counter variable
        self.counter = 0

        # Create and place a label to display the counter
        self.label = tk.Label(root, text=f"Counter: {self.counter}", font=("Arial", 24))
        self.label.pack(pady=20)

        # Create and place a button to increment the counter
        self.button = tk.Button(root, text="Increment", font=("Arial", 20), command=self.increment_counter)
        self.button.pack(pady=10)

    # Function to increment the counter and update the label
    def increment_counter(self):
        self.counter += 1
        self.label.config(text=f"Counter: {self.counter}")

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTkinterApp(root)
    root.geometry("300x200")  # Set window size
    root.mainloop()
