# TASK: CREATION OF A SMART NOTE MANAGER


from datetime import datetime

# 1. Base Class: Note
class Note:
    """
    Attributes:
        content (str): The content of the note.
        created_at (datetime): The timestamp when the note is created.
    Methods:
        display(): Prints the note content and creation time.
    """
    def __init__(self, content): # why cant i add created_at insde?
        self.content = content
        self.created_at = datetime.now()

    def display(self):
        print(f"Note created at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Content: {self.content}")

# Creating a object instance for the code
note = Note("I'm trying my best, this code must run oo")
note.display()

# 2. Derived Class: TextNote (inherits from Note)

class TextNote(Note):
    """
    A subclass of Note that inherits its behavior also
    Overrides the display method
    """
    def display(self):
        return super().display()

# Creating a object instance
textnote = TextNote("Please u dis code run")
print(textnote.display())

# 2.1 Derived Class: TimeReminder (inherits from Note)

"""Inherits from the Note class and  functionality 
    extended to include a reminder time.

    Attributes:
        content (str): The content of the note.
        reminder_time (str): The time set for the reminder.
        created_at (datetime): Inherited from Note, stores when the note was created.

    Methods:
        display(): This will Overrides the display() method to show both 
                   the reminder time and the note details.
    """

class TimeReminder(Note):
    def __init__(self, content, reminder_time):
        super().__init__(content)  # Calls the constructor of the Note class
        self.reminder_time = reminder_time

    def display(self):
        print(f"Reminder Time: {self.reminder_time}") # I tried calling these at end of the code it doesnt wrk(CodeBlocks)
        return super().display()

# Creating an object instance for the code
reminder = TimeReminder("Submission date", "21-02-2025 11:59 PM")

print(reminder.display())

# 3. NoteManager Class (To Include other functionalities)
class NoteManager: # I really dont know how to go about this section of the task
    pass



