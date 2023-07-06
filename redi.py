import webbrowser

def password():
    user_attempt = input("Username: ")
    password_attempt = input("Password: ")

    if user_attempt.lower() == "shea" and password_attempt == "pixel0101":
        print("Login successful.")
        file_path = "file:///C:/Users/sheab/OneDrive/Documents/Python1/sheaC.html"
        webbrowser.open(file_path)
    else:
        print("Incorrect password or username. Please try again later.")

password()  # Call the function only once