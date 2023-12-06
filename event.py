import random
from tkinter import messagebox
import time
from scripts import quiz_questions, random_events, introductions

class Events:
    def __init__(self, game):
        self.game = game
        self.quiz_questions = quiz_questions
        self.answered_questions = set()
        self.random_events = random_events            
        self.introductions = introductions
        
        #Should move these to script file but was lazy:
        self.happiness_game_over_scripts = [
            "Ah, the inevitable end of your virtual journey.# Your avatar has found an escape from the endless loops of Python and despair.# This simulation has reached its conclusion. Next time, maybe try a bit more 'virtual laughter' amid the coding tears.",
            "Alas, your happiness meter has hit the great zero in the sky.# In this digital realm, that's a terminal error, not just for your code, but for your avatar's will to keep debugging.# In your next simulation, remember: even pixels need a bit of joy.",
            "Your happiness has flatlined, right down to zero.# It seems the relentless grind of virtual code and existential dread proved too much for your avatar.# Next iteration, consider sprinkling a little more digital sunshine amidst the gloomy algorithms."
        ]

        self.finances_game_over_scripts = [
            "Time's up##, and your bank account is as empty as your social calendar.# Seems like you've coded your way into financial ruin.# Maybe next time, aim for a virtual job that pays better!",
            "The month is over, but your financial goal remains a distant dream.# In the harsh reality of this game, that spells failure.# Perhaps virtual financial management isn't your forte?",
            "As the virtual month draws to a close, so does your game.# Falling short of your financial target means it's game over.# Maybe in your next virtual life, you'll be a bit thriftier!"
        ]

        self.welcome_back_messages = [
            "Ah,# the prodigious coder returns.# Missed the relentless key-tapping?",
            "Welcome back.# The digital realm awaited your triumphant return with bated bytes.",
            "Oh,## it's you again.# Did the real world prove too mundane for your programming prowess?",
            "Prepared to resume your illustrious coding career in .Py?# The anticipation was palpable.",
            "And here you are,# once more.# The virtual world quivers in excitement...# or## is it fear?"
        ]

    def get_random_welcome_back_message(self):
        return random.choice(self.welcome_back_messages)
                             
    def get_random_introduction(self):
        return random.choice(self.introductions)

    def get_random_happiness_game_over_script(self):
        return random.choice(self.happiness_game_over_scripts)

    def get_random_finances_game_over_script(self):
        return random.choice(self.finances_game_over_scripts)

    def trigger_random_event(self, player):
            event = random.choice(self.random_events)

            # Display the event description with the narrator style
            self.game.add_text_with_sound(event["description"], narrator_mode=True)

            # Short pause after description before showing messagebox
            self.game.root.update()  # Process all pending events to update the text box
            time.sleep(2)  # Wait a bit for the user to read the description

            # Show the decision dialog and get the user's choice
            decision = messagebox.askyesno("Decision Time", "Do you wish to proceed?")
            decision_text = "yes" if decision else "no"
            
            # Determine and return the outcome based on the user's decision
            return self.determine_event_outcome(event, player, decision_text)

    def show_decision_dialog(self, event, player):
        # Now show the messagebox to get the user's decision
        decision = messagebox.askyesno("Decision Time", "Do you wish to proceed?")
        decision_text = "yes" if decision else "no"
        
        # Determine the outcome based on the user's decision
        outcome_text = self.determine_event_outcome(event, player, decision_text)
        
        # Display the outcome with the narrator style
        self.game.add_text_with_sound(outcome_text, narrator_mode=True)

    def determine_event_outcome(self, event, player, decision):
        if decision.lower() == 'yes':
            if random.random() < event["positive_chance"]:
                player.happiness += event["effect"].get("happiness", 0)
                player.finances += event["effect"].get("finances", 0)
                return event["positive_outcome"]
            else:
                player.happiness += event["effect"].get("neg_happiness", 0)
                player.finances += event["effect"].get("neg_finances", 0)
                return event["negative_outcome"]
        else:
            return "You decided not to take the risk."


    def get_quiz_question(self):
        remaining_questions = {k: v for k, v in self.quiz_questions.items() if k not in self.answered_questions}

        if remaining_questions:
            question_key = random.choice(list(remaining_questions.keys()))
            self.answered_questions.add(question_key)  # Store the question key
            return remaining_questions[question_key]
        else:
            return {
                "question": "No more questions.",
                "options": ["A) Repeat", "B) Stop"],
                "answer": "A",
                "explanation": "You can choose to repeat the quiz or stop here."
            }

    def reset_answered_questions(self):
        self.answered_questions.clear()