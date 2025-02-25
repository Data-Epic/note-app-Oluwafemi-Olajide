# note-app-Oluwafemi-Olajide

# Smart Note Manager

##  Project Description
Smart Note Manager is a Python-based command-line application that allows users to create, manage, and search notes efficiently. It supports two types of notes:
- **Text Notes**: Regular notes with text content.
- **Reminder Notes**: Notes with a specified reminder time.

This project demonstrates object-oriented programming (OOP) principles such as **Encapsulation, Inheritance, Polymorphism, and Abstraction**.

---
##  Features
- Create text and reminder notes
- View all saved notes
- Delete notes by ID
- Search notes by keyword
- User-friendly CLI interface

---
##  OOP Concepts Used
1. **Encapsulation**:
   - Attributes like `self.notes` are encapsulated within the `NotesManager` class.
   - Users interact with the class via methods instead of accessing attributes directly.

2. **Abstraction**:
   - Methods like `add_note()` hide complex object creation logic from the user.
   
3. **Inheritance**:
   - `TextNote` and `ReminderNote` inherit from the `Note` base class.
   
4. **Polymorphism**:
   - The `display()` method is overridden in `TextNote` and `ReminderNote` for customized output.

---
##  Project Structure
```
Smart-Note-Manager/
│── notes_manager.py  # Main application script
│── README.md         # Project documentation
```

---
##  Installation & Usage
### Prerequisites
- Python 3.x installed on your system

### Run the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd Smart-Note-Manager
   ```
2. Run the script:
   ```bash
   python notes_manager.py
   ```

---
##  How to Use
1. Run the application and choose an option:
   - **1. Add Note** → Create a new note (Text or Reminder)
   - **2. Delete Note** → Delete a note by ID
   - **3. View Note** → Show all notes
   - **4. Search Note** → Find notes containing a keyword
   - **5. Exit** → Close the application

2. Follow the on-screen instructions to input note details.


---
## 🤝 Contributing
Feel free to submit pull requests or open issues for improvements!


