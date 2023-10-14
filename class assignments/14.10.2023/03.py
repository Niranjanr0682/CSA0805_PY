# Write a program that takes a list of dictionaries, where each dictionary represents a
# person with keys 'name' and 'age'. Calculate and display the average age of all the
# people in the list.

def calculate_average_age(people):
    total_age = 0
    number_of_people = 0
    for person in people:
        total_age += person["age"]
        number_of_people += 1
    average_age = total_age / number_of_people
    return average_age


people1 = [{"name": "niranjan", "age": 25},
           {"name": "santhosh", "age": 30},
           {"name": "dinesh", "age": 27},
           {"name": "sridev", "age": 28},
           {"name": "jeeva", "age": 29}, ]
average_age1 = calculate_average_age(people1)
print(f"The average age of all the people is {average_age1: .2f} years old.")
