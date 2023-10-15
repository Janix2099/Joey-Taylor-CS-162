"""
File: project1.py
Author: Joey Taylor
Date: 10/1/2023
Overview: 
Creating a class with various methods and variables that uses basic user input to display basic information


    Show me that you can design a Python class for a complex object (car, house, computer, being, container structure) by making me a drawing, list,
    or other document showing or describing your design for your object that shows:

        a few components (for a car it would be something like an interior, a transmission, a chassis, and a motor)

        a few attributes for each component (variables),

        a few behaviors for each component (methods),

        and the relationship between the components, attributes, and behaviors (perhaps with lines showing how a value would get used or calculated)

    a simple program with a menu (user input and output, text in a console is perfectly acceptable) to interact with one of the components that you came up with that:

        Instantiates an object from a class that you write that has attributes and behaviors reflecting your design,

        gets basic input from a user that fills in the attributes of your object,

        displays basic info about your object and its behaviors,

        A menu item that allows the user to quit the program; saying goodbye when selected,

        Note: Be sure to use a loop to get back to the menu after finishing an item (other than quitting) to ask the user what to do next."""
# Import module 
import tkinter as tk

class Submarine:
    """Represents a Submarine
    
    Parts of submarine: oxygen tank, hull depth, fuel, type
    Actions of submarine: Emerge, submerged, motion, weapons(?), sonar 
    Attribute of components: Type = Civilian, military | Fuel = percent full / volume | Oxygen = percent full / volume | hull = dive depth
    
    Example of relationship:
submerge: lose fuel, lose oxygen, lower depth, weapons locked
emerge: lose fuel, gain oxygen, raise depth, weapons unlocked
move: lose fuel. if submerged, lose oxygen. if emerged, gain oxygen
weapon: "weapon fired!", weapons locked, dependent on type of submarine.
sonar: "ping!"
    """
    def __init__(self, sub_type: str):
        self.depth = 0
        self.fuel = 100
        self.oxygen = 100
        self.sub_type = sub_type

    def __handle_fuel(self, distance):
        if distance <= 0:
            print("distance must be a greater than 0")
            return
        if self.fuel == 0:
            print("you're out of fuel")
            return
        if distance > self.fuel:
            print(f"you do not have enough fuel to move that far. you have {self.fuel} km of fuel")
            return
        self.fuel = (self.fuel - distance)

    def __handle_oxygen(self, distance):
        if self.oxygen == 0:
            print("Not enough resources to emerge, you have drowned.")
            return
        if self.depth > 0:
            self.oxygen = max(self.oxygen - distance/2, 0)
        else:
            self.oxygen = min(self.oxygen + distance*2, 100)
            
    def motion(self):
        movement = float(input("How many kilometers do you want to move? (Fuel will last 100 km): " ))
        self.__handle_fuel(movement)
        self.__handle_oxygen(movement)
    
    def sonar(self):
        print("Ping!")
        
    def submerge(self):
        new_depth = float(input("How many kilometers do you want to submerge? (Down to 10km): "))
        if new_depth > 10:
            print("Too deep! max 10km")
            return
        if new_depth < 0:
            print("Invalid submerge value, must be >= 0")
        self.__handle_fuel(new_depth)
        self.__handle_oxygen(new_depth)
        self.depth = self.depth + new_depth

    def emerge(self):
        new_depth = float(input("How many kilometers do you want to emerge? (Up to surface): "))
        if new_depth > self.depth:
            print("Too high! We can't fly!")
            return
        if new_depth < 0:
            print("Invalid emerge value, must be >= 0")
        self.__handle_fuel(new_depth)
        self.__handle_oxygen(new_depth)
        self.depth = self.depth - new_depth

    def weapon(self):
        if self.sub_type == "MILITARY":
            if self.depth == 0:
                print('Pew!') 
            else:
                print('You cannot fire your weapons underwater.')
        else:
            print('You have no weapons, silly civilian.')
        
    def display(self):
            print(f"Your fuel is {self.fuel}% after movement.")
            print(f"Your oxygen is at {self.oxygen}% after movement.")
            print(f"Your depth is at {self.depth} kilometers after movement.")


def main():
    # Create object
    root = tk.Tk()

    # Adjust size
    root.minsize(800, 600)

    # Create Label
    title = tk.Label(root, text="Submarine Types:")
    title.pack()

    # Function to set the submarine type
    def set_sub_type(sub_type):
        submarine.sub_type = sub_type

    # Create buttons for selecting submarine type
    military_button = tk.Button(root, text="Military", command=lambda: set_sub_type("MILITARY"))
    military_button.pack()

    civilian_button = tk.Button(root, text="Civilian", command=lambda: set_sub_type("CIVILIAN"))
    civilian_button.pack()

    # Initialize the Submarine object with the selected sub_type
    submarine = Submarine(sub_type=1)

    # Create Label
    label = tk.Label(root, text="Submarine Options:")
    label.pack()

    # Add labels to display information
    fuel_label = tk.Label(root, text="Fuel: 100%")
    fuel_label.pack()

    oxygen_label = tk.Label(root, text="Oxygen: 100%")
    oxygen_label.pack()

    depth_label = tk.Label(root, text="Depth: 0 km")
    depth_label.pack()

    # Add buttons for actions
    move_button = tk.Button(root, text="Move", command=lambda: submarine.motion() + update_labels())
    move_button.pack()

    submerge_button = tk.Button(root, text="Submerge", command=lambda: submarine.submerge() + update_labels())
    submerge_button.pack()

    emerge_button = tk.Button(root, text="Emerge", command=lambda: submarine.emerge() + update_labels())
    emerge_button.pack()

    weapon_button = tk.Button(root, text="Weapon", command=submarine.weapon)
    weapon_button.pack()

    sonar_button = tk.Button(root, text="Sonar", command=submarine.sonar)
    sonar_button.pack()

    # Function to update the information labels
    def update_labels():
        fuel_label.config(text=f"Fuel: {submarine.fuel}%")
        oxygen_label.config(text=f"Oxygen: {submarine.oxygen}%")
        depth_label.config(text=f"Depth: {submarine.depth} km")

    # Function to start the tkinter event loop
    root.mainloop()

# Call the main function to start the program
if __name__ == "__main__":
    main()