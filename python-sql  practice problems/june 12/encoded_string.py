"""In this Python challenge, you need to write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
An example input would be “Robert000Smith000123”. The function should return the following using that input:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }"""

import re

def encoded_string(encoded_str):
    parts = re.split('0+', encoded_str)

    if len(parts) != 3:
        raise ValueError("Encoded string is not in the correct format.")

    first_name, last_name, id_number = parts
    return {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_number
    }
str = input()
encoded_string(str)
