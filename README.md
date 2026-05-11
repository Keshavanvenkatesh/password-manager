# Password Manager

A desktop password manager built using PyQt5 with support for multiple users, password storage, editing, deletion, help/support reporting, and a built-in user guide.

---

# Features

- Multi-user login and signup system
- Store passwords securely per user
- Edit saved passwords
- Remove passwords
- Show all saved passwords
- GUI built with PyQt5
- Built-in help/support system
- Built-in user guide window
- Modular project structure
- Persistent local data storage

---

# Screenshots

## Login Window

<img width="393" height="170" alt="image" src="https://github.com/user-attachments/assets/3dafdb12-dc51-403f-84d9-e1ac8c9c1816" />

---

## Main Dashboard

<img width="822" height="520" alt="image" src="https://github.com/user-attachments/assets/ed881a9d-1e96-4b09-bb8e-b7d26caabf66" />

---

## Help & Support Window

<img width="443" height="271" alt="image" src="https://github.com/user-attachments/assets/ba96c8d5-b454-45f3-a6bb-e5c2a1cdbe1a" />


---

## User Guide Window

<img width="630" height="372" alt="image" src="https://github.com/user-attachments/assets/d9602028-5f54-4eac-a8d2-131e792c1b38" />

---

# Project Structure

```text
password_manager/
│
├── data/
│   ├── user_data.txt
│   └── user_guide.txt
│
├── logic/
│   ├── login_logic.py
│   ├── latest_main_logic.py
│   ├── help_logic.py
│   └── user_guide.py
│
├── models/
│   └── user_class.py
│
├── ui/
│   ├── login_ui.ui
│   ├── latest_main_ui_2.ui
│   ├── help_page.ui
│   └── user_guide.ui
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Keshavanvenkatesh/password-manager.git
```

Move into the project folder:

```bash
cd password-manager
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

# Technologies Used

- Python
- PyQt5
- Pickle
- pathlib
- Git & GitHub

---

# Support System

The application includes a built-in support page where users can:

- Report issues
- Send complaints
- Provide feedback

The app automatically includes:

- OS information
- Python version
- Platform details

inside support reports.

---

# Future Improvements

Planned future upgrades:

- Password encryption
- SQLite database integration
- Password generator
- Search functionality
- Dark mode
- Export/import support
- Cloud synchronization
- Better security architecture

---

# Security Note

This project is currently intended for educational and learning purposes.

Sensitive data is currently stored locally using pickle serialization and is not yet encrypted.

---

# Developer

Developed by:

Keshavan Venkatesh
