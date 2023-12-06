import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pygame
import pickle
import os
from tkinter import simpledialog
from event import Events
import random

# Initialize Pygame Mixer for sound effects
pygame.mixer.init()
narrator_sound = pygame.mixer.Sound('sfx-blipfemale.wav')  # Ensure the path to your sound file is correct
blip_sound = pygame.mixer.Sound('sfx-blipmale.wav')

FINANCE_GOAL = 3000
DAYS_IN_MONTH = 31

# Player class to store player attributes and methods
class Player:
    def __init__(self, happiness=50, finances=100, skills=1, promotion=1, current_day="Sunday", day_count=1, sleep_timer=3):
        # Initialize player attributes
        self.happiness = happiness
        self.finances = finances
        self.skills = skills
        self.promotion = promotion
        self.current_day = current_day
        self.day_count = day_count
        self.sleep_timer = sleep_timer

    # Check if financial goal is met
    def check_goal(self):
        return self.finances >= FINANCE_GOAL

    # Update player status based on actions
    def update_status(self, happiness_change, finances_change, hours=0, working=False):
        self.happiness = min(100, max(0, self.happiness + happiness_change))
        if working:
            self.finances += finances_change * hours * self.promotion
        else:
            self.finances += finances_change

    # Check and apply promotion based on work done.
    def check_promotion(self):
        # Base challenge level for promotion
        base_challenge = 40  # Expected skill points for a promotion (5 days * 8 hours)

        # Introduce randomness: Challenge varies between 70% and 130% of the base challenge
        daily_challenge = random.randint(int(base_challenge * 0.7), int(base_challenge * 1.3))

        # Compare skills with the daily challenge
        if self.skills >= daily_challenge:
            self.promotion += 0.25
            self.skills = 1  # Reset skills after promotion
            return True  # Promotion earned
        return False  # No promotion.


# Game class
class Game:
    def __init__(self, root):
        # Initialize the game with tkinter root
        self.root = root
        self.root.title("Life of .Py")
        self.player = Player()
        self.events = Events(self)
        self.current_day = "Sunday"
        self.current_time = "11 PM"
        self.last_relax_day = None
        self.create_start_menu()
        self.day_count = 1
        self.has_studied_today = False
        self.text_queue = []
        self.is_text_displaying = False

    def create_start_menu(self):
        # Create start menu frame
        start_menu_frame = tk.Frame(self.root)
        start_menu_frame.pack(pady=10)

        # Graphic (Placeholder for now)
        tk.Label(start_menu_frame, text="The Life of .Py", font=("Helvetica", 24)).pack(pady=10)

        # Start Menu Buttons
        tk.Button(start_menu_frame, text="New Game", command=self.start_new_game).pack(pady=5)
        tk.Button(start_menu_frame, text="Load Game", command=self.load_game).pack(pady=5)
        tk.Button(start_menu_frame, text="Exit Game", command=self.root.quit).pack(pady=5)

    def start_new_game(self):
        # Clear the start menu and setup game UI
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_ui()

        # Fetch and display a random introduction
        introduction = self.events.get_random_introduction()
        self.add_text_with_sound(introduction['text'], narrator_mode=True)

    def setup_ui(self):
        # Create a textbox for game output
        self.text_box = tk.Text(self.root, height=10, width=70, font=("Helvetica", 12), spacing3=5)
        self.text_box.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
        self.text_box.insert(tk.END, "Welcome to the Life of .Py\n\n")
        self.text_box.config(state=tk.DISABLED)

        # Call the method to setup progress bars
        self.setup_progress_bars()
        
        #Call the method to setup clock
        self.setup_calendar_clock()
    
        self.countdown_label = tk.Label(self.root, text="Days left: 30")
        self.countdown_label.grid(row=7, column=0, padx=10, pady=10)

        # Create frame for gameplay buttons
        gameplay_frame = tk.LabelFrame(self.root, text="Gameplay", bd=2, relief=tk.GROOVE)
        gameplay_frame.grid(row=4, column=0, columnspan=3, pady=5)

        # Gameplay buttons# In the setup_ui method# In the setup_ui method
        tk.Button(gameplay_frame, text="Work", command=lambda: self.action_dialog('work'), height=2, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(gameplay_frame, text="Hobbies", command=lambda: self.action_dialog('relax'), height=2, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(gameplay_frame, text="Sleep", command=lambda: self.action_dialog('sleep'), height=2, width=10).pack(side=tk.LEFT, padx=5)
        
        # Create frame for options buttons
        options_frame = tk.LabelFrame(self.root, text="Options", bd=2, relief=tk.GROOVE)
        options_frame.grid(row=5, column=0, columnspan=3, pady=5)

        # Options buttons
        tk.Button(options_frame, text="Save Game", command=self.save_game, width=8).pack(side=tk.LEFT, padx=5)
        tk.Button(options_frame, text="Load Game", command=self.load_game, width=8).pack(side=tk.LEFT, padx=5)
        tk.Button(options_frame, text="Exit Game", command=self.root.quit, width=8).pack(side=tk.LEFT, padx=5)
        self.update_progress_bars()

    def setup_calendar_clock(self):
        # Calendar and Clock setup
        calendar_frame = tk.Frame(self.root)
        calendar_frame.grid(row=6, column=0, padx=10, pady=10)

        self.calendar_label = tk.Label(calendar_frame, text=f"Day: {self.current_day}")
        self.calendar_label.pack()

        self.clock_label = tk.Label(calendar_frame, text=f"Time: {self.current_time}")
        self.clock_label.pack()

        self.sleep_timer_label = tk.Label(self.root, text=f"Sleep Timer: {self.player.sleep_timer} hours")
        self.sleep_timer_label.grid(row=8, column=0, padx=10, pady=10)

        

    def update_calendar_clock(self, hours, from_sleep=False):
        # Simplified logic for updating the time and day
        current_hour = int(self.current_time.split()[0])
        am_pm = self.current_time.split()[1]
        new_hour = (current_hour + hours) % 12
        new_hour = 12 if new_hour == 0 else new_hour

        # Switch AM/PM after 12 hours
        if hours >= 12 or (current_hour + hours) >= 12:
            am_pm = 'PM' if am_pm == 'AM' else 'AM'

        # Update the day after 24 hours
        if am_pm == 'AM' and self.current_time.split()[1] == 'PM':
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            current_day_index = days.index(self.current_day)
            self.current_day = days[(current_day_index + 1) % 7]
        # Check if a new day has started
        if "AM" in self.current_time and "PM" in self.previous_time:
            self.day_count += 1
            self.check_month_end()
            promoted = self.player.check_promotion()
            if promoted:
                self.add_text_with_sound("Look at you, climbing up the corporate ladder.## How delightfully average.", narrator_mode=True)
                self.add_text_with_sound("Your skills earned a promotion. 25 percent pay increase.")

        # Decrement the sleep timer only if not from sleeping
        if not from_sleep:
            self.player.sleep_timer = max(0, self.player.sleep_timer - hours)
            if self.player.sleep_timer <= 0:
                self.handle_pass_out()

        # Update sleep timer label
        self.sleep_timer_label.config(text=f"Sleep Timer: {self.player.sleep_timer} hours")

        days_left = DAYS_IN_MONTH - self.day_count
        self.countdown_label.config(text=f"Days left: {days_left}")

        self.previous_time = self.current_time
        self.current_time = f"{new_hour} {am_pm}"
        self.clock_label.config(text=f"Time: {self.current_time}")
        self.calendar_label.config(text=f"Day: {self.current_day}")

    def handle_pass_out(self):
        # Handle the pass-out scenario
        self.add_text_with_sound("You've passed out due to exhaustion!", narrator_mode=True)
        self.player.happiness = max(0, self.player.happiness - 30)  # Reduce happiness
        self.player.sleep_timer = 24  # Reset pass-out timer
        self.update_calendar_clock(12, from_sleep=True)


    def check_month_end(self):
        if self.day_count > DAYS_IN_MONTH:
            self.end_game_check()

    def end_game_check(self):
        if self.player.check_goal():
            self.add_text_with_sound(f"Congratulations! You've met your finance goal with ${self.player.finances} and happiness level of {self.player.happiness}!")
        else:
            self.add_text_with_sound("Unfortunately, you didn't meet your finance goal this month. Better luck next time!")
        self.game_over()

    def create_progress_bar(self, column, label_text, emoji, player_attribute, style):
        progress_frame = tk.Frame(self.root)
        progress_frame.grid(row=1, column=column, rowspan=3, sticky="n", padx=(10, 0))
        
        label = tk.Label(progress_frame, text=emoji, font=("Helvetica", 12))
        label.grid(row=0, column=0, padx=5, pady=5)
        
        progress_bar = ttk.Progressbar(progress_frame, orient="vertical", length=100, mode='determinate')
        progress_bar.grid(row=1, column=0, padx=5, pady=5)
        progress_bar['value'] = getattr(self.player, player_attribute)
        progress_bar.configure(style=f"{style}.Horizontal.TProgressbar")
        return progress_bar

    def setup_progress_bars(self):
        # Finance Bar
        self.finances_bar = self.create_progress_bar(1, "", "$", "finances", "green")

        # Happiness Bar with Smiley Emoji
        self.happiness_bar = self.create_progress_bar(2, "", "😊", "happiness", "yellow")

        # Set custom styles for progress bars
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("green.Horizontal.TProgressbar", troughcolor='white', background='green')
        s.configure("yellow.Horizontal.TProgressbar", troughcolor='white', background='yellow')

    def add_text_with_sound(self, text, narrator_mode=False):
        # Add text to the queue
        self.text_queue.append((text, narrator_mode))
        # If no text is currently being displayed, start the display process
        if not self.is_text_displaying:
            self.process_text_queue()

    def process_text_queue(self):
        # If there's no text to display, set is_text_displaying to False and return
        if not self.text_queue:
            self.is_text_displaying = False
            return

        self.is_text_displaying = True
        text, narrator_mode = self.text_queue.pop(0)
        text = '\n' + text  # Add new line at the beginning of the text

        # Define tag configurations
        self.text_box.tag_config('narrator', foreground='green')
        self.text_box.tag_config('normal', foreground='black')

        # Set the tag based on narrator mode
        tag = 'narrator' if narrator_mode else 'normal'

        # Create a generator that will yield characters and their respective delays
        def char_generator():
            should_play_sound = True
            for char in text:
                if char == '#':
                    yield (char, 500)  # Longer pause for hash symbol
                    continue
                if char not in ' .,|!-':
                    if should_play_sound:
                        pygame.mixer.Sound.play(narrator_sound if narrator_mode else blip_sound)
                    should_play_sound = not should_play_sound
                yield (char, 30)  # Delay of 30ms or 0.03 seconds

        char_iter = char_generator()

        def insert_next_char():
            try:
                char, delay = next(char_iter)
                if char != '#':
                    self.text_box.config(state=tk.NORMAL)
                    self.text_box.insert(tk.END, char, tag)
                    self.text_box.config(state=tk.DISABLED)
                    self.text_box.see(tk.END)
                self.root.after(delay, insert_next_char)
            except StopIteration:
                # Once a text is fully displayed, process the next text in the queue
                self.process_text_queue()

        insert_next_char()

    def make_decision(self, decision, hours):
        # Handles player's decisions and updates game state accordingly
        message = ""
        if decision == 'work':
            if self.can_work():
                # Update player status based on work
                self.player.update_status(-10 * hours / 8, 15 * self.player.promotion, hours, working=True)
                message = f"You worked for {hours} hours and earned ${15 * hours * self.player.promotion:.2f}."
                self.quiz_challenge(hours)  # Add quiz challenge after work
            else:
                message = "It's the weekend or outside working hours. No work today!"
        elif decision == 'relax':
            cost = 5 * hours
            if self.player.finances >= cost:
                self.player.update_status(16 * hours / 8, -cost)
                message = f"You relaxed for {hours} hours and it cost you ${cost}."
                self.trigger_random_event_if_needed()
            else:
                message = "You don't have enough money to relax for that long."
        elif decision == 'sleep':
            # Handle sleep action
            self.sleep(hours)
            return
        else:
            # Fallback for invalid action
            message = "Invalid action selected."

        # Display the decision's outcome and update the game UI
        self.add_text_with_sound(message)
        self.update_calendar_clock(hours)
        self.update_ui()


    def trigger_random_event_if_needed(self):
        # Checks if a random event should be triggered based on game conditions
        # Random events are triggered if the current day is different from the last relaxation day
        # and there's a 50% chance
        if self.current_day != self.last_relax_day and random.random() < 0.5:
            # Trigger a random event and display its outcome
            outcome_text = self.events.trigger_random_event(self.player)
            self.add_text_with_sound(outcome_text, narrator_mode=True)
            self.last_relax_day = self.current_day
            return True  # Indicate that a random event was triggered
        return False  # No random event was triggered

    def can_work(self):
        # Helper function to parse the current time
        current_hour, am_pm = self.parse_current_time()

        # Convert 12-hour format to 24-hour format for easier comparison
        if am_pm == "PM":
            current_hour += 12 if current_hour != 12 else 0
        elif am_pm == "AM" and current_hour == 12:
            current_hour = 0

        # Check if today is a weekend
        if self.current_day in ["Saturday", "Sunday"]:
            self.add_text_with_sound("It's the weekend. No work today!", narrator_mode=True)
            return False

        # Check if current time is within work hours (9 AM to 9 PM in 24-hour format)
        return 9 <= current_hour < 21
   
    def quiz_challenge(self, hours):
        if hours <= 0:
            return  # Base case: no more hours left

        # Get a quiz question
        question_data = self.events.get_quiz_question()
        formatted_question = f"{question_data['question']}\n" + "\n".join(question_data['options'])
        user_answer = simpledialog.askstring("Quiz", formatted_question)

        if user_answer:
            user_answer = user_answer.strip().upper()
            correct_answer = question_data['answer']
            # Checking if the first letter of the user_answer is the correct option
            if user_answer == correct_answer:
                self.add_text_with_sound("Correct! Skill increased.")
                self.player.skills += 1
            else:
                explanation = question_data['explanation']
                self.add_text_with_sound(f"Incorrect. The correct answer was '{correct_answer}'. {explanation}")
                self.player.update_status(-2.5, 0)  # Apply an unhappiness penalty for an incorrect answer

        # Recursive call for the remaining hours
        self.quiz_challenge(hours - 1)

    def parse_current_time(self):
        # Helper function to parse the current time
        current_hour = int(self.current_time.split()[0])
        am_pm = self.current_time.split()[1]
        if current_hour == 12:
            current_hour = 0  # Convert 12 AM/PM to 0 for easier calculations
        return current_hour, am_pm

    def remaining_work_hours(self):
        # Assuming work hours are from 9 AM to 9 PM
        current_hour, am_pm = self.parse_current_time()
        if am_pm == "PM":
            current_hour += 12 if current_hour != 12 else 0
        elif am_pm == "AM" and current_hour == 12:
            current_hour = 0

        if 9 <= current_hour < 21:
            return 21 - current_hour
        return 0

    def action_dialog(self, action_type):
        # Determine the title of the action dialog based on the action type
        action_titles = {
            'work': "Work",
            'relax': "Hobbies",
            'sleep': "Sleep"
        }
        title = action_titles.get(action_type, "Action")

        # Handle work action
        if action_type == 'work':
            if self.current_day in ["Saturday", "Sunday"]:
                self.add_text_with_sound("It's the weekend. No work today!")
                return
            remaining_hours = self.remaining_work_hours()
            if remaining_hours <= 0:
                self.add_text_with_sound("Work hours are over for today.")
                return
            # Ask the player for the number of hours they want to work
            hours = simpledialog.askinteger(title, f"Enter hours to {title.lower()} (up to {remaining_hours} hours):", minvalue=1, maxvalue=remaining_hours)
        elif action_type == 'relax':
            hours = simpledialog.askinteger(title, f"Enter hours to {title.lower()}:", minvalue=1, maxvalue=12)
        else:
            # For sleep action, simply ask the player for hours
            hours = simpledialog.askinteger(title, f"Enter hours to {title.lower()}:", minvalue=1, maxvalue=12)

        # Proceed with the action if hours are provided
        if hours:
            self.make_decision(action_type, hours)


    def sleep(self, hours):
        self.add_text_with_sound(f"You slept for {hours} hours.")
        # Adjust happiness based on hours of sleep
        if hours < 6:
            self.player.happiness = max(0, self.player.happiness - 5)
            self.add_text_with_sound("You did not get a full rest.")
        elif hours >= 8:
            self.player.happiness = min(100, self.player.happiness + 5)
            self.add_text_with_sound("You got a full rest.")
        # Update the sleep timer
        self.player.sleep_timer = min(24, self.player.sleep_timer + (3 * hours))

        # Update time and day, but avoid altering the pass_out_timer again
        self.update_calendar_clock(hours, from_sleep=True)
        self.update_ui()

    def check_game_over(self):
        # Check if the game is over based on happiness or financial conditions
        if self.player.happiness <= 0:
            return 'happiness'
        if self.day_count > DAYS_IN_MONTH and self.player.finances < FINANCE_GOAL:
            return 'finances'
        return None

    def update_ui(self):
        # Check if the game has met a game over condition
        game_over_reason = self.check_game_over()
        if game_over_reason:
            # If there's a game over reason, handle the game over scenario
            self.handle_game_over(game_over_reason)
        else:
            # Otherwise, update the UI with the current happiness and finance status
            message = f"Happiness: {self.player.happiness}, Finances: {self.player.finances}\n"
            self.add_text_with_sound(message)
            self.update_progress_bars()

    def handle_game_over(self, reason):
        # Handle different game over scenarios based on the reason
        if reason == 'happiness':
            script = self.events.get_random_happiness_game_over_script()
        elif reason == 'finances':
            script = self.events.get_random_finances_game_over_script()

        # Display the game over message if the script is a valid string
        if isinstance(script, str):
            self.add_text_with_sound(script, narrator_mode=True)
            self.prompt_restart()  # Prompt player to restart or quit the game after game over message
        else:
            print("Error: Script is not a string.")  # Error handling for invalid script format

    def game_over(self):
        # Display a simple game over message
        self.add_text_with_sound("Game Over")
        self.prompt_restart()  # Prompt the player to restart or quit the game

    def prompt_restart(self):
        # Prompt the player to restart the game after a game over scenario
        restart = messagebox.askyesno("Game Over", "Do you want to restart the game?")
        if restart:
            # If the player chooses to restart, reset the game state
            self.restart_game()
        else:
            # If the player chooses not to restart, quit the application
            self.root.quit()

    def restart_game(self):
        # Logic for restarting the game
        chiding_remark = "Oh, back for more, are we?# Optimism or foolishness,# I wonder.#\n Let's skip the pleasantries this time."
        self.add_text_with_sound(chiding_remark, narrator_mode=True)
        # Reset the game state to start anew
        self.player = Player()  # This will reset day_count, sleep_timer, and other player attributes
        self.events.reset_answered_questions()  # Reset answered questions in quiz
        self.current_day = "Sunday"
        self.current_time = "11 PM"
        self.day_count = 1
        self.has_studied_today = False
        # Update the UI to reflect the new state of the game
        self.update_ui()

    def update_text_box(self, message):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, message + "\n")
        self.text_box.config(state=tk.DISABLED)
        self.text_box.see(tk.END)

    def update_progress_bars(self):
        # Update the happiness progress bar
        self.happiness_bar['value'] = self.player.happiness

        # Update the finances progress bar
        # Calculate the percentage of the financial goal achieved
        financial_progress = (self.player.finances / FINANCE_GOAL) * 100
        self.finances_bar['value'] = financial_progress
        self.update_ui

        self.root.update_idletasks()  # Update the UI immediately

    def save_game(self):
        # Save the current game state to a file for future loading
        game_data = {
            'player': self.player,
            'current_day': self.current_day,
            'day_count': self.day_count
        }
        with open('game_save.pkl', 'wb') as f:
            pickle.dump(game_data, f)  # Use pickle to serialize and save game data
        self.update_text_box("\nYour game has been saved!")  # Notify the player that the game has been saved

    def load_game(self):
        # Load a previously saved game if a save file exists
        if os.path.exists('game_save.pkl'):
            with open('game_save.pkl', 'rb') as f:
                game_data = pickle.load(f)  # Use pickle to deserialize and load game data

            # Update the current game state with loaded data
            self.player = game_data['player']
            self.current_day = game_data['current_day']
            self.day_count = game_data['day_count']

            # Reinitialize the game UI to reflect the loaded game state
            for widget in self.root.winfo_children():
                widget.destroy()
            self.setup_ui()

            # Welcome the player back with a random message
            welcome_back_message = random.choice(self.events.welcome_back_messages)
            self.add_text_with_sound(welcome_back_message, narrator_mode=True)

            self.update_text_box("Your game has been loaded!")  # Notify the player that the game has been loaded
            self.update_progress_bars()  # Update progress bars to reflect the new state
            self.update_calendar_clock(0)  # Set the correct time and date based on loaded data
        else:
            # Show a warning if no save file is found
            messagebox.showwarning("No Save Found", "No saved game found.")

# Create the main window
root = tk.Tk()
game = Game(root)
root.mainloop()