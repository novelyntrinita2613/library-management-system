<div align="center">

# 📚 Library Management System

### ✨ Book Lovers Club — A simple, MySQL-powered library management application

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-blueviolet?style=for-the-badge)

*Organise books, manage memberships, and keep track of borrowing and returns — all from a simple command-line interface.*

</div>

---

## 🌟 About the Project

The **Library Management System** is a Python application backed by a MySQL database. It is based on the project documented in the accompanying CBSE Computer Science project PDF.

The application is designed for librarian/administrator use. It stores book and member details, records borrowing and return transactions, supports searching, and exports database records to text files.

## 🚀 Features

| # | Feature | What it does |
|---|---|---|
| 1 | 📖 Add a book | Stores a book title, author, copy count and unique book ID |
| 2 | 👤 Add a member | Records member ID, name, email, phone, borrowing count and membership status |
| 3 | 📤 Borrow a book | Saves book, member, borrowing date and due date |
| 4 | 📥 Return a book | Records the return date and borrow status |
| 5 | 📚 View books | Displays all books in the catalogue |
| 6 | 🔎 Search books | Searches using the book title and author |
| 7 | 🧑‍🤝‍🧑 View members | Displays registered library members |
| 8 | 🔍 Search members | Searches using member ID and name |
| 9 | 🗑️ Delete a book | Removes a matching book record |
| 10 | 🚪 Delete membership | Removes a matching member record |
| 11 | ❌ Exit | Ends the current menu session |

### 💾 Automatic text-file exports

After adding, borrowing, returning or deleting records, the application refreshes the corresponding text export:

- `books.txt` — book catalogue
- `members.txt` — membership records
- `borrow.txt` — borrowing records
- `return.txt` — return records

These files are generated in the working directory when the corresponding menu action runs.

## 🧰 Tech Stack

- **Python 3.12 or later** — application logic
- **MySQL 8.0 or later** — persistent data storage
- **mysql-connector-python** — Python-to-MySQL connection

## 📁 Project Structure

```text
library-management-system/
│
├── main.py             # Main application and all library operations
├── requirements.txt    # Python dependency
├── .env.example        # Example database configuration
├── sample_data.sql     # Optional demonstration records from the PDF
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

> The database and four text-export files are created/updated when the application runs. The export files are intentionally excluded from Git because they contain local library data.

## ⚙️ Installation & Setup

### 1. Install the prerequisites

Install:

- [Python](https://www.python.org/downloads/) (3.12 or later)
- [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)

During MySQL setup, create or identify a MySQL user that has permission to create a database and tables.

### 2. Clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/library-management-system.git
cd library-management-system
```

### 3. Create and activate a virtual environment (recommended)

**Windows — Command Prompt**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install the Python dependency

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

The application reads these environment variables:

| Variable | Default | Description |
|---|---|---|
| `DB_HOST` | `localhost` | MySQL server address |
| `DB_USER` | `root` | MySQL username |
| `DB_PASSWORD` | `krithika07` | MySQL password |
| `DB_NAME` | `librarymanagement` | Database name |

For a quick local run, you can edit the default values near the top of `main.py`.

**Windows PowerShell example:**

```powershell
$env:DB_HOST="localhost"
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_NAME="librarymanagement"
```

**macOS / Linux example:**

```bash
export DB_HOST="localhost"
export DB_USER="root"
export DB_PASSWORD="your_mysql_password"
export DB_NAME="librarymanagement"
```

> 🔐 Never commit real database passwords to GitHub. Use environment variables and keep local credentials private. The default password in the source is retained from the original PDF for compatibility; change it before publishing or using the project outside a local demonstration.

### 6. Run the application

Make sure the MySQL server is running, then execute:

```bash
python main.py
```

On first run, the program creates the `librarymanagement` database and the required tables automatically.

## 🔑 Login

The original project checks the password and accepts a username as an input.

| Prompt | Demonstration value |
|---|---|
| Username | `abcd` |
| Password | `novakiki#2122` |

> ⚠️ This is the original demonstration login from the project document, not production-grade authentication. The username is prompted for but is not independently validated. Change the authentication design before real-world deployment.

## 🖥️ Application Menu

After successful authentication, the application displays:

```text
Menu:
1. Add a Book
2. Add a member
3. Borrow a book
4. Return a book
5. Viewing available books
6. Searching available books
7. Viewing already existing members of the library
8. Searching for an already existing member
9. Delete a book
10. Delete a membership
11. Exit
Enter your choice:
```

Choose an option and enter the requested information. Dates for borrowing and returning should use `YYYY-MM-DD` format, for example `2024-07-05`.

The menu performs one selected operation per login session, matching the original program's flow. Run the program again to perform another operation.

## 🗄️ Database Design

The application creates these four tables:

| Table | Purpose |
|---|---|
| `books` | Book title, author, available copy count and book ID |
| `membership` | Member identity and membership information |
| `borrow` | Book borrowing and due-date records |
| `return_book` | Book return date, status and member ID |

The database is named `librarymanagement` by default.

## 🧪 Testing the Sample Workflows

The supplied PDF's sample-output section (pages 46–54) demonstrates these workflows:

- 🔐 Successful login and incorrect-password handling
- 📖 Adding a book and checking the books table/text export
- 👤 Adding a member and checking the membership table/text export
- 📤 Recording a borrowing transaction
- 📥 Recording a return transaction
- 📚 Viewing the book catalogue
- 🔎 Searching for an existing and a non-existing book
- 🧑‍🤝‍🧑 Viewing and searching member records
- ❌ Exiting the application

To reproduce the examples, run `python main.py` separately for each operation and enter the values shown in the PDF screenshots. The database starts empty unless you add records. To load the demonstration records transcribed from the PDF's sample database screenshots, first run the application once so it creates the database and tables, then import the optional SQL file:

```bash
mysql -u root -p librarymanagement < sample_data.sql
```

On Windows, run the same command from a terminal where the MySQL client is available. This is optional; it is not run automatically, so a normal first launch starts with an empty catalogue.

## 🛠️ Error Fixes & Compatibility Notes

The original source has been kept recognisable: the same menu options, function names, table concepts, input-driven workflow and text exports remain.

The following defects were corrected so the program can run:

- Replaced typographic quotation marks with valid Python/SQL syntax.
- Corrected indentation and malformed statements in the menu and delete functions.
- Added database creation before connecting to the selected database.
- Added table creation for all four tables at startup.
- Replaced unsafe string-formatted SQL with parameterised queries.
- Corrected the member deletion column from `mid` to `member_id`.
- Removed the inappropriate primary-key restriction from `return_book.member_id`, allowing multiple return records for a member.
- Fixed the incomplete `borrow_file()` print statement.
- Avoided closing the shared database connection inside delete operations.
- Added basic handling for invalid numeric menu input and MySQL connection errors.

**Important scope note:** The original program records borrow and return transactions; it does not implement automatic stock deduction, overdue fine calculation, reservations, or automatic reconciliation of borrow/return records. Those behaviours have not been added because the goal is to retain the original project's scope and structure.

## 🔮 Future Enhancements

Ideas listed in the original project include:

- ☁️ Automated database backups
- 🔐 Stronger authentication and two-factor authentication
- 📱 A mobile application
- 🔔 Book-return reminders
- 📌 Online book reservations
- 💬 Member feedback and book suggestions

## 📚 Reference

This repository is based on the **Library Management System** Computer Science project document (SSCE 2024–2025). The original document's sample outputs are shown on pages 46–54.

## 🤝 Contributions

Suggestions and improvements are welcome. If you find a bug or want to propose an enhancement, open an issue or submit a pull request.

---

<div align="center">

### 📖 Every book has a story. Every library deserves a system.

**Made with 🐍 Python + 🐬 MySQL**

</div>
