from datetime import datetime

# 1. Create a base class Note

class Note:
    """Base class of Note"""

    note_id_counter = 1  # These assign a unique class id counter and start with 1

    def __init__(self, content):
        self.content = content  # This stores the actual note content of the note
        self.created_at = datetime.now()  # It stores the timestamp when it's created
        self.note_id = Note.note_id_counter  # Assigns unique id
        Note.note_id_counter += 1  # Increment of the ID by 1

    def display(self):  # defining the method to display the note details
        return f"[{self.note_id}] {self.created_at.strftime('%Y-%m-%d %H:%M:%S')} - {self.content}"

    ## OOP CONCEPTS USED HERE :
    """ Encapsulation : Note class encapsulates attributes (content, created_at, note_id)
         Abstraction : display() method provides a simple way to retrieve note details without exposing its internal attributes."""

# 2. Create a Inheritance from the Base class (TextNote, ReminderNote)

class TextNote(Note):  # This includes a text note that extends the base note class to specify its a text note
    def display(self):  # To override the base note class method
        return f"Text Note {super().display()}"

    ## OOP CONCEPTS USED HERE :
    """Inheritance: TextNote inherits attributes & methods from Note
    Polymorphism: It overrides the display() method"""

class ReminderNote(Note):
    def __init__(self, content, reminder_time):
        super().__init__(content)
        self.reminder_time = reminder_time  # Assume it's already validated

    def display(self):
        return f"Reminder Note {super().display()} | Reminder Date&Time: {self.reminder_time.strftime('%Y-%m-%d %H:%M')}"

    ## OOP CONCEPTS USED HERE :
    """Inheritance, Polymorphism, Encapsulation"""

# 3. Defining the Note Manager Class

class NotesManager:
    """What does this do? It Manages, Deletes, Views, and Searches the Note content"""
    def __init__(self):  # This will initialize an empty list to store the notes
        self.notes = []

    def add_note(self, note_type, content, reminder_time=None):
        
        # Check for duplicate notes
        for note in self.notes:
            if note.content == content and isinstance(note, (TextNote if note_type == "text" else ReminderNote)):
                return "Error: Duplicate note exists."

        if note_type == "text":
            note = TextNote(content)
        elif note_type == "reminder":
            if not reminder_time:
                return "Error: Reminder note requires a reminder time."
            # Ensure to validate reminder_time BEFORE creating ReminderNote
            try:
                reminder_time = datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")
            except ValueError:
                return "Error: Invalid datetime format. Use YYYY-MM-DD HH:MM."

            note = ReminderNote(content, reminder_time)
        else:
            return "Error: Invalid note type."

        self.notes.append(note)
        return f"Note added successfully! (ID: {note.note_id})"


    ## OOP CONCEPTS USED HERE :
    """Encapsulation: keeps all self.notes private to the NoteManager class
    Abstraction: Users just need to call add_note(), without worrying about object creation details
    Polymorphism: The method here works for both the TextNote and ReminderNote, despite their differences"""

    # 3.1. Delete Action
    def delete_note(self, note_id):  # Deleting notes by their unique ID
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                return f"Note {note_id} deleted successfully."
        return "Error: Note ID not found."

    # 3.2. Showing Action
    def show_note(self):  # Displaying the notes
        if not self.notes:
            return "No notes available."
        return "\n".join(note.display() for note in self.notes)
        """We can see polymorphism in action here where the display() method is called on different note types, having different implementations."""

    # 3.3. Searching for a note
    def search_note(self, keyword):
        results = [note.display() for note in self.notes if keyword.lower() in note.content.lower()]
        return "\n".join(results) if results else "No matching note found."
    """We can see the use of encapsulation to protect the content of self.notes, which can only be accessed through these methods only."""

# 4. The User Interface Code

def main():
    manager = NotesManager()

    while True:
        print("\n Smart Note Manager")
        print("1. Add Note")
        print("2. Delete Note")
        print("3. View Note")
        print("4. Search Note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            note_type = input("Enter note type (text/reminder): ").strip().lower()
            content = input("Enter note content: ").strip()
            reminder_time = None
            if note_type == "reminder":
                reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM): ").strip()

            result = manager.add_note(note_type, content, reminder_time)
            print(result)

        elif choice == "2":
            try:
                note_id = int(input("Enter note ID to delete: "))
                print(manager.delete_note(note_id))
            except ValueError:
                print("Error: Invalid ID, please enter a number.")

        elif choice == "3":
            print(manager.show_note())

        elif choice == "4":
            keyword = input("Enter keyword to search: ").strip()
            print(manager.search_note(keyword))

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

