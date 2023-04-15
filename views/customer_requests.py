CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

def get_all_customers():
    """GETS ALL CUSTOMER OBJECTS """
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    """ GETS A SINGLE EMPLOYEE OBJECT USING ID AS INPUT"""
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last location in the list
    """ADDS NEW CUSTOMER TO THE END OF THE CUSTOMER  DICTIONARY"""
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    customer["id"] = new_id

    # Add the location dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def update_customer(id, new_customer):
    """UPDATES CUSTOMER"""
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break