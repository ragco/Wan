# Define a class for managing personal information
class PersonalInformationManager:
    # Constructor to initialize the information dictionary
    def __init__(self):
        self.information = {}

    # Method to add information to the dictionary
    def add_information(self, key, value):
        self.information[key] = value
        print("Information added successfully!")

    # Method to view all information in the dictionary
    def view_information(self):
        # Check if there is any information available
        if self.information:
            print("Personal Information:")
            # Iterate over each key-value pair in the dictionary and print them
            for key, value in self.information.items():
                print(f"{key}: {value}")
        else:
            print("No information available.")

    # Method to update information in the dictionary
    def update_information(self, key, value):
        # Check if the key exists in the dictionary
        if key in self.information:
            # Update the value associated with the key
            self.information[key] = value
            print("Information updated successfully!")
        else:
            print("Key not found.")

    # Method to delete information from the dictionary
    def delete_information(self, key):
        # Check if the key exists in the dictionary
        if key in self.information:
            # Delete the key-value pair from the dictionary
            del self.information[key]
            print("Information deleted successfully!")
        else:
            print("Key not found.")

# Define the main function to interact with the PersonalInformationManager
def main():
    # Create an instance of PersonalInformationManager
    pim = PersonalInformationManager()
    while True:
        # Display menu options
        print("\n1. Add Information")
        print("2. View Information")
        print("3. Update Information")
        print("4. Delete Information")
        print("5. Exit")

        # Take user input for choice
        choice = input("Enter your choice: ")

        # Perform actions based on user choice
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            pim.add_information(key, value)
        elif choice == '2':
            pim.view_information()
        elif choice == '3':
            key = input("Enter key to update: ")
            value = input("Enter new value: ")
            pim.update_information(key, value)
        elif choice == '4':
            key = input("Enter key to delete: ")
            pim.delete_information(key)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

# Entry point of the program
if __name__ == "__main__":
    main()
