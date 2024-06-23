def is_valid_name(name, mobile):
    """
    Function to validate the name
    :param name: Str
    :return: Bool
    """
    print(f"{name} being validated for {mobile}")
    # name = "Kumar Makala" "Kumar.M" "M.Kumar" "M Kumar" "M_Kumar"
    name = name.replace(".", "").replace(" ", "").replace("_", "")

    # Check the length of the name if less than 2 chars raise exception
    if len(name) > 2:
        pass
    else:
        raise ValueError(f"User name cannot be {len(name)} character for user mobile -user mobile -{mobile}")

    # Check if the name string has only alphabets otherwise raise exception
    if name.isalpha():
        pass
    else:
        raise ValueError(f"User name {name} must be str only user mobile -{mobile}")

    # Return True if all above conditions are True
    print(f"{name} validated successfully")
    return True
