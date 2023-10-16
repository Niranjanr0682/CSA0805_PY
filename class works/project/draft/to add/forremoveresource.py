def remove_resource_by_type():
    resource_type = get_resource_type()
    print(f"\nResources in {resource_type.capitalize()}")
    print("==============================")
    for resource in resources[resource_type]:
        print(f"ID: {resource['id']}, Name: {resource['name']}")
    while True:
        try:
            resource_id_to_remove = input("Enter the ID of the resource to remove: ").strip()
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
        except ValueError:
            print("Invalid input. Please enter a valid integer for the resource ID.")



# def remove_resource(resource_type, name):
#     global resources
#     resource_list = resources[resource_type]
#     resources[resource_type] = [resource for resource in resource_list if resource['name'] != name]
#     print("Resource removed successfully.")
#     save_data()