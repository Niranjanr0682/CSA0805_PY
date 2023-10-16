import json
import os

DATA_FILE = 'it_resource_data.json'
resources = {
    'hardware': [],
    'software': []
}


def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(resources, file, indent=4)


def load_data():
    global resources
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            resources = json.load(file)


def save_to_text_file():
    with open('it_resource_summary.txt', 'w') as file:
        file.write("____________________________________________________________________________\n")
        file.write("|                            IT Resource Summary                           |\n")
        file.write("|__________________________________________________________________________|\n")
        file.write("|  Type  |  ID  |    Resource Name    |    status    |    description      |\n")
        file.write("|__________________________________________________________________________|\n")
        for resource_type, resource_list in resources.items():
            file.write(f"|{resource_type.capitalize()} resources:{"":<55}|\n")
            for resource in resource_list:
                file.write(f"| {resource_type[:1].upper():<6} | {resource['id']:4} | {resource['name'][:20]:<19} "
                           f"| {resource['status']:12} | {resource['description'][:20]:<19} |\n")
            file.write("|__________________________________________________________________________|\n")
    print("__________________________________")
    print("| text file created successfully |")
    print("|________________________________|")


def add_resource():
    resource_type = get_resource_type()
    name = input("Enter resource name: ").strip()
    quantity = get_valid_integer("Enter quantity: ")
    if quantity > 1:
        status = input("Enter status: ").strip()
        description = input("Enter resource description: ").strip()
        for i in range(quantity):
            while True:
                resource_id = input(f"Enter resource ID for item {i + 1}: ").strip()
                if not is_id_unique(resource_id, resource_type):
                    print("ID already exists. Please choose a different ID.")
                else:
                    add_resource_data(resource_type, resource_id, name, quantity, status, description)
                    break
        add_resource_data(resource_type, resource_id, name, quantity, status, description)
    else:
        while True:
            resource_id = input("Enter resource ID: ")
            if not is_id_unique(resource_id, resource_type):
                print("ID already exists. Please choose a different ID.")
            else:
                break
        status = input("Enter status: ").strip()
        description = input("Enter resource description: ").strip()
        add_resource_data(resource_type, resource_id, name, quantity, status, description)


def add_resource_data(resource_type, resource_id, name, quantity, status, description):
    resource = {'id': resource_id, 'name': name, 'quantity': quantity, 'status': status,'description': description}
    resources[resource_type].append(resource)
    save_data()


def is_id_unique(resource_id, resource_type):
    for resource in resources[resource_type]:
        if resource['id'] == resource_id:
            return False
    return True


def update_resource():
    while True:
        try:
            resource_id_to_update = (input("Enter the ID of the resource to update: ").strip())
            found = False
            for resource_type, resource_list in resources.items():
                for resource in resource_list:
                    if resource['id'] == resource_id_to_update:
                        found = True
                        print(f"Resource Name: {resource['name']}")
                        print(f"Current Description: {resource['description']}")
                        status = input("Enter status: ")
                        new_description = input(
                            "Enter new resource description (or press Enter to keep current): ").strip()
                        new_description = new_description if new_description else resource['description']
                        resource['status'] = status
                        resource['description'] = new_description
                        print("_____________________________________________")
                        print("| Resource information updated successfully |")
                        print("|___________________________________________|")
                        save_data()
                        return
            if not found:
                print("______________________")
                print("| Resource not found |")
                print("|____________________|")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the resource ID.")


def search_resource(name):
    found = False
    for resource_type, resource_list in resources.items():
        for resource in resource_list:
            if resource['name'] == name:
                print("____________________________________________________________________")
                print(f"| Resource found in {resource_type.capitalize()} resources: {"":<25}  |")
                print("|__________________________________________________________________|")
                print("|   ID   |     Resource Name     | status |       description      |")
                print("|__________________________________________________________________|")
                print(
                    f"|{resource['id']:<8}|{resource['name']:<22} "
                    f"|{resource['status']:<10}| {resource['description']:<21}|")
                print("|__________________________________________________________________|")
                found = True
    if not found:
        print("Resource not found.")


def display_resources():
    print("________________________________________________________________________")
    print("|                          IT Resource Summary                         |")
    print("|______________________________________________________________________|")
    print("|  Type  |  ID  |    Resource Name    |  status  |    description      |")
    print("|______________________________________________________________________|")
    for resource_type, resource_list in resources.items():
        print(f"|{resource_type.capitalize()} resources:{"":<51}|")
        for resource in resource_list:
            print(f"| {resource_type[:1].upper():<6} | {resource['id']:4} | {resource['name'][:20]:<19} "
                  f"| {resource['status']:<8} | {resource['description']:<19} |")
        print("|______________________________________________________________________|")
    # print("________________________________________________________________________")


def display_resource_names_by_type():
    resource_type = get_resource_type()

    unique_names = set()
    for resource in resources[resource_type]:
        unique_names.add(resource['name'])

    for name in unique_names:
        print(name)


def generate_report():
    report_data = {
        'hardware': resources['hardware'],
        'software': resources['software']
    }
    with open('report1.json', 'w') as file:
        json.dump(report_data, file, indent=4)
    print("Report generated and saved to report.json.")


def resource_statistics():
    print("________________________________")
    print("|  Total resources statistics  |")
    print("|______________________________|")
    for resource_type, resource_list in resources.items():
        print(f"|Total {resource_type.capitalize()} resources: {len(resource_list):<4}|")
        print("|______________________________|")


def get_resource_type():
    while True:
        resource_type_choice = input("Enter resource type : ").strip()
        if resource_type_choice == 'a':
            return 'hardware'
        elif resource_type_choice == 'b':
            return 'software'
        else:
            print("Invalid choice. Please enter 'a' for hardware or 'b' for software.")


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
    print("____________________")
    print("| All data cleared |")
    print("|__________________|")
    save_data()
