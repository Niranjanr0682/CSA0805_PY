import json
import os

# File to store IT resource data
DATA_FILE = 'it_resource_data.json'

# Dictionary to store IT resources
resources = {
    'hardware': [],
    'software': [],
    'licenses': []
}


# Load data from a JSON file
def load_data():
    global resources
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            resources = json.load(file)


# Save data to a JSON file
def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(resources, file, indent=4)


# Function to clear all data
def clear_all_data():
    global resources
    resources = {
        'hardware': [],
        'software': [],
        'licenses': []
    }
    print("All data cleared.")
    save_data()


# Function to add IT resources
def add_resource():
    resource_type = input("Enter resource type (hardware/software/licenses): ").strip().lower()
    name = input("Enter resource name: ").strip()
    quantity = get_valid_integer("Enter quantity: ")
    status = input("Enter status: ").strip()
    add_resource_data(resource_type, name, quantity, status)


# Function to add IT resource data
def add_resource_data(resource_type, name, quantity, status):
    resource = {'name': name, 'quantity': quantity, 'status': status}
    resources[resource_type].append(resource)
    print("Resource added successfully.")
    save_data()


# Function to update IT resource data
def update_resource_data(resource_type, name, quantity, status):
    for resource in resources[resource_type]:
        if resource['name'] == name:
            resource['quantity'] = quantity
            resource['status'] = status
            print("Resource information updated successfully.")
            save_data()
            return

    print("Resource not found.")


# Function to remove a resource
def remove_resource(resource_type, name):
    global resources
    resource_list = resources[resource_type]
    resources[resource_type] = [resource for resource in resource_list if resource['name'] != name]
    print("Resource removed successfully.")
    save_data()


# Function to search for a resource
def search_resource(name):
    found = False
    for resource_type, resource_list in resources.items():
        for resource in resource_list:
            if resource['name'] == name:
                print(f"Resource found in {resource_type.capitalize()} resources: ")
                print(f"Name: {resource['name']}, Quantity: {resource['quantity']}, Status: {resource['status']}")
                found = True
    if not found:
        print("Resource not found.")


# Function to display IT resources
def display_resources():
    for resource_type, resource_list in resources.items():
        print(f"\n{resource_type.capitalize()} resources: ")
        for resource in resource_list:
            print(f"Name: {resource['name']}, Quantity: {resource['quantity']}, Status: {resource['status']}")


# Function to generate a report
def generate_report():
    report_data = {
        'hardware': resources['hardware'],
        'software': resources['software'],
        'licenses': resources['licenses']
    }

    with open('report.json', 'w') as file:
        json.dump(report_data, file, indent=4)

    print("Report generated and saved to report.json.")


# Function to display resource statistics
def resource_statistics():
    total_resources = sum(len(resource_list) for resource_list in resources.values())
    print("Total number of resources:", total_resources)
    for resource_type, resource_list in resources.items():
        print(f"Total {resource_type.capitalize()} resources: ", len(resource_list))


# Function to display a resource summary report
def resource_summary_report():
    print("Resource Summary Report")
    for resource_type, resource_list in resources.items():
        print(f"\n{resource_type.capitalize()} resources: ")
        total_quantity = sum(resource['quantity'] for resource in resource_list)
        print(f"Total {resource_type.capitalize()} resources: {total_quantity}")


# Input validation for integer inputs
def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Quantity cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


# Sample usage
def main():
    load_data()  # Load existing data

    while True:
        print("\nIT Resource Management System\n")
        print("(a)Add IT resources")
        print("(b)Update resources information")
        print("(c)Display IT resources")
        print("(d)Search for a resource")
        print("(e)Report")
        print("(f)Total resources statistics")
        print("(g)Clear all data")
        print("(h)Quit")

        choice = input("Enter option: ").strip().lower()

        if choice == 'a':
            add_resource()
        elif choice == 'b':
            update_resource_data()
        elif choice == 'c':
            display_resources()
        elif choice == 'd':
            resource_name = input("Enter resource name to search: ").strip()
            search_resource(resource_name)
        elif choice == 'e':
            generate_report()
        elif choice == 'f':
            resource_statistics()
        elif choice == 'g':
            clear_all_data()
        elif choice == 'h':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
     main()
