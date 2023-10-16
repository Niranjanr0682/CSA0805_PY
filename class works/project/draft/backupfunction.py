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
        file.write("IT Resource Summary\n")
        file.write("____________________\n\n")
        for resource_type, resource_list in resources.items():
            file.write(f"{resource_type.capitalize()} resources:\n")
            file.write("ID | Resource Name       | Quantity | Status\n")
            for resource in resource_list:
                file.write(
                    f"{resource['id']:20} | {resource['name'][:20]:<20} | "
                    f"{resource['quantity']:8} | {resource['status'][:20]:<20}\n")
            file.write("\n")


def add_resource():
    resource_type = get_resource_type()
    name = input("Enter resource name: ").strip()
    while True:
        resource_id = input("Enter resource ID: ")
        if not is_id_unique(resource_id, resource_type):
            print("ID already exists. Please choose a different ID.")
        else:
            break
    quantity = get_valid_integer("Enter quantity: ")
    status = input("Enter status: ").strip()
    add_resource_data(resource_type, resource_id, name, quantity, status)


def add_resource_data(resource_type, resource_id, name, quantity, status):
    resource = {'id': resource_id, 'name': name, 'quantity': quantity, 'status': status}
    resources[resource_type].append(resource)
    save_data()


def is_id_unique(resource_id, resource_type):
    for resource in resources[resource_type]:
        if resource['id'] == resource_id:
            return False
    return True


def update_resource():
    resource_type = get_resource_type()
    name = input("Enter resource name to update: ").strip()
    quantity = get_valid_integer("Enter updated quantity: ")
    status = input("Enter updated status: ").strip()
    update_resource_data(resource_type, name, quantity, status)


def update_resource_data(resource_type, name, quantity, status):
    for resource in resources[resource_type]:
        if resource['name'] == name:
            resource['quantity'] = quantity
            resource['status'] = status
            print("_____________________________________________")
            print("| Resource information updated successfully |")
            print("|___________________________________________|")
            save_data()
            return
    print("______________________")
    print("| Resource not found |")
    print("|____________________|")


def search_resource(name):
    found = False
    for resource_type, resource_list in resources.items():
        for resource in resource_list:
            if resource['name'] == name:
                print("____________________________________________________________________")
                print(f"| Resource found in {resource_type.capitalize()} resources: {"":<25}  |")
                print("|__________________________________________________________________|")
                print("|   ID   |     Resource Name     | Quantity |        Status        |")
                print("|__________________________________________________________________|")
                print(
                    f"|{resource['id']:<8}|{resource['name']:<22} "
                    f"|{resource['quantity']:<10}| {resource['status']:<21}|")
                print("|__________________________________________________________________|")
                found = True
    if not found:
        print("Resource not found.")


def display_resources():
    print("________________________________________________________________________")
    print("|                          IT Resource Summary                         |")
    print("|______________________________________________________________________|")
    print("|  Type  |  ID  |    Resource Name    | Quantity |       Status        |")
    print("|______________________________________________________________________|")
    for resource_type, resource_list in resources.items():
        print(f"|{resource_type.capitalize()} resources:{"":<51}|")
        for resource in resource_list:
            print(f"| {resource_type[:1].upper():<6} | {resource['id']:4} | {resource['name'][:20]:<19} "
                  f"| {resource['quantity']:8} | {resource['status'][:20]:<19} |")
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


def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Quantity cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


def get_resource_type():
    while True:
        resource_type_choice = input("Enter resource type : ").strip()
        if resource_type_choice == 'a':
            return 'hardware'
        elif resource_type_choice == 'b':
            return 'software'
        else:
            print("Invalid choice. Please enter 'a' for hardware or 'b' for software.")


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
