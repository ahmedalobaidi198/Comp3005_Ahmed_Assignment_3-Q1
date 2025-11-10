# Assignment 3 – Q(1): PostgreSQL Students CRUD

**Name:** Ahmed Al-Obaidi
**Student ID:** 101259592

## Overview

Python app that connects to PostgreSQL and runs CRUD (Create, Read, Update, Delete) on a `students` table.

### Files

- `db/setup.sql` – creates the table and seeds initial rows
- `main.py` – CRUD functions using `psycopg2`

## Prerequisites

- Python 3.8+
- PostgreSQL
- `psycopg2-binary`

## Setup

1. Create a database (e.g., `assignment3`) and a user with access.
2. Run the SQL setup:

```bash
psql -U your_postgres_username -d your_database_name -f db/setup.sql
```

3. Install dependency:

```bash
python3 -m pip install psycopg2-binary
```

4. Set environment variables:

```bash
export DB_NAME=your_database_name
export DB_USER=your_postgres_username
export DB_PASSWORD=your_postgres_password
export DB_HOST=localhost
export DB_PORT=5432
```

##

## Quick start

```bash
# create table + seed data
psql -U your_postgres_username -d your_database_name -f db/setup.sql

# install dependency
python3 -m pip install psycopg2-binary

# env vars
export DB_NAME=your_database_name
export DB_USER=your_postgres_username
export DB_PASSWORD='your_postgres_password'
export DB_HOST=localhost
export DB_PORT=5432

# run the app
python3 main.py

# verify
psql -U your_postgres_username -d your_database_name -c \
"SELECT * FROM students ORDER BY student_id;"
```

## Running the app

```bash
python3 main.py
```

It will:

1. list all students
2. try to insert a duplicate (shows friendly error)
3. update one email
4. delete one row
5. list the final table

## Notes

- The app reads DB settings from environment variables. If they aren’t set, replace placeholders before running.
- For the demo video, show the table before/after in `psql` or pgAdmin.

## Video

https://mediaspace.carleton.ca/media/Assignment3_Q1/1_a5p3zb4b
