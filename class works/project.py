# Data structure to store IT resources
resources = []


# Function to add IT resources
def add_resource():
    name = input("Enter resource name: ")
    r_type = input("Enter resource type (Hardware/Software/License): ")
    quantity = int(input("Enter quantity: "))
    status = input("Enter status: ")

    resource = {"name": name, "type": r_type, "quantity": quantity, "status": status}
    resources.append(resource)


# Function to update IT resources
def update_resource():
    name = input("Enter the resource name you want to update: ")
    for resource in resources:
        if resource["name"] == name:
            resource["type"] = input("Enter new resource type: ")
            resource["quantity"] = int(input("Enter new quantity: "))
            resource["status"] = input("Enter new status: ")
            print("Resource updated.")
            return
    print("Resource not found.")


# Function to display IT resources
def display_resources():
    for resource in resources:
        print(
            f"Name: {resource['name']}, Type: {resource['type']}, Quantity: {resource['quantity']}, Status: {resource['status']}")


# Function to generate a report
def generate_report():
    print("IT Resource Report:")
    for resource in resources:
        print(
            f"Resource: {resource['name']}, Type: {resource['type']}, Quantity: {resource['quantity']}, Status: {resource['status']}")


# Main program
while True:
    print("\nIT Resource Management System")
    print("================================")
    print("(A)dd IT resources")
    print("(U)pdate resources information")
    print("(D)isplay IT resources")
    print("(R)eport")
    print("(E)xit")
    option = input("Enter option: ").upper()

    if option == "A":
        add_resource()
    elif option == "U":
        update_resource()
    elif option == "D":
        display_resources()
    elif option == "R":
        generate_report()
    elif option == "E":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")