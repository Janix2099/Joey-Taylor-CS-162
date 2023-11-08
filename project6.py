"""File: project6.py
Author: Joey Taylor
Date: 11/6/2023
Overview: 
A GUI program that visualizes the insertion sort algorithm using colored text boxes.
This code generates a list of 100 random numbers and allows the user to visually 
follow the sorting process step-by-step, highlighting comparisons, swaps, and the 
current position being sorted."""

import random
import tkinter as tk

class GuiSort:
    def __init__(self):
        """ Initialize the GUI elements and create the list of random values """
        self.root = tk.Tk()
        self.root.title("Insertion Sort Visualization")
        self.sort_button = tk.Button(self.root, text="Sort", command=self.start_sort)
        self.sort_button.grid(column=0, row=0)
        self.text_box = tk.Text(self.root, width=50, height=25)
        self.text_box.grid(column=0, row=1, columnspan=3)
        self.values = self.generate_random_values()
        self.update_text_box(self.values)

    def generate_random_values(self):
        """ Create a list of 100 random values between 1 and 100 """
        return [random.randint(1, 100) for _ in range(100)]

    def update_text_box(self, values):
        """ Update the text box with the current state of the values list """
        self.text_box.delete(1.0, "end")
        for value in values:
            self.text_box.insert("end", f"{value}\n")

    def start_sort(self):
        """ Initiate the sorting process """
        self.sort_button.config(state=tk.DISABLED)  # Disable the sort button during sorting
        self.insertion_sort(1)

    def insertion_sort(self, i):
        """ Perform the insertion sort algorithm """
        if i < len(self.values):
            key = self.values[i]  # The current value to be sorted
            self.mark_as_selected(i)
            self.root.after(100, self.compare_elements, key, i, i - 1)
        else:
            self.mark_all_sorted()  # Mark the entire list as sorted
            self.sort_button.config(state=tk.NORMAL)  # Re-enable the sort button

    def compare_elements(self, key, i, j):
        """ Compare elements during the sort, highlight the elements being compared """
        if j >= 0:
            self.mark_as_comparing(j, j + 1)
            self.root.after(50, self.check_for_swap, key, i, j)
        else:
            self.root.after(50, self.place_key, key, i, j)

    def check_for_swap(self, key, i, j):
        """ Check whether a swap needs to occur """
        if self.values[j] > key:
            self.mark_as_swapping(j, j + 1)
            self.root.after(50, self.swap_elements, key, i, j)
        else:
            self.root.after(50, self.place_key, key, i, j)

    def swap_elements(self, key, i, j):
        """ Swap the elements if necessary """
        self.values[j + 1] = self.values[j]  # Perform the swap
        self.update_text_box(self.values)  # Update the GUI
        self.root.after(50, self.compare_elements, key, i, j - 1)

    def place_key(self, key, i, j):
        """ Place the key in its correct position """
        self.values[j + 1] = key
        self.update_text_box(self.values)  # Update the GUI
        self.insertion_sort(i + 1)  # Continue sorting the next key

    def mark_as_comparing(self, index1, index2):
        """ Visually mark elements being compared """
        self.mark_as_default()
        self.text_box.tag_add("comparing", f"{index1+1}.0", f"{index1+1}.end")
        self.text_box.tag_add("comparing", f"{index2+1}.0", f"{index2+1}.end")
        self.text_box.tag_config("comparing", background="blue")

    def mark_as_swapping(self, index1, index2):
        """ Visually mark elements that are being swapped """
        self.mark_as_default()
        self.text_box.tag_add("swapping", f"{index1+1}.0", f"{index1+1}.end")
        self.text_box.tag_add("swapping", f"{index2+1}.0", f"{index2+1}.end")
        self.text_box.tag_config("swapping", background="purple")

    def mark_as_selected(self, index):
        """ Highlight the current position being sorted """
        self.mark_as_default()
        self.text_box.tag_add("selected", f"{index+1}.0", f"{index+1}.end")
        self.text_box.tag_config("selected", background="orange")

    def mark_all_sorted(self):
        """ Highlight the entire list to indicate sorting is complete """
        self.text_box.tag_add("sorted", "1.0", "end")
        self.text_box.tag_config("sorted", background="light green")

    def mark_as_default(self):
        """ Clear all previous highlights """
        self.text_box.tag_remove("comparing", "1.0", "end")
        self.text_box.tag_remove("swapping", "1.0", "end")
        self.text_box.tag_remove("selected", "1.0", "end")
        self.text_box.tag_remove("sorted", "1.0", "end")

    def mainloop(self):
        """ Start the main loop of the GUI """
        self.root.mainloop()

if __name__ == '__main__':
    gui = GuiSort()
    gui.mainloop()