# it_resource_management.py

import os
import json

DATA_FILE = 'it_resource_data.json'

# Dictionary to store IT resources
resources = {
    'hardware': [],
    'software': []
}


def load_data():
    global resources
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            resources = json.load(file)


def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(resources, file, indent=4)


def save_to_text_file():
    with open('it_resource_summary.txt', 'w') as file:
        file.write("IT Resource Summary\n")
        file.write("====================\n\n")
        for resource_type, resource_list in resources.items():
            file.write(f"{resource_type.capitalize()} resources:\n")
            file.write("ID | Resource Name       | Quantity | Status\n")
            for resource in resource_list:
                file.write(
                    f"{resource['id']:2d} | {resource['name'][:20]:<20} | {resource['quantity']:8} | {resource['status'][:20]:<20}\n")
            file.write("\n")


def add_resource():
    resource_type = input("Enter resource type (hardware/software): ").strip().lower()
    name = input("Enter resource name: ").strip()

    while True:
        try:
            resource_id = int(input("Enter resource ID: "))
            if not is_id_unique(resource_id, resource_type):
                print("ID already exists. Please choose a different ID.")
            else:
                break
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")

    quantity = get_valid_integer("Enter quantity: ")
    status = input("Enter status: ").strip()

    add_resource_data(resource_type, resource_id, name, quantity, status)


# Function to check if the ID is unique
def is_id_unique(resource_id, resource_type):
    for resource in resources[resource_type]:
        if resource['id'] == resource_id:
            return False
    return True


def add_resource_data(resource_type, resource_id, name, quantity, status):
    resource = {'id': resource_id, 'name': name, 'quantity': quantity, 'status': status}
    resources[resource_type].append(resource)
    print("Resource added successfully.")
    save_data()


def update_resource():
    resource_type = input("Enter resource type (hardware/software): ").strip().lower()
    name = input("Enter resource name to update: ").strip()
    quantity = get_valid_integer("Enter updated quantity: ")
    status = input("Enter updated status: ").strip()
    update_resource_data(resource_type, name, quantity, status)


def update_resource_data(resource_type, name, quantity, status):
    for resource in resources[resource_type]:
        if resource['name'] == name:
            resource['quantity'] = quantity
            resource['status'] = status
            print("Resource information updated successfully.")
            save_data()
            return

    print("Resource not found.")


def remove_resource(resource_type, name):
    global resources
    resource_list = resources[resource_type]
    resources[resource_type] = [resource for resource in resource_list if resource['name'] != name]
    print("Resource removed successfully.")
    save_data()


def search_resource(name):
    found = False
    for resource_type, resource_list in resources.items():
        for resource in resource_list:
            if resource['name'] == name:
                print(f"Resource found in {resource_type.capitalize()} resources:")
                print(
                    f"ID: {resource['id']}, Name: {resource['name']}, Quantity: {resource['quantity']}, Status: {resource['status']}")
                found = True
    if not found:
        print("Resource not found.")


def display_resources():
    print("╔══════════════════════════════════════════════╗")
    print("║           IT Resource Summary                   ║")
    print("╠══════════════════════════════════════════════╣")
    print("║  Type  ║  ID  ║ Resource Name       | Quantity | Status              ║")
    print("╠════════╬══════╬═════════════════════╪══════════╪════════════════════╣")
    for resource_type, resource_list in resources.items():
        print(f"║ {resource_type.capitalize()} resources:")
        for resource in resource_list:
            print(
                f"║ {resource_type[:1].upper():<7} ║ {resource['id']:4d} ║ {resource['name'][:20]:<20} | {resource['quantity']:8} | {resource['status'][:20]:<20} ║")
        print("╠════════╧══════╧═════════════════════╧══════════╧════════════════════╣")
    print("╚══════════════════════════════════════════════╝")


def generate_report():
    report_data = {
        'hardware': resources['hardware'],
        'software': resources['software']
    }

    with open('report.json', 'w') as file:
        json.dump(report_data, file, indent=4)

    print("Report generated and saved to report.json.")


def resource_statistics():
    print("Total resources statistics")
    print("==========================")
    for resource_type, resource_list in resources.items():
        print(f"Total {resource_type.capitalize()} resources: {len(resource_list)}")


def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Quantity cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


def clear_all_data():
    global resources
    resources = {
        'hardware': [],
        'software': []
    }
    print("All data cleared.")
    save_data()


def main():
    load_data()  # Load existing data

    while True:
        print("\n╔══════════════════════════════════════════════╗")
        print("║         IT Resource Management System         ║")
        print("╠═══════════════════════════════════════════════╣")
        print("║ (A)dd IT resources                            ║")
        print("║ (U)pdate resources information                ║")
        print("║ (D)isplay IT resources                        ║")
        print("║ (S)earch for a resource                       ║")
        print("║ (R)eport                                      ║")
        print("║ (T)otal resources statistics                  ║")
        print("║ (C)lear all data                              ║")
        print("║ (Q)uit                                        ║")
        print("╚═══════════════════════════════════════════════╝")

        choice = input("Enter option: ").strip().lower()

        if choice == 'a':
            add_resource()
        elif choice == 'u':
            update_resource()
        elif choice == 'd':
            display_resources()
        elif choice == 's':
            resource_name = input("Enter resource name to search: ").strip()
            search_resource(resource_name)
        elif choice == 'r':
            generate_report()
        elif choice == 't':
            resource_statistics()
        elif choice == 'c':
            clear_all_data()
        elif choice == 'q':
            save_to_text_file()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
