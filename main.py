import csv
import os

FILE_NAME = "volunteers.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Phone", "Skill"])


def add_volunteer():
    volunteer_id = input("Enter Volunteer ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    phone = input("Enter Phone Number: ")
    skill = input("Enter Skill: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([volunteer_id, name, age, phone, skill])

    print("\nVolunteer Added Successfully!\n")


def view_volunteers():
    print("\n--- Volunteer List ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    print()


def search_volunteer():
    search_name = input("Enter Volunteer Name: ").lower()

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 1 and search_name in row[1].lower():
                print(row)
                found = True

    if not found:
        print("Volunteer Not Found")


def generate_report():
    count = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            count += 1

    print("\n===== NayePankh Foundation Report =====")
    print("Total Volunteers:", count)
    print("=======================================\n")


while True:
    print("===== NayePankh Foundation =====")
    print("1. Add Volunteer")
    print("2. View Volunteers")
    print("3. Search Volunteer")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_volunteer()

    elif choice == "2":
        view_volunteers()

    elif choice == "3":
        search_volunteer()

    elif choice == "4":
        generate_report()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")