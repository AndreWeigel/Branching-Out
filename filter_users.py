import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == int(age)]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] .lower() == email.lower()]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('name' or 'age' or 'email'): ").strip().lower()

    if filter_option == "name":
        search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(search)
    elif filter_option == "age":
        search = input("Enter a age to filter users: ").strip()
        filter_users_by_age(search)
    elif filter_option == "email":
        search = input("Enter a email to filter users: ").strip()
        filter_users_by_email(search)
    else:
        print("Filtering by that option is not yet supported.")
