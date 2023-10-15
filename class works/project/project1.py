import json

# Dictionary to store IT resources
resources = {
    'hardware': [],
    'software': [],
    'licenses': []
}


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


# Function to update resource information
def update_resource():
    resource_type = input("Enter resource type to update (hardware/software/licenses): ").strip().lower()
    name = input("Enter resource name to update: ").strip()
    quantity = get_valid_integer("Enter updated quantity: ")
    status = input("Enter updated status: ").strip()
    update_resource_data(resource_type, name, quantity, status)


# Function to update IT resource data
def update_resource_data(resource_type, name, quantity, status):
    for resource in resources[resource_type]:
        if resource['name'] == name:
            resource['quantity'] = quantity
            resource['status'] = status
            print("Resource information updated successfully.")
            return

    print("Resource not found.")


# Function to display IT resources
def display_resources():
    for resource_type, resource_list in resources.items():
        print(f"\n{resource_type.capitalize()} resources:")
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
    while True:
        print("\nIT Resource Management System\n")
        print("(A)dd IT resources")
        print("(U)pdate resources information")
        print("(D)isplay IT resources")
        print("(R)eport")
        print("(Q)uit")

        choice = input("Enter option: ").strip().lower()

        if choice == 'a':
            add_resource()

        elif choice == 'u':
            update_resource()

        elif choice == 'd':
            display_resources()

        elif choice == 'r':
            generate_report()

        elif choice == 'q':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
