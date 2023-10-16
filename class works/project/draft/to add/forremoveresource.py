def remove_resource_by_type():
    # print("Select resource type:")
    # print("1. Hardware")
    # print("2. Software")
    # resource_type_choice = input("Enter your choice (1 or 2): ").strip()
    #
    # if resource_type_choice == '1':
    #     resource_type = 'hardware'
    # elif resource_type_choice == '2':
    #     resource_type = 'software'
    # else:
    #     print("Invalid choice. Please enter '1' for hardware or '2' for software.")
    #     return

    print(f"\nResources in {resource_type.capitalize()}")
    print("==============================")

    for resource in resources[resource_type]:
        print(f"ID: {resource['id']}, Name: {resource['name']}")

    while True:
        try:
            resource_id_to_remove = int(input("Enter the ID of the resource to remove: ").strip())
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