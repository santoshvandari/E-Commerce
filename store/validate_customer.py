def validate_customer(customer):
    error_message = None
    if not customer.first_name:
        error_message = "Please Enter your First Name!"
    elif len(customer.first_name) < 3:
        error_message = 'First Name must be 3 characters long or more'
    elif not customer.last_name:
        error_message = 'Please Enter your Last Name'
    elif len(customer.last_name) < 3:
        error_message = 'Last Name must be 3 characters long or more'
    elif not customer.phone:
        error_message = 'Enter your Phone Number'
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must be 10 characters long'
    elif len(customer.password) < 5:
        error_message = 'Password must be 5 characters long'
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 characters long'
    elif customer.isExists():
        error_message = 'Email Address Already Registered'
    return error_message