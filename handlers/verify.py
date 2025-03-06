def verify_username(username):
    if(len(username) < 6):
        return False
    return True


def verify_password(password):
    if(len(password) < 8):
        return ("Please make sure you have more than 8 characters",False)
    if(not any(char.isdigit() for char in password)):
        return ("Please make sure you have a number in your password",False)

    if(not any(char.isupper() for char in password)):
        return ("Please make sure you have an uppercase letter",False)

    if(not any(char.islower() for char in password)):
        return ("Please make sure you have a lowercase letter",False)

    return ("All Good!", True)