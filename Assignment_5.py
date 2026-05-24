import csv

with open("Assignment5..csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Address", "Mobile", "Email"])

    while True:
        print("\nEnter details:")
        name = input("Name: ")
        address = input("Address: ")
        mobile = input("Mobile: ")
        email = input("Email: ")

        writer.writerow([name, address, mobile, email])

        choice = input("Do you want to add another entry? (yes/no): ")
        if choice.lower() != "yes":
            break

print("CSV file saved successfully!")