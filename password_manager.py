import sqlite3
import secrets
import string

connection = sqlite3.connect("passwords.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY,
    website TEXT,
    username TEXT,
    password TEXT
)
""")

connection.commit()

def letters():
    return string.ascii_letters

def numbers():
    return string.digits

def symbols():
    return string.punctuation

def get_characters_set():
    return letters() + numbers() + symbols()

def generate_password(length):
            characters_set = get_characters_set()

            password = ''.join(secrets.choice(characters_set) for _ in range(length))

            return password

def clear_screen():
    import os

    os.system("cls" if os.name == "nt" else "clear")

def password_manager():
         clear_screen()

         print("1. Add a password")
         print("2. View a password")
         print("3. Delete password")
         print("4. Edit password")
         print("5. Exit")

         try:
            choice = int(input("Choice: "))
         except ValueError:
            print("Please enter a number.")
            return


         if choice == 1:
            website = input("Website: ").lower()
            username = input("Username: ")
            length = int(input("Password length: "))
            password = generate_password(length)

            print("password saved")
            print(website)
            print(username)
            print(password)
            input("\nPress Enter to continue...")

            cursor.execute(
                "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                (website, username, password)
            )

            connection.commit()

         elif choice == 2:
            website_pass = input("What website password do you want to view?: ").lower()

            cursor.execute(
                "SELECT username, password FROM passwords WHERE website = ?",
                (website_pass,)
            )

            result = cursor.fetchone()

            if result:
                print("Website found!")
                print(f"Username: {result[0]}")
                print(f"Password: {result[1]}")
                input("\nPress Enter to continue...")
            else:
                print("That website is not saved.")

         elif choice == 3:
            website_delete = input("What website password do you want to delete?: ").lower()

            cursor.execute(
                "SELECT * FROM passwords WHERE website = ?",
                (website_delete,)
            )

            result = cursor.fetchone()

            if result:
                cursor.execute(
                    "DELETE FROM passwords WHERE website = ?",
                    (website_delete,)
                )

                connection.commit()

                ("Password deleted!")

                input("\nPress Enter to continue...")

            else:
                print("That website is not saved.")

         elif choice == 4:
            website_edit = input("What website password do you want to edit?: ").lower()

            cursor.execute(
                "SELECT * FROM passwords WHERE website = ?",
                (website_edit,)
            )

            result = cursor.fetchone()

            if result:
                username = input("New username: ")
                length = int(input("New password length: "))

                password = generate_password(length)

                cursor.execute(
                    """
                    UPDATE passwords
                    SET username = ?, password = ?
                    WHERE website = ?
                    """,
                    (username, password, website_edit)
                )

                connection.commit()

                print("Password updated!")

                input("\nPress Enter to continue...")

            else:
                print("That website is not saved.")

         elif choice == 5:
            print("Goodbye!")
            return False
         else:
            print("Invalid option")

def main():
    while True:
        running = password_manager()

        if running == False:
            break

if __name__ == "__main__":
    main()
