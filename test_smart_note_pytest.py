import pytest  # Okay, first step: import pytest so I can run my tests
from Smart_Note import NotesManager  # Importing my NotesManager class from Smart_Note.py


# --- STARTING WITH ADDING NOTES ---
# I need to make sure I can add different types of notes properly.

def test_add_text_note():
    """Checking if a text note is added correctly."""
    manager = NotesManager()  # Create a new instance of NotesManager
    result = manager.add_note("text", "Test Note")  # Add a simple text note

    # Now, I should check if the note was added successfully
    assert "Note added successfully!" in result  # Expecting this success message
    assert len(manager.notes) == 1  # There should be exactly one note now
    assert manager.notes[0].content == "Test Note"  # Confirming the note content is correct


def test_add_reminder_note():
    """Making sure a reminder note works when I provide a reminder time."""
    manager = NotesManager()
    result = manager.add_note("reminder", "Submission of task", "2025-02-28 11:59")

    # Checking if it worked
    assert "Note added successfully!" in result
    assert len(manager.notes) == 1  # Should be one note in the list
    assert manager.notes[0].content == "Submission of task" # Note text should match
    assert manager.notes[0].reminder_time == "2025-02-28 11:59"  # Reminder time should be correct


def test_add_reminder_note_without_time():
    """If I forget to add a reminder time, the function should return an error."""
    manager = NotesManager()
    result = manager.add_note("reminder", "Submission of task")  # No time provided

    # Should return an error message
    assert result == "Error: Reminder note requires a reminder time."


def test_add_invalid_note_type():
    """Testing if the program correctly rejects an invalid note type."""
    manager = NotesManager()
    result = manager.add_note("invalid", "Invalid Note")  # Trying an unsupported type

    # Should return an error message
    assert result == "Error: Invalid note type."


# --- TESTING DELETING NOTES ---
# Need to check if deleting notes works properly.

def test_delete_existing_note():
    """First, I add a note. Then I try to delete it and check if it’s really gone."""
    manager = NotesManager()
    manager.add_note("text", "To be deleted")  # Add a note first
    note_id = manager.notes[0].note_id  # Get its ID

    result = manager.delete_note(note_id)  # Now delete it

    # Should return a success message and remove the note
    assert result == f"Note {note_id} deleted successfully."
    assert len(manager.notes) == 0  # Notes list should be empty now


def test_delete_non_existing_note():
    """Trying to delete a note that doesn’t exist should return an error."""
    manager = NotesManager()
    result = manager.delete_note(200)  # Fake ID that doesn’t exist

    assert result == "Error: Note ID not found."  # Should return an error


# --- TESTING DISPLAYING NOTES ---
# Making sure the show_note function correctly displays notes.

def test_show_notes():
    """Adding multiple notes and checking if they show up."""
    manager = NotesManager()
    manager.add_note("text", "First Note")
    manager.add_note("text", "Second Note")

    result = manager.show_note()

    assert "First Note" in result  # First note should appear
    assert "Second Note" in result  # Second note should appear


def test_show_notes_empty():
    """If no notes exist, it should say 'No notes available.'"""
    manager = NotesManager()

    result = manager.show_note()

    assert result == "No notes available."


# --- TESTING SEARCHING NOTES ---
# Making sure searching works correctly.

def test_search_note_found():
    """Adding a note and making sure I can find it by searching."""
    manager = NotesManager()
    manager.add_note("text", "Meeting notes")

    result = manager.search_note("Meeting")  # Search for 'Meeting'

    assert "Meeting notes" in result  # This note should show up



def test_search_note_not_found():
    """If I search for something that isn’t in my notes, it should say no matches."""
    manager = NotesManager()
    manager.add_note("text", "Only this note exists")

    result = manager.search_note("meeting")  # Search for something not in notes

    assert result == "No matching note found."


# --- PARAMETERIZED TESTING ---
# This helps me test multiple cases at once.

@pytest.mark.parametrize("note_type, content, reminder_time, expected", [
    ("text", "write any note content", None, "Note added successfully!"),  # Normal text note
    ("reminder", "Reminder message", "2025-05-01 12:00", "Note added successfully!"),  # Reminder with time
    ("reminder", "Missing time", None, "Error: Reminder note requires a reminder time."),  # Missing time
    ("invalid", "Wrong Type", None, "Error: Invalid note type."),  # Invalid type
])
def test_add_note_parametrized(note_type, content, reminder_time, expected):
    """Using pytest parameterized tests to check different note types."""
    manager = NotesManager()
    result = manager.add_note(note_type, content, reminder_time)

    assert expected in result  # Result should match expected output
