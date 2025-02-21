# TASK : Create a base note class that stores the contents and record the datetime

from datetime import datetime

# 1. Base Class: Note
class Note:
    """
    A class to represent a simple note.
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

# Creating an instance of Note
note = Note("I'm trying my best, this code must run oo")
note.display()

# 2. Derived Class: TextNote (inherits from Note)
class TextNote(Note):
    """
    A subclass of Note that inherits its behavior.
    Overrides the display method
    """
    def display(self):
        return super().display()

# Creating an instance of TextNote
textnote = TextNote("Please u dis code run")
print(textnote.display())


