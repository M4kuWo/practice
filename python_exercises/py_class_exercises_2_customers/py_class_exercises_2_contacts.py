import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('customers.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')
conn.commit()

# Create Operation
def add_customer(name, email):
    try:
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Customer added successfully.")
    except sqlite3.IntegrityError:
        print("Error: A customer with this email already exists.")

# Read Operation
def view_customers():
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update Operation
def update_customer(customer_id, name, email):
    cursor.execute("UPDATE customers SET name = ?, email = ? WHERE id = ?", (name, email, customer_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("Error: Customer not found.")
    else:
        print("Customer updated successfully.")

# Delete Operation
def delete_customer(customer_id):
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Error: Customer not found.")
    else:
        print("Customer deleted successfully.")

# Display the menu
def display_menu():
    print("\nMenu:")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Update Customer")
    print("4. Delete Customer")
    print("5. Exit")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Please select an option (1-5): ")
        
        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            add_customer(name, email)
        
        elif choice == '2':
            view_customers()
        
        elif choice == '3':
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            update_customer(customer_id, name, email)
        
        elif choice == '4':
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option, please try again.")

# Run the main function
if __name__ == "__main__":
    main()

# Close the connection when done
conn.close()

