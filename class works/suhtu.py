# print("\n"
#       "┌──────────────────────┐\n"
#       "│    Resource type     │\n"
#       "├──────────────────────┤\n"
#       "│ a) hardware          │\n"
#       "│ b) software          │\n"
#       "└──────────────────────┘\n")
#
#
#
#
#

# def display_unique_resource_names_by_type():
#     resource_type = get_resource_type()
#
#     unique_names = set()
#     for resource in resources[resource_type]:
#         unique_names.add(resource['name'])
#
#     for name in unique_names:
#         print(name)

# print(" __________________________________________")
# print("|Resource information updated successfully |")
# print("|__________________________________________|")
#
# print("____________________________________________")
# print("|Resource information updated successfully |")
# print("|__________________________________________|")

# functions.py

# ... (other functions) ...
#
# def add_resource():
#     resource_type = get_resource_type()
#     name = input("Enter resource name: ").strip()
#     while True:
#         resource_id = input("Enter resource ID: ")
#         if not is_id_unique(resource_id, resource_type):
#             print("ID already exists. Please choose a different ID.")
#         else:
#             break
#     description = input("Enter resource description: ").strip()
#     status = input("Enter status")
#
#     try:
#         quantity = int(input("Enter quantity: "))
#         if quantity > 1:
#             for i in range(1, quantity + 1):
#                 resource_id_i = f"{resource_id}-{i}"
#                 add_resource_data(resource_type, resource_id_i, name, description, status)
#         else:
#             add_resource_data(resource_type, resource_id, name, description, status)
#     except ValueError:
#         print("Invalid input for quantity. Please enter a valid integer.")
#
# # ... (other functions) ...
#
# # functions.py
#
# # ... (other functions) ...
#
# def add_resource():
#     resource_type = get_resource_type()
#     while True:
#         try:
#             quantity = int(input("Enter quantity: "))
#             if quantity > 1:
#                 break
#             else:
#                 print("Quantity should be 1 or more.")
#         except ValueError:
#             print("Invalid input. Please enter a valid integer for quantity.")
#
#     for i in range(quantity):
#         while True:
#             resource_id = input(f"Enter resource ID for item {i + 1}: ").strip()
#             if not is_id_unique(resource_id, resource_type):
#                 print("ID already exists. Please choose a different ID.")
#             else:
#                 break
#
#         # Set status to "good" by default
#         status = input("Enter status: ")
#         description = input("Enter resource description: ").strip()
#         add_resource_data(resource_type, resource_id, status, description)
#
# # ... (other functions) ...
#
# def add_resource():
#     resource_type = get_resource_type()
#     name = input("Enter resource name: ").strip()
#     quantity = get_valid_integer("Enter quantity: ")
#     if quantity >1:
#         for i in range(quantity):
#             while True:
#                 resource_id = input(f"Enter resource ID for item {i + 1}: ").strip()
#                 if not is_id_unique(resource_id, resource_type):
#                     print("ID already exists. Please choose a different ID.")
#                 else:
#                     break
#         status = input("Enter status: ").strip()
#         description = input("Enter resource description: ").strip()
#     else:
#         while True:
#             resource_id = input("Enter resource ID: ")
#             if not is_id_unique(resource_id, resource_type):
#                 print("ID already exists. Please choose a different ID.")
#             else:
#                 break
#         status = input("Enter status: ").strip()
#         add_resource_data(resource_type, resource_id, name, quantity, status, description)
#
#
# def add_resource_data(resource_type, resource_id, name, quantity, status, description):
#     resource = {'id': resource_id, 'name': name, 'quantity': quantity, 'status': status,'description': description}
#     resources[resource_type].append(resource)
#     save_data()
#
#
# functions.py

# ... (other functions) ...
#
# def display_resources_by_status():
#     status = input("Enter status to sort: ").strip().lower()
#     found = False
#     print(f"\nResources with status '{status.capitalize()}'")
#     for resource_type, resource_list in resources.items():
#         print("__________________________________________________________________________")
#         print("|         f"\nResources with status '{status.capitalize()}'"             |")
#         print("|________________________________________________________________________|")
#         print("|  Type  |   ID   |    Resource Name    |  status  |    description      |")
#         print("|________________________________________________________________________|")
#         for resource in resource_list:
#             if resource['status'].lower() == status:
#                 print(
#                     f"|{resource_type[:1].upper():<6} |{resource['id']:<8}|{resource['name']:<22} "
#                     f"|{resource['status']:<10}| {resource['description']:<21}|")
#                 print("|____________________________________________________________________|")
#                 found = True
#     if not found:
#         print("No resources found with the specified status.")
#




