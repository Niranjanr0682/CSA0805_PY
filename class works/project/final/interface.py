from functions import (add_resource, display_resource_names_by_type, load_data, update_resource, display_resources,
                       search_resource, generate_report, resource_statistics, clear_all_data, save_to_text_file)
import datetime


def hard_soft():
    print("\n"
          "________________________\n"
          "|    Resource type     |\n"
          "|______________________|\n"
          "| a) hardware          |\n"
          "| b) software          |\n"
          "|______________________|\n")


def main():
    print('\nwelcome to the world of IT resource management "mame"')
    now = datetime.datetime.now()
    load_data()
    print("date : ", now.date(), "\ttime : ", now.time())
    while True:
        print("\n"
              "_________________________________________________\n"
              "|         IT Resource Management System         |\n"
              "|_______________________________________________|\n"
              "| (A)Add IT resources                           |\n"
              "| (U)Update resources information               |\n"
              "| (D)Display IT resources                       |\n"
              "| (S)Search for a resource                      |\n"
              "| (V)View different resources                   |\n"
              "| (R)Report                                     |\n"
              "| (T)Total resources statistics                 |\n"
              "| (M)make text file of data                     |\n"
              "| (C)Clear all data                             |\n"
              "| (Q)Quit                                       |\n"
              "|_______________________________________________|\n")

        choice = input("Enter option: ").strip().lower()
        if choice == 'a':
            hard_soft()
            add_resource()
            print("\n"
                  "_______________________________\n"
                  "| Resource added successfully |\n"
                  "|_____________________________|\n")
        elif choice == 'u':
            #hard_soft()
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
        elif choice == 'v':
            hard_soft()
            display_resource_names_by_type()
        elif choice == 'm':
            save_to_text_file()
        elif choice == 'q':
            print("\nthank you for Using ><")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
