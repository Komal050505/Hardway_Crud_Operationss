
import logging
# DATABASE RECORD
data = {"records": [{"mobile": 914234234245, "name": "Kumar Makala", "company": "KXN"},
                    {"mobile": 915421215452, "name": "Komal", "company": "APPLE"},
                    {"mobile": 913020022100, "name": "Mahesh", "company": "MICROSOFT"},
                    {"mobile": 910000000000, "name": "Rajesh", "company": "WIPRO"},
                    {"mobile": 914111111111, "name": "Suresh", "company": "MIND TREE"}]}


# POST
# User1
# User sign up - Insert the new record in the database
# data["records"].append({"mobile":12345, "name":"Kumar Makala", "company": "KXN"})

# MOBILE VALIDATION
def is_valid_mobile(mobile):

    if isinstance(mobile, int):
        converted_str = str(mobile)
        if len(converted_str) == 12:
            if converted_str[:2] == "91":
                logging.info("Mobile verification is successful")
                # print("Mobile verification is successfull")
                return True
            else:
                raise ValueError(f"Invalid country code - {converted_str[:2]}")
        else:
            raise ValueError(f"Invalid mobile number - {mobile}")
