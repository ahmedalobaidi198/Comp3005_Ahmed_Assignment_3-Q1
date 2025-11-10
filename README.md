# Assignment 3 – Q(1): PostgreSQL Students CRUD

**Name:** Ahmed Al-Obaidi
**Student ID:** 101259592

---

## 📘 Overview

This repository contains a simple Python application demonstrating CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database.

### Files

- **`db/setup.sql`** — SQL script to create the `students` table and insert initial data.
- **`main.py`** — Python script implementing the CRUD functions using `psycopg2`.

---

## Prerequisites

- Python **3.8+**
- PostgreSQL server (local or remote)
- `psycopg2-binary` Python package

---

## Setup Instructions

1. **Create a PostgreSQL database** (e.g., `assignment3`) and user with proper privileges.
2. **Run the SQL setup script:**

   ```bash
   psql -U your_postgres_username -d your_database_name -f db/setup.sql
   ```

3. **Install dependencies:**

   ```bash
   python3 -m pip install psycopg2-binary
   ```

4. **Set environment variables (recommended):**

   ```bash
   export DB_NAME=your_database_name
   export DB_USER=your_postgres_username
   export DB_PASSWORD=your_postgres_password
   export DB_HOST=localhost
   export DB_PORT=5432
   ```

---

## 💻 macOS / Homebrew Note

If `psql` is not available in your PATH, install it using Homebrew:

```bash
brew install libpq
export PATH="/opt/homebrew/opt/libpq/bin:$PATH"
```

_(For Intel Macs, the path may be `/usr/local/opt/libpq/bin`.)_
To make the PATH permanent, add this line to your `~/.zshrc`.

---

## 🚀 Quick Start Example

Replace placeholders with your own values before running these commands.

```bash
# Run the SQL setup
psql -U your_postgres_username -d your_database_name -f db/setup.sql

# Install dependency
python3 -m pip install psycopg2-binary

# Set environment variables
export DB_NAME=your_database_name
export DB_USER=your_postgres_username
export DB_PASSWORD='your_postgres_password'
export DB_HOST=localhost
export DB_PORT=5432

# Run the application
python3 main.py

# Verify results
psql -U your_postgres_username -d your_database_name -c "SELECT * FROM students ORDER BY student_id;"
```

---

## ▶️ Running the Application

Execute the demo script:

```bash
python3 main.py
```

The program will:

1. Display all students (Read)
2. Attempt to insert a duplicate student (Create – with error handling)
3. Update an existing student’s email (Update)
4. Delete one student record (Delete)
5. Display the final table

---

## Notes

- The script reads database settings from **environment variables** for security.
- If variables are not set, it defaults to placeholder values — update them before running.
- For your demonstration video, show table contents **before and after** the operations (using `psql` or pgAdmin).

---

## 🎥 Video Demo

**Link:** https://mediaspace.carleton.ca/media/Assignment3_Q1/1_a5p3zb4b
