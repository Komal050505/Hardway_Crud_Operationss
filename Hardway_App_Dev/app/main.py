"""
from Hardway_App_Dev.utils.user_utils import *
from constants import *  # * means import everything in the constants file

print("Please enter the PROFILE info: ")

total_users = int(input("How many users you want to enter:")) # 2

for item in range(total_users): # range(4) => [0, 1]
    print(f"SAVED_RECORDS is {SAVED_RECORDS}")
    print(f"Please enter {item+1} user details: ")
    PROFILE = {}
    PROFILE["mob"] = int(input("Mobile:"))
    if PROFILE["mob"] in REGISTERED_USERS:  # "9848000023" in [9848000023, 675424242]
        print("Mobile Number verified successfully:")
        PROFILE["name"] = input("Name:")
        if is_valid_name(PROFILE["name"], mobile=PROFILE["mob"]):
            PROFILE["dob"] = input("Date Of Birth:")  or "12-08-1990"
            PROFILE["email"] = input("Email:")

            PROFILE["blood_group"] = input("Blood Group:") or "A+"
            if PROFILE["blood_group"].upper() in VALID_BLOOD_GROUP:
                pass
            else:
                raise ValueError(f'Incorrect blood group {PROFILE["blood_group"]}')
            PROFILE["gender"] = input("Gender:") or "Others"
            # PROFILE["address"]["street"] = input("Street Name:") # Str
            # PROFILE["address"]["city"] = input("City:") # Str
            # PROFILE["address"]["state"] = input("State:") # Str
            # PROFILE["address"]["pin"] = input("Pin Code:") # Must be int

            print(f'PROFILE saved successfully for mobile number {PROFILE["mob"]}')

            SAVED_RECORDS.append(PROFILE)
        else:
            print(f'Incorrect {PROFILE["mob"]}')

print(SAVED_RECORDS)
"""

from Hardway_App_Dev.utils.user_utils import is_valid_name
from constants import *  # Importing everything from the constants file

print("Please enter the PROFILE info:")

total_users = int(input("How many users you want to enter: "))  # For example, 2

for item in range(total_users):  # Iterating through the number of users
    print(f"SAVED_RECORDS is {SAVED_RECORDS}")
    print(f"Please enter details for user {item + 1}:")
    PROFILE = {}

    # Mobile number validation
    PROFILE["mob"] = int(input("Mobile: "))
    if PROFILE["mob"] in REGISTERED_USERS:
        print("Mobile Number verified successfully:")

        # Name validation
        PROFILE["name"] = input("Name: ")
        if is_valid_name(PROFILE["name"], mobile=PROFILE["mob"]):
            PROFILE["dob"] = input("Date Of Birth (default: 12-08-1990): ") or "12-08-1990"
            PROFILE["email"] = input("Email: ")

            # Blood group validation
            PROFILE["blood_group"] = input("Blood Group (default: A+): ") or "A+"
            if PROFILE["blood_group"].upper() not in VALID_BLOOD_GROUP:
                raise ValueError(f'Incorrect blood group {PROFILE["blood_group"]}')

            PROFILE["gender"] = input("Gender (default: Others): ") or "Others"

            # Address input (uncomment if needed)
            # PROFILE["address"] = {}
            # PROFILE["address"]["street"] = input("Street Name: ")
            # PROFILE["address"]["city"] = input("City: ")
            # PROFILE["address"]["state"] = input("State: ")
            # PROFILE["address"]["pin"] = int(input("Pin Code: "))  # Must be int

            print(f'PROFILE{PROFILE} saved successfully for mobile number {PROFILE["mob"]}')
            SAVED_RECORDS.append(PROFILE)
        else:
            print(f'Invalid name for mobile number {PROFILE["mob"]}')
    else:
        print(f'Mobile number {PROFILE["mob"]} is not registered.')

print("All saved profiles:", SAVED_RECORDS)





