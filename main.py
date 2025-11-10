"""
Database Interaction Application - Assignment (3) Q(1)
------------------------------------------------------
This script connects to a PostgreSQL database and performs
CRUD operations on the 'students' table.

Functions implemented:
1. getAllStudents()         - Retrieve all records
2. addStudent()             - Insert a new record
3. updateStudentEmail()     - Update email for a given student_id
4. deleteStudent()          - Delete record by student_id

Author: [Your Name]
Date: [Date]
"""

import os
import psycopg2
from psycopg2 import sql
from psycopg2.errors import UniqueViolation

# -----------------------------------------------
# Database connection configuration
# -----------------------------------------------
# Read DB configuration from environment variables for safety and flexibility.
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "your_database_name"),
    "user": os.getenv("DB_USER", "your_postgres_username"),
    "password": os.getenv("DB_PASSWORD", "your_postgres_password"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}

# -----------------------------------------------
# Function: create_connection()
# -----------------------------------------------
def create_connection():
    """Create and return a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Error while connecting to the database:", e)
        return None

# -----------------------------------------------
# Function: getAllStudents()
# -----------------------------------------------
def getAllStudents():
    """Retrieve and display all student records."""
    conn = create_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM students ORDER BY student_id;")
                rows = cur.fetchall()
                print("\nAll Students:")
                for row in rows:
                    print(row)
        except Exception as e:
            print("Error fetching data:", e)
        finally:
            conn.close()

# -----------------------------------------------
# Function: addStudent()
# -----------------------------------------------
def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student record."""
    conn = create_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO students (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s);
                """, (first_name, last_name, email, enrollment_date))
                conn.commit()
                print(f"✅ Added: {first_name} {last_name}")
        except Exception as e:
            # Handle common unique constraint violation for email
            if isinstance(e, UniqueViolation) or getattr(e, 'pgcode', None) == '23505':
                print(f"Error: email '{email}' already exists.")
            else:
                print("Error inserting data:", e)
        finally:
            conn.close()

# -----------------------------------------------
# Function: updateStudentEmail()
# -----------------------------------------------
def updateStudentEmail(student_id, new_email):
    """Update the email address for a given student."""
    conn = create_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE students
                    SET email = %s
                    WHERE student_id = %s;
                """, (new_email, student_id))
                conn.commit()
                print(f"✏️ Updated student {student_id} email to {new_email}")
        except Exception as e:
            print("Error updating data:", e)
        finally:
            conn.close()

# -----------------------------------------------
# Function: deleteStudent()
# -----------------------------------------------
def deleteStudent(student_id):
    """Delete a student record by ID."""
    conn = create_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
                conn.commit()
                print(f"🗑️ Deleted student with ID: {student_id}")
        except Exception as e:
            print("Error deleting data:", e)
        finally:
            conn.close()

# -----------------------------------------------
# Main execution for demo purposes
# -----------------------------------------------
if __name__ == "__main__":
    # Example usage
    print("Connecting to PostgreSQL database...")

    getAllStudents()  # Retrieve initial data

    # Add a new student
    addStudent("Alice", "Johnson", "alice.johnson@example.com", "2023-09-03")

    # Update student email
    updateStudentEmail(1, "john.newemail@example.com")

    # Delete a student by ID
    deleteStudent(3)

    # Show final list
    getAllStudents()
