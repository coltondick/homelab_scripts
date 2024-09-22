# Usage:
# python reset_word_count.py user_id "example"

import sqlite3
import sys


# Function to connect to the SQLite database
def connect_to_database(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        sys.exit(1)


# Function to update the word quantity for a specific user
def update_word_quantity(conn, user_id, word):
    sql_command = """
    UPDATE member_words 
    SET quantity = '1' 
    WHERE user_id = ? 
    AND word = ?;
    """
    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Execute the SQL command with the passed user_id and word
        cursor.execute(sql_command, (user_id, word))

        # Commit the changes
        conn.commit()

        print("Update executed successfully.")
    except sqlite3.Error as error:
        print("Error while executing the update:", error)


# Main function to handle the process
def main(database_path, user_id, word):
    conn = connect_to_database(database_path)

    try:
        update_word_quantity(conn, user_id, word)
    finally:
        # Close the connection
        if conn:
            conn.close()


# Script entry point
if __name__ == "__main__":
    # Check if correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python script.py <user_id> <word>")
        sys.exit(1)

    # Arguments passed into the script
    user_id = sys.argv[1]
    word = sys.argv[2]

    # Path to your SQLite database
    database_path = "/docker/appdata/segafanbot/cogs/WordStats/wordstats.db"

    # Call the main function with the provided arguments
    main(database_path, user_id, word)
