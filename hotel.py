import os
import random

def calculate_bill(room_type, number_of_days, tax, bill):
    tax = tax /100
    if room_type == "ac":
        bill += 6000 * number_of_days
    elif room_type == "non-ac":
        bill += 4000 * number_of_days
    else:
        return None
    bill += bill * tax
    return bill

customer_id = []
customer_name = []
ac_room = []
nonac_room = []
booked_room = []

for i in range(1, 501):
    nonac_room.append(i)
for j in range(501, 1001):
    ac_room.append(j)

while True:
    print(f"\n-----WELCOME TO OUR HOTEL-----\n")
    print(f"1. Book a Room\n2. Check-Out\n3. Total Bill\n4. Save All Data\n5. Exit\n")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter your name: ")
            customer_name.append(name)
            id = input("Enter your ID: ")
            customer_id.append(id)
            room_type = input("Which type of room you wanted(AC/Non-AC): ").lower()
            if room_type == "ac":
                room_no = random.choice(ac_room)
                ac_room.remove(room_no)
                booked_room.append(room_no)
                print(f"Your Room No. is {room_no}")
            elif room_type == "non-ac":
                room_no = random.choice(nonac_room)
                nonac_room.remove(room_no)
                booked_room.append(room_no)
                print(f"Your Room No. is {room_no}")
            else:
                print(f"Please enter a valid room type!")

        case 2:
            room_no = int(input("Enter your room no for check out: "))
            if room_no in booked_room:
                booked_room.remove(room_no)
                if room_no in range(1, 501):
                    nonac_room.append(room_no)
                elif room_no in range(501, 1001):
                    ac_room.append(room_no)
                print(f"Check out successfully!")
            else:
                print(f"Please enter your booked room no!")

        case 3:
            room_type = input("Which type of room you wanted(AC/Non-AC): ").lower()
            tax = 15
            bill = 0.0
            number_of_days = int(input("Enter number of days: "))
            bill = calculate_bill(room_type, number_of_days, tax, bill)
            print(f"Your total bill is {bill}Rs.")

        case 4:
            with open("data.txt", "a") as new_file:
                for i in range(len(customer_name)):
                    new_file.write(f"Customer Name: {customer_name[i]}, Customer ID: {customer_id[i]}\n")
                
            with open("data.txt") as file:
                print(file.read())
        
        case 5:
            break

        case _:
            print(f"Please enter a valid choice!")