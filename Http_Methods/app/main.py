from Http_Methods.utils.user_utils import *

import logging

# LOGGING MODULES
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a', filename='main.log')


# POST METHOD
def new_record(record):
    logging.debug(f"POST METHOD entered with record {record}")
    if isinstance(record, dict):

        if "mobile" in record:
            try:
                if is_valid_mobile(record["mobile"]):
                    data["records"].append(record)
                    response = {"message": "Successfully inserted into the record ", "record": record}
                    logging.info(f"Record successfully inserted using POST METHOD: {record}")
                    return response
            except ValueError as err:
                response = {"message": str(err), "status": "Failed"}
                logging.error(f"Error inserting record: {err} using POST METHOD")
                return response
        else:
            response = {"message": "Missing mobile key in the record", "status": "Failed"}
            logging.error("Missing mobile key in the record in POST METHOD.")
            return response
    else:
        response = {"message": f"Incorrect record type {type(record)}"}
        logging.error(f"Incorrect record type in POST METHOD: {type(record)}")
        return response


# print(new_record([1,2,3]))


print(new_record({"mobile": 914234123456, "name": "Queen", "company": "ABC"}))
print(data)


# GET METHOD
def get_user_details(record):
    logging.debug(f"GET METHOD entered with record {record}")
    # print(f"Get method entered with mobile number {record}")
    if isinstance(record, dict):
        if "mobile" in record:
            mobile = record["mobile"]

            try:
                if is_valid_mobile(record["mobile"]):
                    for user in data['records']:
                        if user["mobile"] == mobile:
                            logging.info(f"User details found -->> {user}")
                            # print(f"User details found -->> {user}")
                            return user
                    logging.warning(f"No user details found for mobile number in GET METHOD {mobile}"
                                    f" so GET METHOD will return nothing.")
                    # print(f"No user details found for mobile number {mobile}.")
                    return {"error": "User details not found"}
            except ValueError as err:
                logging.error(f"Error in GET METHOD: {err}")
                return {"error": str(err)}

        else:
            logging.error("Missing mobile key in the record in GET METHOD.")
            return {"error": "Missing mobile key in the record"}
    else:
        logging.error(f"Incorrect record type in GET METHOD {type(record)}.")
        return {"error": f"Incorrect record type {type(record)}"}


print(get_user_details({"mobile": 915421215452}))
print(f"Users are -->> {data}")


def delete_user_details(record):
    logging.debug(f"DELETE method entered with record {record}")
    # print(f"DELETE method entered with mobile number {record}")
    if isinstance(record, dict):
        if "mobile" in record:
            mobile = record["mobile"]

            try:
                if is_valid_mobile(record["mobile"]):
                    for x, user in enumerate(data['records']):
                        if user["mobile"] == mobile:
                            logging.info(f"User details found -->> {user}")
                            # print(f"User details found -->> {user}")
                            delete_user = data['records'].pop(x)
                            logging.info(f"User deleted successfully in DELETE METHOD: {delete_user}")
                            return delete_user

                    logging.warning(f"No user details found for mobile number {mobile} so DELETION is not possible.")
                    # print(f"No user details found for mobile number {mobile}.")
                    return {"error": "User details not found"}
            except ValueError as err:
                logging.error(f"Error: {err}")
                return {"error": str(err)}

        else:
            logging.error("Missing mobile key in the record for DELETION METHOD.")
            return {"error": "Missing mobile key in the record"}
    else:
        logging.error(f"Incorrect record type in DELETE METHOD {type(record)}.")
        return {"error": f"Incorrect record type {type(record)}"}


print(delete_user_details({"mobile": 915421215451}))
print(f"Users are -->> {data}")
