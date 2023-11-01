"""File: project5.py
Author: Joey Taylor
Date: 10/31/2023
Overview: 
Creating a 100 integer GUI that displays the search process. The assignment suggested using shapes, 
but since the in-class work already did that I decided to try colored text boxes"""

import random
import tkinter as tk

class GuiSearch:
    def update_label_text(self, new_text):
        self.label_string_var.set(new_text)

    def search(self, proposed_number=None):
        if proposed_number is None:
            proposed_number = int(self.input_text.get())

        self.proposed_number = proposed_number  # Store the proposed number

        # Initialize the index to zero
        self.search_index = 0
        self.found_count = 0  # Initialize the count of found values

        # Start the search with a 250 ms delay
        self.root.after(250, self.check_and_mark_non_matching)

    def check_and_mark_non_matching(self):
        if self.search_index < 100:
            self.mark_as_searching(self.search_index)  # Highlight the value as yellow
            
            # Schedule a check with a 100 ms delay to mark as not found or found
            self.root.after(100, self.check_value)

        else:
            # Search is completed, update the found count label
            self.found_count_label.config(text=f"Found: {self.found_count}")

    def check_value(self):
        if self.values[self.search_index] != self.proposed_number:
            self.mark_as_not_found(self.search_index)
        else:
            self.mark_as_found(self.search_index)  # Mark matching value as light green
            self.found_count += 1  # Increment the count of found values
        
        # Increment the index and schedule the next check with a 100 ms interval
        self.search_index += 1
        self.root.after(100, self.check_and_mark_non_matching)

    def mark_as_searching(self, index):
        # Marks values being searched as yellow
        self.text_box.tag_add("searching", f"{index+1}.0", f"{index+1}.end")
        self.text_box.tag_config("searching", background="yellow")

    def mark_as_found(self, index):
        # Marks matches as light green
        self.text_box.tag_add("found", f"{index+1}.0", f"{index+1}.end")
        self.text_box.tag_config("found", background="light green")

    def mark_as_not_found(self, index):
        # Marks non-matches as red
        self.text_box.tag_add("not_found", f"{index+1}.0", f"{index+1}.end")
        self.text_box.tag_config("not_found", background="red")

    def update_text_box(self, values):
        # Inserts values into the GUI
        self.text_box.delete(1.0, "end")
        for value in values:
            self.text_box.insert("end", f"{value}\n")

    def generate_random_values(self):
        # Creates 100 random values between 1-100
        return [random.randint(1, 100) for _ in range(100)]

    def __init__(self):
        # Initialize GUI
        self.root = tk.Tk()
        self.root.title("Search GUI (1-100)")
        self.label_string_var = tk.StringVar(self.root, "Enter a number to search for:")
        self.label = tk.Label(self.root, textvariable=self.label_string_var)
        self.label.grid(column=0, row=0)
        self.input_text = tk.Entry(self.root, width=10)
        self.input_text.grid(column=1, row=0)
        self.search_button = tk.Button(self.root, text="Search", command=self.search)
        self.search_button.grid(column=2, row=0)
        self.text_box = tk.Text(self.root, width=40, height=20)
        self.text_box.grid(column=0, row=1, columnspan=3)
        self.values = self.generate_random_values()
        self.update_text_box(self.values)
        
        # Label to display the count of found values
        self.found_count_label = tk.Label(self.root, text="")
        self.found_count_label.grid(column=0, row=2, columnspan=3)

    def mainloop(self):
        self.root.mainloop()

if __name__ == '__main__':
    gui = GuiSearch()
    gui.mainloop()
