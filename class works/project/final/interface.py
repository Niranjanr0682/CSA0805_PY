from functions import (add_resource, display_resource_names_by_type, load_data, update_resource, display_resources,
                       remove_resource_by_type, search_resource, generate_report, resource_statistics, clear_all_data,
                       save_to_text_file, get_non_empty_input,
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
    print('\nwelcome to the IT Resource Management System ')
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
              "| (c)Display IT resources                       |\n"
              "| (d)Search for a resource                      |\n"
              "| (e)Remove a resource                          |\n"
              "| (f)View different resources                   |\n"
              "| (g)Total resources statistics                 |\n"
              "| (h)Sort by status                             |\n"
              "| (i)Report                                     |\n"
              "| (j)make text file of data                     |\n"
              "| (k)Clear all data                             |\n"
              "| (q)Quit                                       |\n"
              "|_______________________________________________|\n")

        choice = get_non_empty_input("Enter option: ").strip().lower()
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
            resource_name = get_non_empty_input("\nEnter resource name to search: ").strip()
            search_resource(resource_name)
        elif choice == 'e':
            hard_soft()
            remove_resource_by_type()
        elif choice == 'f':
            hard_soft()
            display_resource_names_by_type()
        elif choice == 'g':
            resource_statistics()
        elif choice == 'h':
            display_resources_by_status()
        elif choice == 'i':
            generate_report()
        elif choice == 'j':
            save_to_text_file()
        elif choice == 'k':
            clear_all_data()
        elif choice == 'q':
            print("\nthank you for Using ><")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
