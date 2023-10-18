import json
import os
import string

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
        file.write("_________________________________________________________________________________\n")
        file.write("|                              IT Resource Summary                              |\n")
        file.write("|_______________________________________________________________________________|\n")
        file.write("|  Type  |  ID  |    Resource Name    |    status    |      description         |\n")
        file.write("|_______________________________________________________________________________|\n")
        for resource_type, resource_list in resources.items():
            file.write(f"|{resource_type.capitalize()} resources:{"":<60}|\n")
            for resource in resource_list:
                file.write(f"| {resource_type[:1].upper():^6} | {resource['id']:^4} | {resource['name'][:20]:^19} "
                           f"| {resource['status']:^12} | {resource['description'][:20]:^23} |\n")
            file.write("|_______________________________________________________________________________|\n")
    print("__________________________________")
    print("| text file created successfully |")
    print("|________________________________|")


def add_resource():
    resource_type = get_resource_type()
    while True:
        name = get_non_empty_input("Enter resource name: ").strip()
        if is_valid_name(name):
            break
    quantity = get_valid_integer("Enter quantity: ")
    if quantity > 1:
        status = get_non_empty_input("Enter status: ").strip()
        description = get_non_empty_input("Enter resource description: ").strip()
        for i in range(quantity):
            while True:
                resource_id = get_non_empty_input(f"Enter resource ID for item {i + 1}: ").strip()
                if not is_id_unique(resource_id, resource_type):
                    print("ID already exists. Please choose a different ID.")
                else:
                    add_resource_data(resource_type, resource_id, name, status, description)
                    break
        print("\n"
              "_______________________________\n"
              "| Resource added successfully |\n"
              "|_____________________________|\n")
    else:
        while True:
            resource_id = get_non_empty_input("Enter resource ID: ")
            if not is_id_unique(resource_id, resource_type):
                print("ID already exists. Please choose a different ID.")
            else:
                break
        status = get_non_empty_input("Enter resource status: ").strip()
        description = get_non_empty_input("Enter resource description: ").strip()
        print("\n"
              "_______________________________\n"
              "| Resource added successfully |\n"
              "|_____________________________|\n")
        add_resource_data(resource_type, resource_id, name, status, description)


def add_resource_data(resource_type, resource_id, name, status, description):
    resource = {'id': resource_id, 'name': name, 'status': status, 'description': description}
    resources[resource_type].append(resource)
    save_data()


def update_resource():
    while True:
        try:
            resource_id_to_update = get_non_empty_input("Enter the ID of the resource to update: ").strip()
            found = False
            for resource_type, resource_list in resources.items():
                for resource in resource_list:
                    if resource['id'] == resource_id_to_update:
                        print(f"Resource Name: {resource['name']}")
                        print(f"Current Status: {resource['status']}")
                        print(f"Current Description: {resource['description']}")
                        status = get_non_empty_input("Enter new status: ")
                        new_description = input(
                            "Enter new resource description (press Enter to keep current): ").strip()
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
        print("________________________________________________________________________")
        print(f"| Resource found in {resource_type.capitalize()}:{"":<40}  |")
        print("|______________________________________________________________________|")
        print("|   ID   |     Resource Name     |   status   |       description      |")
        print("|______________________________________________________________________|")
        for resource in resource_list:
            if resource['name'] == name:
                print(
                    f"|{resource['id']:^8}|{resource['name']:^22} "
                    f"|{resource['status']:^12}| {resource['description']:^23}|")
                found = True
        print("|______________________________________________________________________|")
    if not found:
        print("Resource not found.")


def display_resources():
    print("_________________________________________________________________________________")
    print("|                               IT Resource Summary                             |")
    print("|_______________________________________________________________________________|")
    print("|  Type  |  ID  |    Resource Name    |    status    |       description        |")
    print("|_______________________________________________________________________________|")
    for resource_type, resource_list in resources.items():
        print(f"|{resource_type.capitalize()} resources:{"":<60}|")
        for resource in resource_list:
            print(f"| {resource_type[:1].upper():^6} | {resource['id']:^4} | {resource['name'][:20]:^19} "
                  f"| {resource['status']:^12} | {resource['description']:^23} |")
        print("|_______________________________________________________________________________|")


def display_resource_names_by_type():
    resource_type = get_resource_type()

    unique_names = set()
    for resource in resources[resource_type]:
        unique_names.add(resource['name'])

    for name in unique_names:
        print(f"-> {name}")


def remove_resource_by_type():
    resource_type = get_resource_type()
    print(f"\nResources in {resource_type.capitalize()}")
    print("______________________________")
    for resource in resources[resource_type]:
        print(f"ID: {resource['id']}, Name: {resource['name']}")
    while True:
        try:
            resource_id_to_remove = get_non_empty_input("Enter the ID of the resource to remove: ").strip()
            found = False
            for resource in resources[resource_type]:
                if resource['id'] == resource_id_to_remove:
                    found = True
                    print(f"Removing {resource['name']} from {resource_type.capitalize()}...")
                    resources[resource_type].remove(resource)
                    save_data()
                    print("Resource removed successfully.")
                    break
            if not found:
                print("Invalid resource ID. Please try again.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the resource ID.")
        break


def display_resources_by_status():
    status = get_non_empty_input("Enter status to sort: ").strip().lower()
    found = False
    for resource_type, resource_list in resources.items():
        print(f"Resources with status '{status.capitalize()}' on {resource_type} :                 ")
        print("___________________________________________________________")
        print("|   ID   |    Resource Name    |       description        |")
        print("|_________________________________________________________|")
        for resource in resource_list:
            if resource['status'].lower() == status:
                print(
                    f"|{resource['id']:^8}|{resource['name']:^20} "
                    f"|{resource['description']:^26}|")
                print("|_________________________________________________________|")
                found = True
    if not found:
        print("No resources found with the specified status.")


def generate_report():
    report_data = {
        'hardware': resources['hardware'],
        'software': resources['software']
    }
    with open('report.json', 'w') as file:
        json.dump(report_data, file, indent=4)
    print("Report generated and saved to report.json.")


def resource_statistics():
    print("__________________________________")
    print("|   Total resources statistics   |")
    print("|________________________________|")
    for resource_type, resource_list in resources.items():
        print(f"|  Total {resource_type.capitalize()} resources: {len(resource_list):^4}|")
        print("|________________________________|")


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
        except ValueError:
            print(f"Invalid input: enter valid number ")


def is_valid_name(name):
    if all(char in string.ascii_letters + ' ' for char in name):
        return True
    print("invalid character used. Please enter valid name")
    return False


def is_id_unique(resource_id, resource_type):
    for resource in resources[resource_type]:
        if resource['id'] == resource_id:
            return False
    return True


def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")


# def check_for_exit(user_input):
#     return user_input.lower() == 'exit'


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
