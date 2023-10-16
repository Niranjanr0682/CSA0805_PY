from functions import (add_resource, display_resource_names_by_type, load_data, update_resource, display_resources,
 remove_resource_by_type, search_resource, generate_report, resource_statistics, clear_all_data, save_to_text_file,
                       display_resources_by_status)
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
              "| (a)Add IT resources                           |\n"
              "| (b)Update resources information               |\n"
              "| (C)Display IT resources                       |\n"
              "| (D)Search for a resource                      |\n"
              "| (E)Remove a resource                          |\n"
              "| (F)View different resources                   |\n"
              "| (G)Total resources statistics                 |\n"
              "| (K)Sort by status                             |\n"
              "| (H)Report                                     |\n"
              "| (I)make text file of data                     |\n"
              "| (J)Clear all data                             |\n"
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
        elif choice == 'b':
            update_resource()
        elif choice == 'c':
            display_resources()
        elif choice == 'd':
            resource_name = input("Enter resource name to search: ").strip()
            search_resource(resource_name)
        elif choice == 'e':
            hard_soft()
            remove_resource_by_type()
        elif choice == 'f':
            hard_soft()
            display_resource_names_by_type()
        elif choice == 'g':
            resource_statistics()
        elif choice == 'k':
            display_resources_by_status()
        elif choice == 'h':
            generate_report()
        elif choice == 'i':
            save_to_text_file()
        elif choice == 'j':
            clear_all_data()
        elif choice == 'q':
            print("\nthank you for Using ><")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
